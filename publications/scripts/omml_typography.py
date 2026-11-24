"""Preserve explicit TeX spacing and variable styles in native Word math."""

import unicodedata
import xml.etree.ElementTree as ET

MATH = "http://schemas.openxmlformats.org/officeDocument/2006/math"
XML_SPACE = "{http://www.w3.org/XML/1998/namespace}space"


def normalize_typography(tree: ET.Element) -> None:
    """Make implicit variable italics explicit; retain intentional Roman text.

    Pandoc emits U+2001 EM QUAD for TeX's quad spacing. Canonical EM SPACE
    has the same width and is also Word's native LaTeX mapping. Mark spacing
    runs as normal text so equation layout preserves the specified glue
    rather than applying operator spacing to it. Automatic spacing around
    operators remains the equation editor's responsibility.
    """
    for run in tree.iter(f"{{{MATH}}}r"):
        text = run.find(f"{{{MATH}}}t")
        if text is None or not text.text:
            continue
        text.text = text.text.replace("\u2001", "\u2003").replace("\u2000", "\u2002")
        properties = run.find(f"{{{MATH}}}rPr")
        if properties is None:
            properties = ET.Element(f"{{{MATH}}}rPr")
            run.insert(0, properties)
        if text.text.isspace():
            text.set(XML_SPACE, "preserve")
            if properties.find(f"{{{MATH}}}nor") is None:
                # m:lit, when present, precedes m:nor in the schema.
                index = 1 if properties.find(f"{{{MATH}}}lit") is not None else 0
                properties.insert(index, ET.Element(f"{{{MATH}}}nor"))
            for style in properties.findall(f"{{{MATH}}}sty"):
                properties.remove(style)
        elif (
            properties.find(f"{{{MATH}}}nor") is None
            and properties.find(f"{{{MATH}}}sty") is None
            and properties.find(f"{{{MATH}}}scr") is None
            and all(
                unicodedata.name(c, "").startswith("GREEK ") and c.islower()
                for c in text.text
            )
        ):
            # A style supplied by \mathrm, \text, \mathbf, etc. wins.
            ET.SubElement(properties, f"{{{MATH}}}sty", {f"{{{MATH}}}val": "i"})
