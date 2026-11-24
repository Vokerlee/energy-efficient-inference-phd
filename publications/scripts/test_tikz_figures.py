"""Regression checks for grouped figures, native captions and math extraction."""

import unittest

from tex_syntax import mask_comments, read_argument
from tikz_figures import (
    extract_figures,
    extract_panels,
    replace_figures,
    split_standalone_math,
)


class TikzExtractionTests(unittest.TestCase):
    def test_group_retains_all_panels_and_outer_caption_before_them(self) -> None:
        source = r"\begin{figure}\caption{Outer {caption}}\label{fig:main}"
        for index in range(3):
            source += (
                r"\begin{subfigure}{\linewidth}\begin{tikzpicture}"
                + r"\node (x) {$x$};\end{tikzpicture}\caption{Panel "
                + str(index)
                + r"}\label{panel:"
                + str(index)
                + r"}\end{subfigure}"
            )
        source += r"\end{figure}"
        (figure,) = extract_figures(source)
        self.assertEqual(figure.label, "fig:main")
        self.assertEqual(figure.caption, "Outer {caption}")
        self.assertEqual(len(figure.pictures), 3)
        self.assertEqual(
            [panel.caption for panel in extract_panels(figure)],
            ["Panel 0", "Panel 1", "Panel 2"],
        )
        self.assertNotIn(r"\caption{Outer", figure.scene)

    def test_comments_do_not_create_fake_figures_or_captions(self) -> None:
        source = "% \\begin{figure}fake\n" + r"\begin{figure}\begin{tikzpicture}"
        source += "\n% \\caption{wrong}\\label{wrong}\n"
        source += (
            r"\node {$x$};\end{tikzpicture}\caption{Right}\label{right}\end{figure}"
        )
        (figure,) = extract_figures(source)
        self.assertEqual(figure.caption, "Right")
        self.assertEqual(figure.label, "right")

    def test_equation_is_extracted_but_named_nodes_and_paths_are_preserved(
        self,
    ) -> None:
        source = (
            r"\begin{tikzpicture}\node (x) at (0,0) {$x$};"
            r"\draw (x) -- (1,0);\node at (2,-2.8) {$x=y+z$};\end{tikzpicture}"
        )
        picture, equations = split_standalone_math(source)
        self.assertEqual(equations, ("x=y+z",))
        self.assertIn(r"\node (x)", picture)
        self.assertIn(r"\draw (x)", picture)
        self.assertNotIn("x=y+z", picture)

    def test_replacement_preserves_surrounding_text(self) -> None:
        source = r"before\begin{figure}\begin{tikzpicture}x\end{tikzpicture}\caption{C}\label{f}\end{figure}after"
        self.assertEqual(
            replace_figures(source, lambda figure: figure.label), "beforefafter"
        )

    def test_escaped_braces_and_commented_braces_do_not_end_argument(self) -> None:
        source = "{a \\{b\\} % } ignored\n c} tail"
        value, end = read_argument(source, 0)
        self.assertIn("c", value)
        self.assertEqual(source[end:], " tail")
        self.assertEqual(len(mask_comments(source)), len(source))


if __name__ == "__main__":
    unittest.main()
