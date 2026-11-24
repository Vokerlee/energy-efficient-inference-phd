"""OOXML property ordering regression discovered by Microsoft schema checks."""

import unittest
import xml.etree.ElementTree as ET

from word_document import W, order_properties


class TableOrderingTests(unittest.TestCase):
    def test_new_row_properties_precede_cells_without_reordering_them(self) -> None:
        row = ET.fromstring(
            f'<w:tr xmlns:w="{W}"><w:tc/><w:tc/><w:trPr><w:cantSplit/></w:trPr></w:tr>'
        )
        cells = list(row)[:2]
        order_properties(row)
        self.assertEqual(row[0].tag, "{" + W + "}trPr")
        self.assertEqual(list(row)[1:], cells)


if __name__ == "__main__":
    unittest.main()
