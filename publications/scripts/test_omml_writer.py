"""Check real LaTeX-to-Word output with the pinned shared Pandoc writer."""

import io
import subprocess
import unittest
import xml.etree.ElementTree as ET
import zipfile

from omml import MATH, normalize_omml
from setup_docx import PANDOC


class PandocEquationTests(unittest.TestCase):
    @unittest.skipUnless(PANDOC.is_file(), "Run make docx-setup to install Pandoc")
    def test_latex_spacing_and_styles_survive_the_real_writer(self) -> None:
        source = r"$\alpha\,\beta\quad\gamma\qquad\delta+\mathrm{\alpha}+\Delta$"
        output = subprocess.run(
            [str(PANDOC), "-f", "latex", "-t", "docx"],
            input=source.encode(),
            capture_output=True,
            check=True,
        )
        with zipfile.ZipFile(io.BytesIO(output.stdout)) as package:
            tree = ET.fromstring(package.read("word/document.xml"))
        normalize_omml(tree)
        runs = list(tree.iter(f"{{{MATH}}}r"))
        spaces = [
            run.find(f"{{{MATH}}}t").text
            for run in runs
            if (run.find(f"{{{MATH}}}t").text or "").isspace()
        ]
        self.assertEqual(spaces, ["\u2009", "\u2003", "\u2003\u2003"])
        alphas = [run for run in runs if run.find(f"{{{MATH}}}t").text == "α"]
        self.assertEqual(len(alphas), 2)
        styles = [run.find(f"{{{MATH}}}rPr/{{{MATH}}}sty") for run in alphas]
        self.assertEqual([style.get(f"{{{MATH}}}val") for style in styles], ["i", "p"])


if __name__ == "__main__":
    unittest.main()
