#!/usr/bin/env python3
"""Check exported content, editable equations, native tables and journal styles."""

import argparse
import hashlib
import json
import re
import unicodedata
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path
from typing import Any

from latex_source import BUILD
from setup_docx import ARTICLE
from word_document import MATH_FONT, MATH_SIZE, NS, W, walk_nodes

MATH = "http://schemas.openxmlformats.org/officeDocument/2006/math"
DRAWING = "http://schemas.openxmlformats.org/drawingml/2006/main"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def normalized(text: str) -> str:
    # Pandoc inserts a zero-width space in otherwise empty mathematical cells.
    return "".join(unicodedata.normalize("NFKC", text).replace("\u200b", "").split())


def source_text(document: dict[str, Any]) -> str:
    fragments = []
    for node in walk_nodes(document["blocks"]):
        if node["t"] == "Str":
            fragments.append(node["c"])
        elif node["t"] == "Code":
            fragments.append(node["c"][1])
        elif node["t"] == "Math":
            number = re.search(r"\\qquad\\text\{(\(\d+\))\}$", node["c"][1])
            if number:
                fragments.append(number[1])
    return "".join(fragments)


def check_content(document: ET.Element, manifest: dict[str, Any]) -> dict[str, int]:
    counts = {
        "math": len(document.findall(f".//{{{MATH}}}oMath")),
        "figures": len(document.findall(f".//{{{DRAWING}}}blip")),
        "tables": len(document.findall(".//w:tbl", NS)),
        "bibliography": len(manifest["bibliography_keys"]),
    }
    require(
        counts["math"] == manifest["math_count"],
        "A formula was lost or exported without editable OMML",
    )
    require(counts["figures"] == len(manifest["figures"]), "Figure count changed")
    require(counts["tables"] == manifest["table_count"], "A native Word table was lost")
    ast = json.loads((BUILD / "article.json").read_text())
    expected = normalized(source_text(ast))
    actual = normalized(
        "".join(node.text or "" for node in document.findall(".//w:t", NS))
    )
    (BUILD / "expected-text.txt").write_text(expected)
    (BUILD / "actual-text.txt").write_text(actual)
    require(
        actual == expected,
        "Word text differs from the prepared article; see build/docx/*-text.txt",
    )
    require(
        not re.search(r"\[(?:eq|fig|tab|sec|st):|\\(?:cite|eqref|ref)\{", actual),
        "An unresolved reference remains",
    )
    for path, digest in manifest["source_sha256"].items():
        require(
            hashlib.sha256((ARTICLE / path).read_bytes()).hexdigest() == digest,
            f"Export is stale: {path}",
        )
    for table in document.findall(".//w:tbl", NS):
        width = table.find("w:tblPr/w:tblW", NS)
        require(
            width is not None and width.get("{" + W + "}w") == "9071",
            "Table width exceeds the 16 cm profile",
        )
    numbers = []
    for paragraph in document.findall(".//w:p", NS):
        style = paragraph.find("w:pPr/w:pStyle", NS)
        if style is None or style.get("{" + W + "}val") != "Equation":
            continue
        numbers.append("".join(n.text or "" for n in paragraph.findall("w:r/w:t", NS)))
        require(
            paragraph.find("w:pPr/w:tabs/w:tab[@w:val='right']", NS) is not None,
            "An equation number has no right-aligned tab stop",
        )
    require(
        numbers == [f"({item['number']})" for item in manifest["equations"]],
        "Equation numbers changed or remain embedded inside mathematics",
    )
    for run in document.findall(f".//{{{MATH}}}r"):
        font = run.find("w:rPr/w:rFonts", NS)
        size = run.find("w:rPr/w:sz", NS)
        require(
            font is not None and font.get("{" + W + "}ascii") == MATH_FONT,
            "An equation run has no explicit math font",
        )
        require(
            size is not None and size.get("{" + W + "}val") == str(MATH_SIZE),
            "An equation run has no explicit font size",
        )
    return counts


def check_styles(styles: ET.Element) -> None:
    defaults = styles.find("w:docDefaults/w:rPrDefault/w:rPr", NS)
    fonts = defaults.find("w:rFonts", NS)
    require(
        fonts is not None and fonts.get("{" + W + "}ascii") == "Times New Roman",
        "Wrong main font",
    )
    require(
        defaults.find("w:sz", NS).get("{" + W + "}val") == "28",
        "Main font is not 14 pt",
    )
    for identifier in ("Normal", "BodyText", "FirstParagraph"):
        style = styles.find(f"w:style[@w:styleId='{identifier}']", NS)
        spacing = style.find("w:pPr/w:spacing", NS)
        require(
            spacing is not None and spacing.get("{" + W + "}line") == "360",
            f"Wrong line spacing in {identifier}",
        )


def submission_reminders() -> list[str]:
    """Report content work without inventing translations or author details."""
    return [
        "The journal template requests bilingual title, abstract "
        "and author information; review the current front matter.",
        "Check each abstract against the template's 500-character limit "
        "and reduce keywords to at most five.",
        "Supply a verified UDC classification and complete author/contact information.",
        "The user chose DOCX with modern editable OMML equations "
        "rather than legacy Equation 3.0 objects.",
        "This export does not validate scientific claims, bibliography metadata "
        "or editorial acceptance.",
        "Inspect a PDF rendered from the DOCX and open the document "
        "in Microsoft Word before submission.",
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("document", type=Path)
    args = parser.parse_args()
    manifest = json.loads((BUILD / "manifest.json").read_text())
    with zipfile.ZipFile(args.document) as package:
        require(package.testzip() is None, "Corrupt DOCX archive")
        document = ET.fromstring(package.read("word/document.xml"))
        styles = ET.fromstring(package.read("word/styles.xml"))
        settings = ET.fromstring(package.read("word/settings.xml"))
        font = settings.find(f"{{{MATH}}}mathPr/{{{MATH}}}mathFont")
        require(
            font is not None and font.get("{" + MATH + "}val") == MATH_FONT,
            "The document's default math font is missing",
        )
        images = {
            hashlib.sha256(package.read(name)).hexdigest()
            for name in package.namelist()
            if name.startswith("word/media/")
        }
        require(
            images == {figure["sha256"] for figure in manifest["figures"]},
            "Embedded figure content differs from the compiled TikZ figures",
        )
    counts = check_content(document, manifest)
    check_styles(styles)
    report = {
        "checks": "passed",
        "counts": counts,
        "submission_reminders": submission_reminders(),
    }
    (BUILD / "validation.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    )
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
