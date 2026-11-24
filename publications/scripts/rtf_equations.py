"""Preserve native Office Math when an RTF layout exporter falls back to pictures.

The surrounding RTF must already contain one mmath group per DOCX equation,
in document order. Only those groups are replaced; body text and artwork stay
with the layout exporter. Unsupported OMML constructs fail explicitly.
"""

from pathlib import Path
import re
import xml.etree.ElementTree as ET
import zipfile

from omml import MATH, WORD
from math_alphabets import alphabet_text

M = "{" + MATH + "}"
W = "{" + WORD + "}"
CONTAINERS = set(
    "oMath acc accPr box boxPr d dPr den e eqArr f fPr groupChr groupChrPr lim limLow nary naryPr num sSub sSubSup sSup sub sup".split()
)
CHARACTERS = {"begChr", "endChr", "chr", "sepChr"}
ENUMS = {"limLoc", "pos", "type", "vertJc"}
SWITCHES = {"grow", "subHide", "supHide", "opEmu"}
SCRIPTS = {
    "roman": 0,
    "script": 1,
    "fraktur": 2,
    "double-struck": 3,
    "sans-serif": 4,
    "monospace": 5,
}
STYLES = {"p": 0, "b": 1, "i": 2, "bi": 3}
CONTROL = re.compile(rb"\\([A-Za-z]+)(-?\d+)? ?")
MATH_GROUP = re.compile(rb"\{\s*\\mmath(?=[^A-Za-z]|$)")


def escape_rtf(text: str) -> str:
    output = []
    for char in text:
        if char in "\\{}":
            output.append("\\" + char)
        elif 32 <= ord(char) < 127:
            output.append(char)
        else:
            data = char.encode("utf-16-le")
            for index in range(0, len(data), 2):
                value = int.from_bytes(data[index : index + 2], "little", signed=True)
                output.append(f"\\u{value}?")
    return "".join(output)


def math_group_spans(data: bytes) -> list[tuple[int, int]]:
    """Find complete mmath groups, honoring escaped braces and binary data."""
    stack = []
    spans = []
    position = 0
    while position < len(data):
        char = data[position : position + 1]
        if char == b"\\":
            control = CONTROL.match(data, position)
            if control:
                position = control.end()
                if control[1] == b"bin":
                    length = int(control[2] or b"0")
                    if length < 0 or position + length > len(data):
                        raise ValueError("Invalid RTF binary length")
                    position += length
                continue
            position += 2
            continue
        if char == b"{":
            opening = MATH_GROUP.match(data, position)
            stack.append((position, opening is not None))
        elif char == b"}":
            if not stack:
                raise ValueError("Unbalanced RTF group")
            start, math = stack.pop()
            if math:
                spans.append((start, position + 1))
        position += 1
    if stack:
        raise ValueError("Unclosed RTF group")
    return sorted(spans)


def _font_ids(data: bytes) -> dict[str, int]:
    fonts = {}
    for match in re.finditer(rb"\{\\f(\d+)([^{};]*);", data):
        name = (
            re.sub(rb"\\[A-Za-z]+-?\d* ?", b"", match[2])
            .strip()
            .decode("ascii", errors="ignore")
        )
        if name:
            fonts[name] = int(match[1])
    return fonts


def _serialize(node: ET.Element, fonts: dict[str, int]) -> str:
    name = node.tag.removeprefix(M)
    if name == "t":
        return escape_rtf(node.text or "")
    if name == "r":
        properties = node.find(M + "rPr")
        styled = alphabet_text(node)
        settings = "\\mnor " + "\\i0 \\b0 " if styled is not None else ""
        if properties is not None:
            if styled is None and properties.find(M + "nor") is not None:
                settings += "\\mnor "
            script = properties.find(M + "scr")
            style = properties.find(M + "sty")
            if script is not None and styled is None:
                settings += "\\mscr" + str(SCRIPTS[script.get(M + "val")]) + " "
            if style is not None and styled is None:
                settings += "\\msty" + str(STYLES[style.get(M + "val")]) + " "
            if properties.find(M + "aln") is not None:
                settings += "{\\maln on}"
        word = node.find(W + "rPr")
        if word is not None:
            family = word.find(W + "rFonts")
            if family is not None:
                selected = family.get(W + "ascii")
                if selected not in fonts:
                    raise ValueError(f"RTF font table has no {selected}")
                settings += f"\\f{fonts[selected]} "
            for tag, control in (("sz", "fs"), ("i", "i"), ("b", "b")):
                value = word.find(W + tag)
                if value is not None:
                    settings += "\\" + control + value.get(W + "val", "1") + " "
        content = (
            escape_rtf(styled)
            if styled is not None
            else "".join(
                _serialize(child, fonts) for child in node if child.tag == M + "t"
            )
        )
        return "{\\mr " + settings + content + "}"

    if name in CHARACTERS:
        return "{\\m" + name + " " + escape_rtf(node.get(M + "val", "")) + "}"
    if name in ENUMS:
        return "{\\m" + name + " " + node.get(M + "val", "").lower() + "}"
    if name in SWITCHES:
        value = node.get(M + "val", "on")
        return (
            "{\\m"
            + name
            + " "
            + ("off" if value in {"0", "off", "false"} else "on")
            + "}"
        )
    if name in CONTAINERS:
        prefix = "{\\*\\moMath\\uc1 " if name == "oMath" else "{\\m" + name + " "
        return prefix + "".join(_serialize(child, fonts) for child in node) + "}"
    raise ValueError(f"Unsupported OMML element in RTF export: {name}")


def restore_native_math(document: Path, rtf: Path) -> int:
    """Replace picture-only math groups with their editable DOCX structures."""
    with zipfile.ZipFile(document) as package:
        tree = ET.fromstring(package.read("word/document.xml"))
    equations = list(tree.iter(M + "oMath"))
    data = rtf.read_bytes()
    fonts = _font_ids(data)
    required = {
        font.get(W + "ascii")
        for equation in equations
        for font in equation.iter(W + "rFonts")
        if font.get(W + "ascii")
    }
    missing = sorted(required - fonts.keys())
    if missing:
        table = re.search(rb"\{\\fonttbl(?=[^A-Za-z]|$)", data)
        if table is None:
            raise ValueError("RTF has no font table")
        next_id = (
            max((int(value) for value in re.findall(rb"\{\\f(\d+)", data)), default=-1)
            + 1
        )
        entries = []
        for name in missing:
            if not name.isascii() or any(char in name for char in "{}\\;"):
                raise ValueError(f"Unsupported RTF font name: {name}")
            fonts[name] = next_id
            entries.append(f"{{\\f{next_id}\\fnil\\fcharset0 {name};}}".encode("ascii"))
            next_id += 1
        data = data[: table.end()] + b"".join(entries) + data[table.end() :]
    spans = math_group_spans(data)
    if len(spans) != len(equations):
        raise ValueError(f"RTF has {len(spans)} math groups; DOCX has {len(equations)}")
    replacements = [
        b"{\\mmath " + _serialize(equation, fonts).encode("ascii") + b"}"
        for equation in equations
    ]
    for (start, end), replacement in reversed(
        list(zip(spans, replacements, strict=True))
    ):
        data = data[:start] + replacement + data[end:]
    if len(math_group_spans(data)) != len(equations) or b"\\mmathPict" in data:
        raise ValueError("RTF math replacement failed")
    temporary = rtf.with_suffix(".tmp.rtf")
    temporary.write_bytes(data)
    temporary.replace(rtf)
    return len(equations)
