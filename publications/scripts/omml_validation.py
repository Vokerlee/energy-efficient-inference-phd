"""Validate native mathematics in a saved DOCX independently of its profile."""

from pathlib import Path
import re
import xml.etree.ElementTree as ET
import zipfile

from omml_format import MATH, WORD


def validate_omml(path: Path, *, expected_count: int | None = None) -> int:
    """Check the saved package, including equations inside drawing labels.

    Images may represent figures. Every source math expression must still
    have its own OMML element; an image or plain-text substitute fails the
    expected-count check. This does not claim rendering compatibility with
    an untested editor such as Google Docs.
    """
    if path.suffix.lower() != ".docx":
        raise ValueError("Native Word equations require DOCX output")
    with zipfile.ZipFile(path) as package:
        if package.testzip() is not None:
            raise ValueError("Corrupt DOCX package")
        count = 0
        for member in package.namelist():
            if member.startswith("word/embeddings/"):
                raise ValueError("Embedded OLE/MathType objects are forbidden")
            if member.endswith(".rels"):
                relationships = ET.fromstring(package.read(member))
                if any(
                    item.get("Type", "").endswith("/oleObject")
                    for item in relationships
                ):
                    raise ValueError("An OLE equation relationship remains")
            if not member.startswith("word/") or not member.endswith(".xml"):
                continue
            tree = ET.fromstring(package.read(member))
            if tree.find(f".//{{{WORD}}}object") is not None:
                raise ValueError("Legacy Word objects are forbidden")
            for equation in tree.iter(f"{{{MATH}}}oMath"):
                for properties in equation.iter(f"{{{MATH}}}rPr"):
                    if (
                        properties.find(f"{{{MATH}}}nor") is not None
                        and properties.find(f"{{{MATH}}}sty") is not None
                    ):
                        raise ValueError(
                            "Normal Word math text cannot also have a math style"
                        )
                text = "".join(
                    node.text or "" for node in equation.iter(f"{{{MATH}}}t")
                )
                if not text.strip():
                    raise ValueError("An OMML equation is empty")
                if re.search(r"\\(?:frac|begin|sum|sqrt|widetilde|vec)\b", text):
                    raise ValueError("Unconverted LaTeX remains inside an equation")
                if any(
                    "\ue000" <= char <= "\uf8ff" or char == "\ufffd" for char in text
                ):
                    raise ValueError(
                        "A font-specific or missing glyph remains in an equation"
                    )
                count += 1
    if expected_count is not None and count != expected_count:
        raise ValueError(f"Expected {expected_count} OMML equations; found {count}")
    return count
