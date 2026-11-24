"""Normalize native Word equation structures without touching manuscript text."""

import re
import xml.etree.ElementTree as ET

from omml_typography import normalize_typography

MATH = "http://schemas.openxmlformats.org/officeDocument/2006/math"
WORD = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def _underbraces(tree: ET.Element) -> None:
    """Use Word's stretchable underbrace instead of a lowered glyph.

    Pandoc represents TeX underbraces as nested lower limits. The inner
    limit contains a literal brace glyph, which need not stretch over its
    expression. Preserve the annotation and replace only that inner node.
    """
    for parent in list(tree.iter()):
        for node in list(parent):
            if node.tag != f"{{{MATH}}}limLow":
                continue
            expression = node.find(f"{{{MATH}}}e")
            limit = node.find(f"{{{MATH}}}lim")
            if (
                expression is None
                or limit is None
                or "".join(limit.itertext()).strip() != "⏟"
            ):
                continue
            brace = ET.Element(f"{{{MATH}}}groupChr")
            properties = ET.SubElement(brace, f"{{{MATH}}}groupChrPr")
            for key, value in (("chr", "⏟"), ("pos", "bot"), ("vertJc", "top")):
                ET.SubElement(properties, f"{{{MATH}}}{key}", {f"{{{MATH}}}val": value})
            brace.append(expression)
            parent[list(parent).index(node)] = brace


def _alignment(tree: ET.Element) -> None:
    for array in tree.iter(f"{{{MATH}}}eqArr"):
        for row in array.findall(f"{{{MATH}}}e"):
            for index, node in enumerate(list(row)):
                if node.tag != f"{{{MATH}}}r" or "".join(node.itertext()) != "&":
                    continue
                row.remove(node)
                following = list(row)[index]
                properties = following.find(f"{{{MATH}}}rPr")
                if properties is None:
                    properties = ET.Element(f"{{{MATH}}}rPr")
                    following.insert(0, properties)
                ET.SubElement(properties, f"{{{MATH}}}aln")


def _roman_labels(tree: ET.Element) -> None:
    # Preserve Roman labels as words, rather than separate variables.
    for parent in list(tree.iter()):
        pending = None
        for node in list(parent):
            text = node.find(f"{{{MATH}}}t") if node.tag == f"{{{MATH}}}r" else None
            properties = node.find(f"{{{MATH}}}rPr")
            style = (
                properties.find(f"{{{MATH}}}sty") if properties is not None else None
            )
            upright_word = (
                text is not None
                and re.fullmatch(r"[A-Za-z]+", text.text or "")
                and style is not None
                and style.get(f"{{{MATH}}}val") == "p"
                and properties.find(f"{{{MATH}}}scr") is None
            )
            if not upright_word:
                pending = None
                continue
            if properties.find(f"{{{MATH}}}nor") is None:
                position = 1 if properties.find(f"{{{MATH}}}lit") is not None else 0
                properties.insert(position, ET.Element(f"{{{MATH}}}nor"))
            properties.remove(style)
            if pending is None:
                pending = node
            else:
                pending.find(f"{{{MATH}}}t").text += text.text
                parent.remove(node)


def normalize_omml(tree: ET.Element) -> None:
    """Normalize Word math groups, alignment and Roman labels in place."""
    _underbraces(tree)
    _alignment(tree)
    _roman_labels(tree)
    normalize_typography(tree)
    for properties in tree.iter(f"{{{MATH}}}rPr"):
        if properties.find(f"{{{MATH}}}nor") is not None:
            for style in properties.findall(f"{{{MATH}}}sty"):
                properties.remove(style)
