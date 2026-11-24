"""Regression checks for geometry extraction and the actual native DOCX export."""

import copy
import json
import tempfile
import unittest
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

from check_docx import check_diagrams
from latex_source import BUILD
from native_diagrams import NAMESPACES, drawing_digest, tag
from pdf_paths import compose, transform
from setup_docx import ARTICLE
from tikz_scene import instrument


class TikzGeometryTests(unittest.TestCase):
    def test_nested_translation_and_scale(self) -> None:
        matrix = compose((2, 0, 0, 2, 10, 20), (1, 0, 0, 1, 3, 4))
        self.assertEqual(transform((5, 6), matrix), (26, 40))

    def test_named_anonymous_and_loop_labels(self) -> None:
        source = r"""\begin{tikzpicture}
        \node[draw] (box) at (0,0) {$x_{i}$};
        \draw (box) -- (1,0) node[right] {output};
        \foreach \x/\value in {0/{-2},1/{-1}} {
            \node[below] at (\x,0) {$10^{\value}$};
        }
        \end{tikzpicture}"""
        instrumented, labels = instrument(source)
        self.assertEqual(
            [label.tex for label in labels],
            [r"$x_{i}$", "output", r"$10^{-2}$", r"$10^{-1}$"],
        )
        self.assertEqual(len({label.name for label in labels}), 4)
        self.assertEqual(instrumented.count(r"execute at end node"), 4)
        self.assertNotIn(r"\foreach", instrumented)


class NativeExportTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        path = ARTICLE.parent / "gemm-simulator-accuracy.docx"
        if not path.is_file() or not (BUILD / "manifest.json").is_file():
            raise RuntimeError("Build the article with make docx before running tests")
        cls.manifest = json.loads((BUILD / "manifest.json").read_text())
        with zipfile.ZipFile(path) as package:
            cls.document = ET.fromstring(package.read("word/document.xml"))
            cls.members = package.namelist()

    def test_all_figures_are_editable_without_image_parts(self) -> None:
        counts = check_diagrams(self.document, self.manifest)
        self.assertEqual(counts["figures"], len(self.manifest["figures"]))
        self.assertGreater(counts["diagram_math"], 0)
        self.assertFalse(any(name.startswith("word/media/") for name in self.members))

    def test_lost_shape_is_rejected(self) -> None:
        document = copy.deepcopy(self.document)
        canvas = document.find(".//wpc:wpc", NAMESPACES)
        canvas.remove(canvas.find("wps:wsp", NAMESPACES))
        with self.assertRaisesRegex(ValueError, "shape was lost"):
            check_diagrams(document, self.manifest)

    def test_changed_label_is_rejected(self) -> None:
        document = copy.deepcopy(self.document)
        text = document.find(".//wps:txbx//m:t", NAMESPACES)
        text.text = "CORRUPTED"
        with self.assertRaisesRegex(ValueError, "label changed"):
            check_diagrams(document, self.manifest)

    def test_changed_geometry_is_rejected(self) -> None:
        document = copy.deepcopy(self.document)
        point = document.find(".//a:path/a:moveTo/a:pt", NAMESPACES)
        point.set("x", str(int(point.get("x")) + 1000))
        with self.assertRaisesRegex(ValueError, "geometry, text or formatting"):
            check_diagrams(document, self.manifest)

    def test_raster_fallback_is_rejected(self) -> None:
        document = copy.deepcopy(self.document)
        ET.SubElement(document.find(".//w:drawing", NAMESPACES), tag("a:blip"))
        with self.assertRaisesRegex(ValueError, "exported as a picture"):
            check_diagrams(document, self.manifest)

    def test_digest_survives_namespace_and_zip_roundtrip(self) -> None:
        drawing = self.document.find(".//w:drawing", NAMESPACES)
        expected = drawing_digest(drawing)
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "roundtrip.zip"
            with zipfile.ZipFile(path, "w") as archive:
                archive.writestr("drawing.xml", ET.tostring(drawing))
            with zipfile.ZipFile(path) as archive:
                restored = ET.fromstring(archive.read("drawing.xml"))
            self.assertEqual(drawing_digest(restored), expected)


if __name__ == "__main__":
    unittest.main()
