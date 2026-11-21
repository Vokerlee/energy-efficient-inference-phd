"""Apply the journal profile to Pandoc documents and native Word styles."""

import io
import re
import subprocess
import xml.etree.ElementTree as ET
import zipfile
from collections.abc import Callable, Iterator
from pathlib import Path
from typing import Any

from setup_docx import ARTICLE, PANDOC

BUILD = ARTICLE / "build" / "docx"

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
NS = {"w": W}
M = "http://schemas.openxmlformats.org/officeDocument/2006/math"
MATH_FONT = "Cambria Math"
MATH_SIZE = 28

# OOXML property elements are ordered sequences, not unordered mappings.
PROPERTY_ORDER = {
    "style": "name aliases basedOn next link autoRedefine hidden uiPriority "
    "semiHidden unhideWhenUsed qFormat locked personal personalCompose "
    "personalReply rsid pPr rPr tblPr trPr tcPr tblStylePr",
    "tblPr": "tblStyle tblpPr tblOverlap bidiVisual tblStyleRowBandSize "
    "tblStyleColBandSize tblW jc tblCellSpacing tblInd tblBorders shd "
    "tblLayout tblCellMar tblLook tblCaption tblDescription tblPrChange",
    "tcPr": "cnfStyle tcW gridSpan hMerge vMerge tcBorders shd noWrap tcMar "
    "textDirection tcFitText vAlign hideMark headers cellIns cellDel "
    "cellMerge tcPrChange",
    "pPr": "pStyle keepNext keepLines pageBreakBefore framePr widowControl numPr "
    "suppressLineNumbers pBdr shd tabs suppressAutoHyphens kinsoku wordWrap "
    "overflowPunct topLinePunct autoSpaceDE autoSpaceDN bidi adjustRightInd "
    "snapToGrid spacing ind contextualSpacing mirrorIndents suppressOverlap jc "
    "textDirection textAlignment textboxTightWrap outlineLvl divId cnfStyle "
    "rPr sectPr pPrChange",
    "rPr": "rStyle rFonts b bCs i iCs caps smallCaps strike dstrike outline shadow "
    "emboss imprint noProof snapToGrid vanish webHidden color spacing w kern "
    "position sz szCs highlight u effect bdr shd fitText vertAlign rtl cs em lang "
    "eastAsianLayout specVanish oMath rPrChange",
}


def order_properties(tree: ET.Element) -> None:
    for name, sequence in PROPERTY_ORDER.items():
        positions = {
            "{" + W + "}" + tag: index for index, tag in enumerate(sequence.split())
        }
        for properties in tree.iter("{" + W + "}" + name):
            properties[:] = sorted(
                properties, key=lambda child: positions.get(child.tag, len(positions))
            )


def walk_nodes(value: Any) -> Iterator[dict[str, Any]]:
    if isinstance(value, dict):
        if "t" in value:
            yield value
        for child in value.values():
            yield from walk_nodes(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_nodes(child)


def prepare_document_ast(
    document: dict[str, Any], labels: dict[str, str]
) -> dict[str, Any]:
    counts = [0, 0, 0, 0]
    for node in walk_nodes(document):
        kind, content = node["t"], node.get("c")
        if kind in ("RawBlock", "RawInline"):
            # PDF-only spacing commands have no Word content to preserve.
            if re.fullmatch(
                r"\\(?:clearpage|smallskip|noindent|centering|vspace\{[^}]+\})\s*",
                content[1],
            ):
                node.update(
                    t="Plain" if kind == "RawBlock" else "Str",
                    c=[] if kind == "RawBlock" else "",
                )
            else:
                raise ValueError(f"Unconverted TeX: {content}")
        elif kind == "Header" and content[0] <= 3 and "unnumbered" not in content[1][1]:
            level = content[0] - 1
            counts[level] += 1
            counts[level + 1 :] = [0] * (len(counts) - level - 1)
            number = ".".join(map(str, counts[: level + 1]))
            content[2][:0] = [{"t": "Str", "c": number + "."}, {"t": "Space"}]
        elif kind == "Math":
            # LibreOffice escapes parentheses inside an OMML normal-text run.
            # Leave numeric equation tags intact until format_equations moves them.
            def delimiters(match: re.Match[str]) -> str:
                text = match[1]
                return match[0] if text.isdecimal() else r"(\text{" + text + "})"

            content[1] = re.sub(r"\\text\{\(([^{}]*)\)\}", delimiters, content[1])
        elif kind in ("Figure", "Table"):
            key = content[0][0]
            prefix = "Рис." if kind == "Figure" else "Таблица"
            caption = content[1][1]
            caption[0]["c"][:0] = [
                {"t": "Str", "c": f"{prefix} {labels[key]}."},
                {"t": "Space"},
            ]
    return document


def xml_child(parent: ET.Element, name: str, **attributes: str | int) -> ET.Element:
    child = parent.find("w:" + name, NS)
    if child is None:
        child = ET.SubElement(parent, "{" + W + "}" + name)
    for key, value in attributes.items():
        child.set("{" + W + "}" + key, str(value))
    return child


def rewrite_docx(
    path: Path, transformations: dict[str, Callable[[ET.Element], None]]
) -> None:
    temporary = path.with_suffix(".tmp.docx")
    with (
        zipfile.ZipFile(path) as source,
        zipfile.ZipFile(temporary, "w", zipfile.ZIP_DEFLATED) as target,
    ):
        for member in source.infolist():
            data = source.read(member.filename)
            if member.filename in transformations:
                namespaces = dict(
                    value
                    for _, value in ET.iterparse(io.BytesIO(data), events=["start-ns"])
                )
                for prefix, namespace in namespaces.items():
                    ET.register_namespace(prefix, namespace)
                tree = ET.fromstring(data)
                transformations[member.filename](tree)
                order_properties(tree)
                # Prefixes referenced by mc:Ignorable must survive serialization,
                # even when no remaining element uses that extension namespace.
                ignorable = "{http://schemas.openxmlformats.org/markup-compatibility/2006}Ignorable"
                serialized = ET.tostring(tree, encoding="unicode")
                for prefix in tree.get(ignorable, "").split():
                    if f"xmlns:{prefix}=" not in serialized:
                        tree.set(f"xmlns:{prefix}", namespaces[prefix])
                data = ET.tostring(tree, encoding="utf-8", xml_declaration=True)
            target.writestr(member, data)
    temporary.replace(path)


def create_reference_docx() -> Path:
    reference = BUILD / "reference.docx"
    with reference.open("wb") as output:
        subprocess.run(
            [str(PANDOC), "--print-default-data-file=reference.docx"],
            stdout=output,
            check=True,
        )

    def styles(tree: ET.Element) -> None:
        defaults = tree.find("w:docDefaults/w:rPrDefault/w:rPr", NS)
        xml_child(
            defaults,
            "rFonts",
            ascii="Times New Roman",
            hAnsi="Times New Roman",
            cs="Times New Roman",
        )
        xml_child(defaults, "sz", val=28)
        xml_child(defaults, "szCs", val=28)
        xml_child(defaults, "lang", val="ru-RU")
        for style in tree.findall("w:style", NS):
            if style.get("{" + W + "}type") not in ("paragraph", "character"):
                continue
            identifier = style.get("{" + W + "}styleId", "")
            paragraph = xml_child(style, "pPr")
            xml_child(
                paragraph, "spacing", before=0, after=0, line=360, lineRule="auto"
            )
            runs = xml_child(style, "rPr")
            fonts = xml_child(
                runs,
                "rFonts",
                ascii="Times New Roman",
                hAnsi="Times New Roman",
                cs="Times New Roman",
            )
            for key in list(fonts.attrib):
                if "Theme" in key:
                    del fonts.attrib[key]
            xml_child(runs, "sz", val=28)
            xml_child(runs, "szCs", val=28)
            xml_child(runs, "color", val="000000")
            if identifier in ("BodyText", "FirstParagraph"):
                xml_child(paragraph, "jc", val="both")
                xml_child(paragraph, "ind", firstLine=709)
            if identifier.startswith("Heading"):
                xml_child(runs, "b")
                xml_child(
                    paragraph,
                    "spacing",
                    before=240,
                    after=120,
                    line=360,
                    lineRule="auto",
                )
            if "Caption" in identifier:
                xml_child(paragraph, "jc", val="center")
        for identifier in (
            "ArticleTitle",
            "ArticleAuthors",
            "ArticleAffiliation",
            "Equation",
        ):
            style = ET.SubElement(
                tree,
                "{" + W + "}style",
                {"{" + W + "}type": "paragraph", "{" + W + "}styleId": identifier},
            )
            xml_child(style, "name", val=identifier)
            xml_child(style, "basedOn", val="Normal")
            paragraph = xml_child(style, "pPr")
            xml_child(
                paragraph, "jc", val="left" if identifier == "Equation" else "center"
            )
            xml_child(
                paragraph, "spacing", before=0, after=120, line=360, lineRule="auto"
            )
            if identifier == "ArticleTitle":
                xml_child(xml_child(style, "rPr"), "b")

    def page(tree: ET.Element) -> None:
        section = tree.find(".//w:sectPr", NS)
        xml_child(section, "pgSz", w=11906, h=16838)
        xml_child(section, "pgMar", top=1134, bottom=1134, left=1417, right=1417)

    rewrite_docx(reference, {"word/styles.xml": styles, "word/document.xml": page})
    return reference


def format_document(tree: ET.Element) -> None:
    body = tree.find("w:body", NS)
    paragraphs = body.findall("w:p", NS)
    for paragraph, name in zip(
        paragraphs[:3], ("ArticleTitle", "ArticleAuthors", "ArticleAffiliation")
    ):
        xml_child(xml_child(paragraph, "pPr"), "pStyle", val=name)
    for paragraph in paragraphs:
        properties = xml_child(paragraph, "pPr")
        style = properties.find("w:pStyle", NS)
        if paragraph.find(".//w:drawing", NS) is not None or (
            style is not None and style.get("{" + W + "}val") == "TableCaption"
        ):
            xml_child(properties, "keepNext")
    # Fix native tables to 16 cm, preserving merged cells and their contents.
    width = 9071
    for table in body.findall("w:tbl", NS):
        properties = xml_child(table, "tblPr")
        xml_child(properties, "tblW", w=width, type="dxa")
        xml_child(properties, "tblLayout", type="fixed")
        grid = table.find("w:tblGrid", NS)
        columns = list(grid)
        weights = [max(1, int(column.get("{" + W + "}w", "1"))) for column in columns]
        sizes = [round(width * weight / sum(weights)) for weight in weights]
        sizes[-1] += width - sum(sizes)
        for column, size in zip(columns, sizes):
            column.set("{" + W + "}w", str(size))
        for row in table.findall("w:tr", NS):
            offset = 0
            for cell in row.findall("w:tc", NS):
                cell_properties = xml_child(cell, "tcPr")
                span = cell_properties.find("w:gridSpan", NS)
                count = int(span.get("{" + W + "}val")) if span is not None else 1
                xml_child(
                    cell_properties,
                    "tcW",
                    w=sum(sizes[offset : offset + count]),
                    type="dxa",
                )
                offset += count
    format_equations(body)


def format_equations(body: ET.Element) -> None:
    """Keep equation numbers as text at the right tab stop, outside the math."""
    for paragraph in body.iter("{" + W + "}p"):
        display = paragraph.find("{" + M + "}oMathPara")
        if display is None:
            continue
        math = display.find("{" + M + "}oMath")
        final_run = list(math)[-1]
        number = "".join(final_run.itertext())
        if not re.fullmatch(r"\(\d+\)", number):
            continue
        math.remove(final_run)
        if len(math) and not "".join(list(math)[-1].itertext()).strip():
            math.remove(list(math)[-1])
        paragraph.remove(display)
        properties = xml_child(paragraph, "pPr")
        xml_child(properties, "pStyle", val="Equation")
        xml_child(properties, "jc", val="left")
        xml_child(properties, "ind", left=0, right=0, firstLine=0)
        tabs = xml_child(properties, "tabs")
        for position, alignment in ((4535, "center"), (9071, "right")):
            ET.SubElement(
                tabs,
                "{" + W + "}tab",
                {"{" + W + "}val": alignment, "{" + W + "}pos": str(position)},
            )
        xml_child(ET.SubElement(paragraph, "{" + W + "}r"), "tab")
        paragraph.append(math)
        xml_child(ET.SubElement(paragraph, "{" + W + "}r"), "tab")
        xml_child(ET.SubElement(paragraph, "{" + W + "}r"), "t").text = number
    for run in body.iter("{" + M + "}r"):
        properties = run.find("w:rPr", NS)
        if properties is None:
            properties = ET.Element("{" + W + "}rPr")
            text = run.find("{" + M + "}t")
            run.insert(
                list(run).index(text) if text is not None else len(run), properties
            )
        xml_child(properties, "rFonts", ascii=MATH_FONT, hAnsi=MATH_FONT, cs=MATH_FONT)
        xml_child(properties, "sz", val=MATH_SIZE)
        xml_child(properties, "szCs", val=MATH_SIZE)


def format_math_settings(tree: ET.Element) -> None:
    properties = tree.find("{" + M + "}mathPr")
    if properties is None:
        properties = ET.Element("{" + M + "}mathPr")
        # mathPr precedes themeFontLang and trailing compatibility extensions.
        following = {
            "themeFontLang",
            "clrSchemeMapping",
            "doNotIncludeSubdocsInStats",
            "doNotAutoCompressPictures",
            "forceUpgrade",
            "captions",
            "readModeInkLockDown",
            "smartTagType",
            "schemaLibrary",
            "shapeDefaults",
            "doNotEmbedSmartTags",
            "decimalSymbol",
            "listSeparator",
        }
        position = next(
            (
                i
                for i, child in enumerate(tree)
                if child.tag.split("}")[-1] in following
            ),
            len(tree),
        )
        tree.insert(position, properties)
    font = properties.find("{" + M + "}mathFont")
    if font is None:
        font = ET.SubElement(properties, "{" + M + "}mathFont")
    font.set("{" + M + "}val", MATH_FONT)
