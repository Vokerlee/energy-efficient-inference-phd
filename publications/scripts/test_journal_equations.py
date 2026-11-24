"""Protect mathematical meaning while applying an opt-in journal profile."""

import unittest
import xml.etree.ElementTree as ET

from journal_equations import M, W, apply_native_math
from math_alphabets import equation_text


class JournalEquationTests(unittest.TestCase):
    def document(self, math: str) -> ET.Element:
        return ET.fromstring(
            f'<w:document xmlns:w="{W[1:-1]}" xmlns:m="{M[1:-1]}">'
            f"<w:body><w:p><m:oMath>{math}</m:oMath></w:p></w:body></w:document>"
        )

    def test_native_profile_keeps_simple_notation_in_the_equation_editor(self) -> None:
        tree = self.document(
            '<m:sSup><m:e><m:r><m:rPr><m:scr m:val="double-struck"/></m:rPr>'
            "<m:t>R</m:t></m:r></m:e><m:sup><m:r><m:t>n</m:t></m:r></m:sup></m:sSup>"
        )
        report = apply_native_math(tree)
        self.assertEqual(report["native_equations"], 1)
        self.assertEqual(report["simple_text_math"], 0)
        self.assertIsNotNone(tree.find(".//" + M + "sSup"))
        self.assertFalse(list(tree.iter(W + "t")))

    def test_native_variables_use_math_styles_and_one_math_font(self) -> None:
        tree = self.document(
            '<m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>f</m:t></m:r>'
            '<m:r><m:rPr><m:sty m:val="i"/></m:rPr>'
            '<w:rPr><w:i/><w:position w:val="6"/></w:rPr><m:t>γ</m:t></m:r>'
        )
        apply_native_math(tree)
        runs = list(tree.iter(M + "r"))
        self.assertEqual(
            [r.find(M + "rPr/" + M + "sty").get(M + "val") for r in runs], ["i", "p"]
        )
        for run in runs:
            self.assertIsNone(run.find(M + "rPr/" + M + "nor"))
            self.assertIsNone(run.find(W + "rPr/" + W + "position"))
            self.assertIsNone(run.find(W + "rPr/" + W + "i"))
            self.assertEqual(
                run.find(W + "rPr/" + W + "rFonts").get(W + "ascii"), "Cambria Math"
            )
        expected = ET.tostring(tree)
        apply_native_math(tree)
        self.assertEqual(ET.tostring(tree), expected)

    def test_inline_limits_are_compact_while_display_limits_are_preserved(self) -> None:
        math = '<m:nary><m:naryPr><m:chr m:val="∑"/><m:limLoc m:val="undOvr"/></m:naryPr><m:sub><m:r><m:t>j</m:t></m:r></m:sub><m:sup/><m:e><m:r><m:t>n</m:t></m:r></m:e></m:nary>'
        for display in (False, True):
            with self.subTest(display=display):
                tree = self.document(math)
                if display:
                    paragraph = tree.find(".//" + W + "p")
                    properties = ET.Element(W + "pPr")
                    ET.SubElement(properties, W + "pStyle", {W + "val": "Equation"})
                    paragraph.insert(0, properties)
                expected = equation_text(tree)
                apply_native_math(tree)
                self.assertEqual(equation_text(tree), expected)
                if display:
                    self.assertEqual(
                        tree.find(".//" + M + "limLoc").get(M + "val"), "undOvr"
                    )
                else:
                    self.assertIsNone(tree.find(".//" + M + "nary"))
                    self.assertIsNotNone(tree.find(".//" + M + "sSub"))
                    self.assertIn("∑", equation_text(tree))

    def test_nested_inline_sums_and_hidden_placeholders_keep_their_content(
        self,
    ) -> None:
        inner = '<m:nary><m:naryPr><m:chr m:val="∑"/></m:naryPr><m:sub><m:r><m:t>j</m:t></m:r></m:sub><m:sup/><m:e><m:r><m:t>x</m:t></m:r></m:e></m:nary>'
        tree = self.document(
            '<m:nary><m:naryPr><m:chr m:val="∑"/><m:supHide m:val="1"/></m:naryPr>'
            "<m:sub><m:r><m:t>i</m:t></m:r></m:sub><m:sup><m:r><m:t>\u200b</m:t></m:r></m:sup><m:e>"
            + inner
            + "</m:e></m:nary>"
        )
        expected = equation_text(tree).replace("\u200b", "")
        report = apply_native_math(tree)
        self.assertEqual(report["inline_side_limits"], 2)
        self.assertEqual(equation_text(tree), expected)
        self.assertIsNone(tree.find(".//" + M + "nary"))


if __name__ == "__main__":
    unittest.main()
