"""Unicode mathematical alphabets and semantic text shared by Word exporters."""

import unicodedata
import xml.etree.ElementTree as ET

from omml import MATH, WORD

M = "{" + MATH + "}"
W = "{" + WORD + "}"

ALPHABETS = {"script": "SCRIPT", "double-struck": "DOUBLE-STRUCK", "fraktur": "FRAKTUR"}
LETTERLIKE = {
    "SCRIPT": dict(zip("BEFHILMRego", "ℬℰℱℋℐℒℳℛℯℊℴ", strict=True)),
    "DOUBLE-STRUCK": dict(zip("CHNPQRZ", "ℂℍℕℙℚℝℤ", strict=True)),
    "FRAKTUR": dict(zip("CHIRZ", "ℭℌℑℜℨ", strict=True)),
}


def alphabet_text(run: ET.Element) -> str | None:
    script = run.find(M + "rPr/" + M + "scr")
    if script is None or script.get(M + "val") not in ALPHABETS:
        return None
    style = run.find(M + "rPr/" + M + "sty")
    if style is not None and style.get(M + "val") != "p":
        return None
    name = ALPHABETS[script.get(M + "val")]
    output = []
    for char in "".join(node.text or "" for node in run.findall(M + "t")):
        if char in LETTERLIKE[name]:
            output.append(LETTERLIKE[name][char])
        elif char.isascii() and char.isalpha():
            try:
                output.append(
                    unicodedata.lookup(
                        f"MATHEMATICAL {name} {'CAPITAL' if char.isupper() else 'SMALL'} {char.upper()}"
                    )
                )
            except KeyError:
                return None
        else:
            return None
    return "".join(output)


def equation_text(tree: ET.Element) -> str:
    """Read semantic text, retaining mathematical alphabets and delimiters."""
    if tree.tag in {M + "t", W + "t"}:
        return tree.text or ""
    if tree.tag == M + "r":
        styled = alphabet_text(tree)
        return (
            styled
            if styled is not None
            else "".join(node.text or "" for node in tree.findall(M + "t"))
        )
    if tree.tag == M + "nary":
        operator = tree.find(M + "naryPr/" + M + "chr")
        return (operator.get(M + "val", "") if operator is not None else "") + "".join(
            equation_text(child) for child in tree if child.tag != M + "naryPr"
        )
    if tree.tag == M + "d":
        opening = tree.find(M + "dPr/" + M + "begChr")
        closing = tree.find(M + "dPr/" + M + "endChr")
        separator = tree.find(M + "dPr/" + M + "sepChr")
        return (
            (opening.get(M + "val") if opening is not None else "(")
            + (separator.get(M + "val") if separator is not None else "|").join(
                equation_text(node) for node in tree.findall(M + "e")
            )
            + (closing.get(M + "val") if closing is not None else ")")
        )
    return "".join(equation_text(child) for child in tree)
