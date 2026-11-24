"""Protect source math spacing and Greek styles across Word normalization."""

import unittest
import xml.etree.ElementTree as ET

from omml import MATH, normalize_omml
from omml_typography import XML_SPACE


class EquationTypographyTests(unittest.TestCase):
    def equation(self, runs: str) -> ET.Element:
        return ET.fromstring(f'<m:oMath xmlns:m="{MATH}">{runs}</m:oMath>')

    def test_explicit_spaces_keep_their_width_and_position(self) -> None:
        tree = self.equation(
            "<m:r><m:t>a,</m:t></m:r><m:r><m:t>\u2009</m:t></m:r>"
            "<m:r><m:t>b,</m:t></m:r><m:r><m:t>\u2001</m:t></m:r>"
            "<m:r><m:t>c,</m:t></m:r><m:r><m:t>\u2001\u2001</m:t></m:r>"
            "<m:r><m:t>d</m:t></m:r>"
        )
        normalize_omml(tree)
        self.assertEqual("".join(tree.itertext()), "a,\u2009b,\u2003c,\u2003\u2003d")
        for run in list(tree)[1::2]:
            self.assertEqual(run.find(f"{{{MATH}}}t").get(XML_SPACE), "preserve")
            self.assertIsNotNone(run.find(f"{{{MATH}}}rPr/{{{MATH}}}nor"))
            self.assertIsNone(run.find(f"{{{MATH}}}rPr/{{{MATH}}}sty"))

    def test_greek_variables_are_italic_without_changing_uppercase(self) -> None:
        tree = self.equation(
            "<m:r><m:t>α</m:t></m:r><m:r><m:t>ϵ</m:t></m:r>"
            '<m:r><m:rPr><m:sty m:val="p"/></m:rPr><m:t>Δ</m:t></m:r>'
        )
        normalize_omml(tree)
        styles = [run.find(f"{{{MATH}}}rPr/{{{MATH}}}sty") for run in tree]
        self.assertEqual([s.get(f"{{{MATH}}}val") for s in styles], ["i", "i", "p"])

    def test_explicit_roman_and_bold_greek_are_preserved(self) -> None:
        tree = self.equation(
            '<m:r><m:rPr><m:sty m:val="p"/></m:rPr><m:t>α</m:t></m:r>'
            "<m:r><m:rPr><m:nor/></m:rPr><m:t>β</m:t></m:r>"
            '<m:r><m:rPr><m:sty m:val="b"/></m:rPr><m:t>γ</m:t></m:r>'
        )
        normalize_omml(tree)
        self.assertEqual(tree[0][0][0].get(f"{{{MATH}}}val"), "p")
        self.assertIsNone(tree[1].find(f"{{{MATH}}}rPr/{{{MATH}}}sty"))
        self.assertEqual(tree[2][0][0].get(f"{{{MATH}}}val"), "b")

    def test_normalization_is_idempotent(self) -> None:
        tree = self.equation(
            "<m:r><m:t>η</m:t></m:r><m:r><m:t>\u2001\u2001</m:t></m:r>"
        )
        normalize_omml(tree)
        expected = ET.tostring(tree)
        normalize_omml(tree)
        self.assertEqual(ET.tostring(tree), expected)


if __name__ == "__main__":
    unittest.main()
