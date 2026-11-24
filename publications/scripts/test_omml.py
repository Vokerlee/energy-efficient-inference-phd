"""Regression checks for the equation format that survives Word editing."""

import tempfile
import unittest
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

from omml import MATH, WORD, normalize_math_tex, normalize_omml, validate_omml


class NativeEquationTests(unittest.TestCase):
    def package(self, directory: str, *, legacy: bool = False) -> Path:
        path = Path(directory) / "article.docx"
        content = (
            f'<w:document xmlns:w="{WORD}" xmlns:m="{MATH}"><w:body><w:p>'
            "<m:oMath><m:f><m:num><m:r><m:t>a</m:t></m:r></m:num>"
            "<m:den><m:r><m:t>b</m:t></m:r></m:den></m:f></m:oMath>"
            "</w:p></w:body></w:document>"
        )
        with zipfile.ZipFile(path, "w") as package:
            package.writestr("word/document.xml", content)
            if legacy:
                package.writestr("word/embeddings/equation.bin", b"legacy equation")
        return path

    def test_native_fraction_is_retained(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(
                validate_omml(self.package(directory), expected_count=1), 1
            )

    def test_mathtype_fallback_is_rejected_even_with_native_equations(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "OLE/MathType"):
                validate_omml(self.package(directory, legacy=True), expected_count=1)

    def test_missing_inline_expression_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "Expected 2 OMML"):
                validate_omml(self.package(directory), expected_count=2)

    def test_underbrace_stretches_without_losing_its_annotation(self) -> None:
        tree = ET.fromstring(
            f'<m:oMath xmlns:m="{MATH}"><m:limLow><m:e><m:limLow>'
            "<m:e><m:r><m:t>a+b</m:t></m:r></m:e>"
            "<m:lim><m:r><m:t>⏟</m:t></m:r></m:lim></m:limLow></m:e>"
            "<m:lim><m:r><m:t>Δ</m:t></m:r></m:lim></m:limLow></m:oMath>"
        )
        normalize_omml(tree)
        self.assertEqual(len(list(tree.iter(f"{{{MATH}}}groupChr"))), 1)
        self.assertEqual(len(list(tree.iter(f"{{{MATH}}}limLow"))), 1)
        self.assertEqual("".join(tree.itertext()), "a+bΔ")

    def test_alignment_marker_does_not_print_as_ampersand(self) -> None:
        tree = ET.fromstring(
            f'<m:oMath xmlns:m="{MATH}"><m:eqArr><m:e>'
            "<m:r><m:t>x</m:t></m:r><m:r><m:t>&amp;</m:t></m:r>"
            "<m:r><m:t>=y</m:t></m:r></m:e></m:eqArr></m:oMath>"
        )
        normalize_omml(tree)
        self.assertEqual("".join(tree.itertext()), "x=y")
        self.assertEqual(len(list(tree.iter(f"{{{MATH}}}aln"))), 1)

    def test_norms_retain_existing_delimiters_and_receive_native_groups(self) -> None:
        source = r"\|x\|+\left\|y\right\|+\left \|z\right \|"
        expected = r"\left\|x\right\|+\left\|y\right\|+\left \|z\right \|"
        self.assertEqual(normalize_math_tex(source), expected)
        self.assertEqual(normalize_math_tex(expected), expected)

    def test_roman_label_remains_one_word(self) -> None:
        tree = ET.fromstring(
            f'<m:oMath xmlns:m="{MATH}"><m:sSub><m:e><m:r><m:t>R</m:t>'
            "</m:r></m:e><m:sub>"
            + "".join(
                f'<m:r><m:rPr><m:sty m:val="p"/></m:rPr><m:t>{c}</m:t></m:r>'
                for c in "fwd"
            )
            + "</m:sub></m:sSub></m:oMath>"
        )
        normalize_omml(tree)
        subscript = tree.find(f".//{{{MATH}}}sub")
        self.assertEqual(len(list(subscript)), 1)
        self.assertEqual("".join(subscript.itertext()), "fwd")
        self.assertIsNotNone(subscript.find(f".//{{{MATH}}}nor"))
        self.assertIsNone(subscript.find(f".//{{{MATH}}}sty"))


if __name__ == "__main__":
    unittest.main()
