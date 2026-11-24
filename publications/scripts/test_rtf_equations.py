"""Check editable RTF math and reject incomplete or unsupported conversion."""

from pathlib import Path
import tempfile
import unittest
import zipfile

from omml import MATH, WORD
from rtf_equations import escape_rtf, math_group_spans, restore_native_math


class RtfEquationTests(unittest.TestCase):
    def source(self, directory: str, formula: str) -> tuple[Path, Path]:
        folder = Path(directory)
        document = folder / "article.docx"
        with zipfile.ZipFile(document, "w") as package:
            package.writestr(
                "word/document.xml",
                f'<w:document xmlns:w="{WORD}" xmlns:m="{MATH}"><w:body><w:p><m:oMath>{formula}</m:oMath></w:p></w:body></w:document>',
            )
        rtf = folder / "article.rtf"
        rtf.write_bytes(
            rb"{\rtf1{\fonttbl{\f0 Times New Roman;}}before{\mmath{\mmathPict image}}after}"
        )
        return document, rtf

    def test_fraction_replaces_picture_with_native_math(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            document, rtf = self.source(
                directory,
                "<m:f><m:num><m:r><m:t>x</m:t></m:r></m:num><m:den><m:r><m:t>δ</m:t></m:r></m:den></m:f>",
            )
            self.assertEqual(restore_native_math(document, rtf), 1)
            content = rtf.read_bytes()
            self.assertIn(rb"\mf ", content)
            self.assertIn(rb"\mnum ", content)
            self.assertIn(rb"\mden ", content)
            self.assertIn(rb"\u948?", content)
            self.assertNotIn(rb"\mmathPict", content)
            self.assertIn(b"before", content)
            self.assertIn(b"after", content)
            restore_native_math(document, rtf)
            self.assertEqual(rtf.read_bytes(), content)

    def test_alignment_is_a_property_group_not_a_destination_for_the_equal_sign(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            document, rtf = self.source(
                directory,
                "<m:eqArr><m:e><m:r><m:rPr><m:aln/></m:rPr><m:t>=</m:t></m:r></m:e></m:eqArr>",
            )
            restore_native_math(document, rtf)
            self.assertIn(rb"{\maln on}=", rtf.read_bytes())
            self.assertNotIn(rb"\maln1", rtf.read_bytes())

    def test_parser_ignores_escaped_and_binary_braces(self) -> None:
        data = rb"{\rtf1 \{literal\} \bin2 {} {\mmath{\*\moMath x}}}"
        spans = math_group_spans(data)
        self.assertEqual(len(spans), 1)
        self.assertEqual(data[slice(*spans[0])], rb"{\mmath{\*\moMath x}}")

    def test_missing_group_does_not_rewrite_the_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            document, rtf = self.source(directory, "<m:r><m:t>x</m:t></m:r>")
            rtf.write_bytes(rb"{\rtf1 plain text}")
            original = rtf.read_bytes()
            with self.assertRaisesRegex(ValueError, "0 math groups"):
                restore_native_math(document, rtf)
            self.assertEqual(rtf.read_bytes(), original)

    def test_math_only_font_is_added_when_the_layout_export_omits_it(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            document, rtf = self.source(
                directory,
                '<m:r><w:rPr><w:rFonts w:ascii="Cambria Math"/></w:rPr><m:t>f</m:t></m:r>',
            )
            restore_native_math(document, rtf)
            content = rtf.read_bytes()
            self.assertIn(rb"{\f1\fnil\fcharset0 Cambria Math;}", content)
            self.assertIn(rb"\f1 ", content)
            restore_native_math(document, rtf)
            self.assertEqual(rtf.read_bytes(), content)

    def test_unknown_construct_is_rejected_instead_of_becoming_a_picture(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            document, rtf = self.source(directory, "<m:unsupported/>")
            original = rtf.read_bytes()
            with self.assertRaisesRegex(ValueError, "Unsupported OMML"):
                restore_native_math(document, rtf)
            self.assertEqual(rtf.read_bytes(), original)

    def test_unicode_uses_signed_utf16_units(self) -> None:
        self.assertEqual(escape_rtf("δ{\\}"), r"\u948?\{\\\}")
        self.assertEqual(escape_rtf("𝑥").count(r"\u-"), 2)

    def test_number_set_keeps_its_glyph_even_in_readers_ignoring_math_alphabet_flags(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as directory:
            document, rtf = self.source(
                directory,
                '<m:r><m:rPr><m:scr m:val="double-struck"/><m:sty m:val="p"/></m:rPr><m:t>R</m:t></m:r>',
            )
            restore_native_math(document, rtf)
            self.assertIn(rb"\u8477?", rtf.read_bytes())
            self.assertNotIn(rb"\mscr3", rtf.read_bytes())


if __name__ == "__main__":
    unittest.main()
