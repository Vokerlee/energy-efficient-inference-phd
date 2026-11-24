"""Check embedded font bytes, equation styles and saved Word font selection."""

from pathlib import Path
import struct
import subprocess
import tempfile
import unittest
import uuid
import xml.etree.ElementTree as ET
import zipfile

from omml import MATH, WORD, validate_omml
from setup_docx import PANDOC
from word_fonts import OFFICE_REL, REL, _check_font, embed_math_font, obfuscate_font

LATIN_MODERN = Path(
    "/usr/share/texmf/fonts/opentype/public/lm-math/latinmodern-math.otf"
)


class EmbeddedFontTests(unittest.TestCase):
    def test_obfuscation_uses_the_standard_guid_byte_order(self) -> None:
        key = uuid.UUID("001B70DC-AA60-4AD5-90EC-18A0948E1EAE")
        mask = bytes.fromhex("AE1E8E94A018EC90D54A60AADC701B00")
        data = bytes(range(64))
        expected = (
            bytes(value ^ mask[index % 16] for index, value in enumerate(data[:32]))
            + data[32:]
        )
        self.assertEqual(obfuscate_font(data, key), expected)
        self.assertEqual(obfuscate_font(expected, key), data)

    def test_editable_embedding_is_required(self) -> None:
        # Minimal table directory exercises permissions without external fonts.
        for flags in (0, 8, 12, 2, 4, 0x200):
            with self.subTest(flags=flags):
                header = struct.pack(">4sHHHH", b"OTTO", 2, 0, 0, 0)
                tables = struct.pack(">4sIII", b"MATH", 0, 44, 4)
                tables += struct.pack(">4sIII", b"OS/2", 0, 48, 10)
                data = header + tables + bytes(4) + bytes(8) + struct.pack(">H", flags)
                if flags in (0, 8, 12):
                    _check_font(data)
                else:
                    with self.assertRaisesRegex(ValueError, "editable outline"):
                        _check_font(data)

    @unittest.skipUnless(
        PANDOC.is_file() and LATIN_MODERN.is_file(), "Requires Pandoc and fonts-lmodern"
    )
    def test_native_equations_use_the_embedded_font_without_losing_styles(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "equations.docx"
            subprocess.run(
                [str(PANDOC), "-f", "latex", "-t", "docx", "-o", str(path)],
                input=r"Text $\alpha+\mathrm{\alpha}+\Delta$.",
                text=True,
                capture_output=True,
                check=True,
            )
            metadata = embed_math_font(path, LATIN_MODERN, family="Latin Modern Math")
            self.assertEqual(validate_omml(path, expected_count=1), 1)
            with zipfile.ZipFile(path) as package:
                original_parts = set(package.namelist())
                embedded = package.read(metadata["part"])
                self.assertEqual(
                    obfuscate_font(embedded, uuid.UUID(metadata["font_key"])),
                    LATIN_MODERN.read_bytes(),
                )
                tree = ET.fromstring(package.read("word/document.xml"))
                for run in tree.iter(f"{{{MATH}}}r"):
                    fonts = run.find(f"{{{WORD}}}rPr/{{{WORD}}}rFonts")
                    self.assertEqual(fonts.get(f"{{{WORD}}}ascii"), "Latin Modern Math")
                # Explicit Roman alpha and uppercase Delta keep Pandoc's style.
                upright = [
                    run.find(f"{{{MATH}}}rPr/{{{MATH}}}sty")
                    for run in tree.iter(f"{{{MATH}}}r")
                    if run.find(f"{{{MATH}}}t").text in {"α", "Δ"}
                ]
                self.assertEqual(
                    sum(
                        style is not None and style.get(f"{{{MATH}}}val") == "p"
                        for style in upright
                    ),
                    2,
                )
                fonts = ET.fromstring(package.read("word/fontTable.xml"))
                entry = next(
                    item
                    for item in fonts
                    if item.get(f"{{{WORD}}}name") == "Latin Modern Math"
                )
                identifier = entry.find(f"{{{WORD}}}embedRegular").get(
                    f"{{{OFFICE_REL}}}id"
                )
                rels = ET.fromstring(package.read("word/_rels/fontTable.xml.rels"))
                self.assertEqual(rels[0].tag, f"{{{REL}}}Relationship")
                self.assertEqual(
                    next(item for item in rels if item.get("Id") == identifier).get(
                        "Target"
                    ),
                    metadata["part"].removeprefix("word/"),
                )
                settings = ET.fromstring(package.read("word/settings.xml"))
                self.assertEqual(
                    settings.find(f"{{{MATH}}}mathPr/{{{MATH}}}mathFont").get(
                        f"{{{MATH}}}val"
                    ),
                    "Latin Modern Math",
                )
            self.assertEqual(
                embed_math_font(path, LATIN_MODERN, family="Latin Modern Math"),
                metadata,
            )
            with zipfile.ZipFile(path) as package:
                self.assertEqual(set(package.namelist()), original_parts)
                self.assertEqual(len(package.namelist()), len(original_parts))


if __name__ == "__main__":
    unittest.main()
