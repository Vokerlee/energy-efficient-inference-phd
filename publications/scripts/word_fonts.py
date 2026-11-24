"""Select and embed an editable OpenType math font in a native Word document."""

import hashlib
from pathlib import Path
import struct
import uuid
import xml.etree.ElementTree as ET
import zipfile

from word_document import M, W, format_math_settings, rewrite_docx, xml_child

REL = "http://schemas.openxmlformats.org/package/2006/relationships"
OFFICE_REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
TYPES = "http://schemas.openxmlformats.org/package/2006/content-types"
FONT_TYPE = "application/vnd.openxmlformats-officedocument.obfuscatedFont"
FONT_RELS = "word/_rels/fontTable.xml.rels"


def _check_font(data: bytes) -> None:
    if len(data) < 12 or data[:4] not in (b"OTTO", b"\x00\x01\x00\x00"):
        raise ValueError("Expected a standalone OpenType font")
    count = struct.unpack_from(">H", data, 4)[0]
    if 12 + 16 * count > len(data):
        raise ValueError("Truncated OpenType table directory")
    tables = {}
    for index in range(count):
        tag, _, offset, length = struct.unpack_from(">4sIII", data, 12 + 16 * index)
        if offset + length > len(data):
            raise ValueError("Truncated OpenType table")
        tables[tag] = data[offset : offset + length]
    if b"MATH" not in tables or len(tables.get(b"OS/2", b"")) < 10:
        raise ValueError("The font needs MATH and OS/2 tables")
    permissions = struct.unpack_from(">H", tables[b"OS/2"], 8)[0]
    if permissions & 0x200 or (permissions & 0xE and not permissions & 0x8):
        raise ValueError("The font does not permit editable outline embedding")


def obfuscate_font(data: bytes, key: uuid.UUID) -> bytes:
    """Apply ECMA-376 font obfuscation; the same operation decodes it."""
    if len(data) < 32:
        raise ValueError("An embedded font needs at least 32 bytes")
    mask = key.bytes[::-1]
    return (
        bytes(value ^ mask[index % 16] for index, value in enumerate(data[:32]))
        + data[32:]
    )


def _font_settings(tree: ET.Element, family: str) -> None:
    format_math_settings(tree)
    tree.find(f"{{{M}}}mathPr/{{{M}}}mathFont").set(f"{{{M}}}val", family)
    # This early part of CT_Settings is ordered, before proofState, etc.
    prefix = "writeProtection view zoom removePersonalInformation removeDateAndTime "
    prefix += (
        "doNotDisplayPageBoundaries displayBackgroundShape printPostScriptOverText "
    )
    prefix += "printFractionalCharacterWidth printFormsData embedTrueTypeFonts "
    prefix += "embedSystemFonts saveSubsetFonts"
    order = {f"{{{W}}}{name}": index for index, name in enumerate(prefix.split())}
    for name, value in (("embedTrueTypeFonts", "1"), ("saveSubsetFonts", "0")):
        node = xml_child(tree, name, val=value)
        tree.remove(node)
        position = next(
            (
                i
                for i, item in enumerate(tree)
                if order.get(item.tag, len(order)) > order[node.tag]
            ),
            len(tree),
        )
        tree.insert(position, node)


def embed_math_font(document: Path, font: Path, *, family: str) -> dict[str, str]:
    """Apply one math font throughout DOCX and embed its complete font data.

    Body text styles are preserved. Native OMML structures and their explicit
    italic/Roman choices remain intact. The full font allows editing with
    additional symbols. Consumers still control whether they honor embedded
    fonts; schema validity alone cannot establish a particular editor's layout.
    """
    if document.suffix.lower() != ".docx":
        raise ValueError("Native equation font embedding requires DOCX")
    data = font.read_bytes()
    _check_font(data)
    if not family.strip():
        raise ValueError("A font family name is required")
    digest = hashlib.sha256(data).hexdigest()
    key = uuid.uuid5(uuid.NAMESPACE_URL, "urn:sha256:" + digest)
    part = f"word/fonts/{digest[:24]}.odttf"
    with zipfile.ZipFile(document) as package:
        fonts = ET.fromstring(package.read("word/fontTable.xml"))
        relationships = (
            ET.fromstring(package.read(FONT_RELS))
            if FONT_RELS in package.namelist()
            else ET.Element(f"{{{REL}}}Relationships")
        )
        math_parts = [
            name
            for name in package.namelist()
            if name.startswith("word/")
            and name.endswith(".xml")
            and f"{{{M}}}oMath"
            in {item.tag for item in ET.fromstring(package.read(name)).iter()}
        ]
    entry = next((item for item in fonts if item.get(f"{{{W}}}name") == family), None)
    if entry is None:
        entry = ET.SubElement(fonts, f"{{{W}}}font", {f"{{{W}}}name": family})
    embedded = entry.find(f"{{{W}}}embedRegular")
    if embedded is None:
        embedded = ET.Element(f"{{{W}}}embedRegular")
        position = next(
            (
                i
                for i, item in enumerate(entry)
                if item.tag.rsplit("}", 1)[-1].startswith("embed")
            ),
            len(entry),
        )
        entry.insert(position, embedded)
    identifier = embedded.get(f"{{{OFFICE_REL}}}id")
    if identifier is None:
        used = {item.get("Id") for item in relationships}
        identifier = next(
            f"rIdMathFont{i}"
            for i in range(len(used) + 1)
            if f"rIdMathFont{i}" not in used
        )
    relationship = next(
        (item for item in relationships if item.get("Id") == identifier), None
    )
    if relationship is None:
        relationship = ET.SubElement(relationships, f"{{{REL}}}Relationship")
    relationship.attrib.update(
        Id=identifier, Type=OFFICE_REL + "/font", Target=part.removeprefix("word/")
    )
    embedded.attrib.update(
        {
            f"{{{OFFICE_REL}}}id": identifier,
            f"{{{W}}}fontKey": "{" + str(key).upper() + "}",
            f"{{{W}}}subsetted": "0",
        }
    )

    def select_font(tree: ET.Element) -> None:
        for equation in tree.iter(f"{{{M}}}oMath"):
            for run in equation.iter(f"{{{M}}}r"):
                properties = run.find(f"{{{W}}}rPr")
                if properties is None:
                    properties = ET.Element(f"{{{W}}}rPr")
                    text = run.find(f"{{{M}}}t")
                    run.insert(
                        list(run).index(text) if text is not None else len(run),
                        properties,
                    )
                fonts = xml_child(
                    properties,
                    "rFonts",
                    ascii=family,
                    hAnsi=family,
                    cs=family,
                    eastAsia=family,
                )
                for attribute in list(fonts.attrib):
                    if attribute.endswith("Theme"):
                        del fonts.attrib[attribute]

    def content_types(tree: ET.Element) -> None:
        if not any(item.get("Extension") == "odttf" for item in tree):
            ET.SubElement(
                tree, f"{{{TYPES}}}Default", Extension="odttf", ContentType=FONT_TYPE
            )

    def font_table(tree: ET.Element) -> None:
        tree[:] = list(fonts)

    staged = document.with_name(document.stem + ".font-stage.docx")
    try:
        with (
            zipfile.ZipFile(document) as source,
            zipfile.ZipFile(staged, "w", zipfile.ZIP_DEFLATED) as target,
        ):
            for item in source.infolist():
                if item.filename not in {part, FONT_RELS}:
                    target.writestr(item, source.read(item.filename))
            target.writestr(part, obfuscate_font(data, key))
            target.writestr(
                FONT_RELS,
                ET.tostring(relationships, encoding="utf-8", xml_declaration=True),
            )
        rewrite_docx(
            staged,
            {
                **dict.fromkeys(math_parts, select_font),
                "word/fontTable.xml": font_table,
                "word/settings.xml": lambda tree: _font_settings(tree, family),
                "[Content_Types].xml": content_types,
            },
        )
        staged.replace(document)
    finally:
        staged.unlink(missing_ok=True)
    return {"family": family, "sha256": digest, "part": part, "font_key": str(key)}
