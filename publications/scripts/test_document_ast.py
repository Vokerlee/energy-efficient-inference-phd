"""Keep grouped panels, captions and mathematics in Word reading order."""

import unittest

from document_ast import expand_grouped_figures, visible_nodes, walk_nodes


class GroupedFigureTests(unittest.TestCase):
    def test_panels_are_vertical_and_displayed_math_has_its_own_block(self) -> None:
        image = {
            "t": "Image",
            "c": [["", [], []], [{"t": "Str", "c": "hidden alt"}], ["panel.png", ""]],
        }
        math = {"t": "Math", "c": [{"t": "DisplayMath"}, "x=y"]}
        figure = {
            "t": "Figure",
            "c": [
                ["fig:group", [], []],
                [None, [{"t": "Para", "c": [{"t": "Str", "c": "Caption"}]}]],
                [{"t": "Para", "c": [image, math]}, {"t": "Para", "c": [image]}],
            ],
        }
        document = expand_grouped_figures({"blocks": [figure]})
        self.assertEqual(document["blocks"][0]["t"], "Div")
        body = document["blocks"][0]["c"][1]
        self.assertEqual(
            [block["t"] for block in body], ["Para", "Para", "Para", "Div"]
        )
        self.assertEqual(body[1]["c"], [math])
        self.assertEqual(sum(node["t"] == "Image" for node in walk_nodes(document)), 2)
        words = [node["c"] for node in visible_nodes(document) if node["t"] == "Str"]
        self.assertEqual(words, ["Caption"])


if __name__ == "__main__":
    unittest.main()
