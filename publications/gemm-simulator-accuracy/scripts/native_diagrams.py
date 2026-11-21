"""Build editable Word canvases from PGF paths and semantic TeX labels."""

import copy
import hashlib
import json
import xml.etree.ElementTree as ET
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from latex_source import BUILD, run_command
from setup_docx import PANDOC
from word_document import (
    MATH_FONT,
    order_properties,
    prepare_document_ast,
    rewrite_docx,
    walk_nodes,
)

NAMESPACES = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "wps": "http://schemas.microsoft.com/office/word/2010/wordprocessingShape",
    "wpc": "http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas",
    "m": "http://schemas.openxmlformats.org/officeDocument/2006/math",
}
for prefix, namespace in NAMESPACES.items():
    ET.register_namespace(prefix, namespace)


def tag(name: str) -> str:
    prefix, local = name.split(":")
    return "{" + NAMESPACES[prefix] + "}" + local


def append(
    parent: ET.Element, qualified_name: str, **attributes: str | int
) -> ET.Element:
    return ET.SubElement(
        parent,
        tag(qualified_name),
        {
            tag(key) if ":" in key else key: str(value)
            for key, value in attributes.items()
        },
    )


@dataclass
class LabelContent:
    paragraphs: list[ET.Element]
    text: str
    math_count: int


def editable_labels(scenes: list[dict[str, Any]]) -> dict[str, LabelContent]:
    source = [r"\newcommand{\Vec}[1]{\mathbf{#1}}"]
    names = []
    for index, scene in enumerate(scenes):
        for label in scene["labels"]:
            if not label["tex"].strip():
                continue
            name = f"NATIVELABEL{index}X{label['name']}"
            label["content_key"] = name
            names.append(name)
            source.extend([r"\section*{" + name + "}", label["tex"], "\n"])
    document = json.loads(
        run_command([PANDOC, "-f", "latex", "-t", "json"], data="\n".join(source))
    )
    document = prepare_document_ast(document, {})
    path = BUILD / "diagram-labels.docx"
    run_command(
        [PANDOC, "-f", "json", "-t", "docx", "-o", path], data=json.dumps(document)
    )
    with zipfile.ZipFile(path) as package:
        body = ET.fromstring(package.read("word/document.xml")).find(
            "w:body", NAMESPACES
        )
    collected: dict[str, list[ET.Element]] = {}
    current = None
    for block in body:
        text = "".join(n.text or "" for n in block.iter(tag("w:t")))
        if text in names:
            current = text
            collected[current] = []
        elif current is not None and block.tag == tag("w:p"):
            collected[current].append(copy.deepcopy(block))
        elif block.tag != tag("w:sectPr"):
            raise ValueError("A diagram label produced an unsupported Word block")
    result = {}
    for name in names:
        paragraphs = collected[name]
        result[name] = LabelContent(
            paragraphs,
            "".join(
                n.text or ""
                for p in paragraphs
                for n in p.iter()
                if n.tag in (tag("w:t"), tag("m:t"))
            ),
            sum(len(list(p.iter(tag("m:oMath")))) for p in paragraphs),
        )
    expected_math = sum(node["t"] == "Math" for node in walk_nodes(document))
    if sum(content.math_count for content in result.values()) != expected_math:
        raise ValueError("Diagram mathematics was not converted to editable OMML")
    return result


def solid_fill(parent: ET.Element, value: str | None, alpha: float = 1) -> None:
    if value is None:
        append(parent, "a:noFill")
        return
    color = append(append(parent, "a:solidFill"), "a:srgbClr", val=value)
    if alpha < 1:
        append(color, "a:alpha", val=round(alpha * 100000))


def shape_properties(
    parent: ET.Element, bounds: tuple[int, int, int, int]
) -> ET.Element:
    left, top, right, bottom = bounds
    properties = append(parent, "wps:spPr")
    transform = append(properties, "a:xfrm")
    append(transform, "a:off", x=left, y=top)
    append(transform, "a:ext", cx=max(1, right - left), cy=max(1, bottom - top))
    return properties


def outline(properties: ET.Element, path: dict[str, Any], scale: float) -> None:
    line = append(
        properties,
        "a:ln",
        w=max(1, round(path["width"] * scale)),
        cap=["flat", "rnd", "sq"][path["cap"]],
    )
    solid_fill(line, path["stroke"], path["stroke_alpha"])
    if path["dash"]:
        pattern = append(line, "a:custDash")
        lengths = path["dash"]
        if len(lengths) % 2:
            lengths *= 2
        for index in range(0, len(lengths), 2):
            append(
                pattern,
                "a:ds",
                d=round(100000 * lengths[index] / path["width"]),
                sp=round(100000 * lengths[index + 1] / path["width"]),
            )
    append(line, ["a:miter", "a:round", "a:bevel"][path["join"]])


def label_paragraphs(content: LabelContent, size: int) -> list[ET.Element]:
    paragraphs = copy.deepcopy(content.paragraphs)
    for paragraph in paragraphs:
        properties = paragraph.find("w:pPr", NAMESPACES)
        if properties is not None:
            paragraph.remove(properties)
        properties = ET.Element(tag("w:pPr"))
        paragraph.insert(0, properties)
        append(
            properties,
            "w:spacing",
            **{
                "w:before": 0,
                "w:after": 0,
                "w:line": 240,
                "w:lineRule": "auto",
            },
        )
        append(properties, "w:jc", **{"w:val": "center"})
        append(properties, "w:ind", **{"w:left": 0, "w:right": 0, "w:firstLine": 0})
        mark = append(properties, "w:rPr")
        append(mark, "w:sz", **{"w:val": size})
        append(mark, "w:szCs", **{"w:val": size})
        for run in paragraph.iter():
            if run.tag not in (tag("w:r"), tag("m:r")):
                continue
            properties = run.find("w:rPr", NAMESPACES)
            if properties is None:
                properties = ET.Element(tag("w:rPr"))
                index = 1 if len(run) and run[0].tag == tag("m:rPr") else 0
                run.insert(index, properties)
            for child in list(properties):
                if child.tag not in (tag("w:b"), tag("w:i")):
                    properties.remove(child)
            font = MATH_FONT if run.tag == tag("m:r") else "Times New Roman"
            append(properties, "w:rFonts", **{"w:ascii": font, "w:hAnsi": font})
            append(properties, "w:sz", **{"w:val": size})
            append(properties, "w:szCs", **{"w:val": size})
    return paragraphs


def text_body(shape: ET.Element, content: LabelContent | None, size: int) -> None:
    if content is not None:
        body = append(append(shape, "wps:txbx"), "w:txbxContent")
        body.extend(label_paragraphs(content, size))
    properties = append(
        shape,
        "wps:bodyPr",
        wrap="square",
        lIns=0,
        tIns=0,
        rIns=0,
        bIns=0,
        anchor="ctr",
        anchorCtr=0,
    )
    append(append(properties, "a:prstTxWarp", prst="textNoShape"), "a:avLst")
    append(properties, "a:noAutofit")


def draw_scene(
    scene: dict[str, Any], content: dict[str, LabelContent], width: int, identifier: int
) -> tuple[ET.Element, dict[str, Any]]:
    scale = width / scene["width"]
    height = round(scene["height"] * scale)
    drawing = ET.Element(tag("w:drawing"))
    inline = append(drawing, "wp:inline", distT=0, distB=0, distL=0, distR=0)
    append(inline, "wp:extent", cx=width, cy=height)
    append(inline, "wp:effectExtent", l=0, t=0, r=0, b=0)
    append(inline, "wp:docPr", id=identifier, name=f"Native TikZ figure {identifier}")
    append(
        append(inline, "wp:cNvGraphicFramePr"), "a:graphicFrameLocks", noChangeAspect=1
    )
    data = append(append(inline, "a:graphic"), "a:graphicData", uri=NAMESPACES["wpc"])
    canvas = append(data, "wpc:wpc")
    solid_fill(append(canvas, "wpc:bg"), "FFFFFF")
    append(canvas, "wpc:whole")
    unused_labels = scene["labels"].copy()
    identifiers = iter(range(identifier * 1000, identifier * 1000 + 999))

    def point(pair: list[float]) -> tuple[int, int]:
        return round(pair[0] * scale), round((scene["height"] - pair[1]) * scale)

    def attach_label(shape: ET.Element, label: dict[str, Any] | None) -> None:
        value = (
            content[label["content_key"]]
            if label and label.get("content_key")
            else None
        )
        size = max(4, round(2 * label["font_size"] * scale / 12700)) if label else 12
        text_body(shape, value, size)

    for index, path in enumerate(scene["paths"]):
        vertices = [p for _, points in path["commands"] for p in points]
        bounds = (
            min(p[0] for p in vertices),
            min(p[1] for p in vertices),
            max(p[0] for p in vertices),
            max(p[1] for p in vertices),
        )
        label = next(
            (
                candidate
                for candidate in unused_labels
                if max(abs(a - b) for a, b in zip(bounds, candidate["bounds"])) < 0.7
            ),
            None,
        )
        if label:
            unused_labels.remove(label)
        x1, y1 = point([bounds[0], bounds[3]])
        x2, y2 = point([bounds[2], bounds[1]])
        shape = append(canvas, "wps:wsp")
        append(
            shape,
            "wps:cNvPr",
            id=next(identifiers),
            name=label["name"] if label else f"Path {index + 1}",
        )
        append(shape, "wps:cNvSpPr")
        properties = shape_properties(shape, (x1, y1, x2, y2))
        geometry = append(properties, "a:custGeom")
        for name in ("a:avLst", "a:gdLst", "a:ahLst", "a:cxnLst"):
            append(geometry, name)
        append(geometry, "a:rect", l=0, t=0, r="r", b="b")
        custom = append(
            append(geometry, "a:pathLst"),
            "a:path",
            w=max(1, x2 - x1),
            h=max(1, y2 - y1),
            fill="norm" if path["fill"] else "none",
            stroke=int(path["stroke"] is not None),
        )
        for verb, points in path["commands"]:
            command = append(
                custom,
                {
                    "move": "a:moveTo",
                    "line": "a:lnTo",
                    "curve": "a:cubicBezTo",
                    "close": "a:close",
                }[verb],
            )
            for vertex in points:
                x, y = point(vertex)
                append(command, "a:pt", x=x - x1, y=y - y1)
        solid_fill(properties, path["fill"], path["fill_alpha"])
        outline(properties, path, scale)
        attach_label(shape, label)
    for label in unused_labels:
        if not label["tex"].strip():
            continue
        left, bottom, right, top = label["bounds"]
        x1, y1 = point([left, top])
        x2, y2 = point([right, bottom])
        shape = append(canvas, "wps:wsp")
        append(shape, "wps:cNvPr", id=next(identifiers), name=label["name"])
        append(shape, "wps:cNvSpPr", txBox=1)
        properties = shape_properties(shape, (x1, y1, x2, y2))
        append(append(properties, "a:prstGeom", prst="rect"), "a:avLst")
        solid_fill(properties, None)
        solid_fill(append(properties, "a:ln"), None)
        attach_label(shape, label)
    order_properties(drawing)
    expected_labels = {
        label["name"]: content[label["content_key"]].text
        for label in scene["labels"]
        if label.get("content_key")
    }
    return drawing, {
        "sha256": drawing_digest(drawing),
        "shape_count": len(canvas.findall("wps:wsp", NAMESPACES)),
        "labels": expected_labels,
        "math_count": sum(
            content[label["content_key"]].math_count
            for label in scene["labels"]
            if label.get("content_key")
        ),
    }


def drawing_digest(drawing: ET.Element) -> str:
    canonical = ET.canonicalize(
        ET.tostring(drawing, encoding="unicode"), rewrite_prefixes=True
    )
    return hashlib.sha256(canonical.encode()).hexdigest()


def replace_images(path: Path, figures: list[dict[str, Any]]) -> None:
    scenes = [
        json.loads((BUILD / figure["scene_file"]).read_text()) for figure in figures
    ]
    labels = editable_labels(scenes)

    def replace(document: ET.Element) -> None:
        drawings = [
            node
            for node in document.iter(tag("w:drawing"))
            if node.find(".//a:blip", NAMESPACES) is not None
        ]
        if len(drawings) != len(figures):
            raise ValueError(
                "The number of staged figures differs from the native scenes"
            )
        parents = {child: parent for parent in document.iter() for child in parent}
        for index, (drawing, scene, figure) in enumerate(
            zip(drawings, scenes, figures), 1
        ):
            extent = drawing.find("wp:inline/wp:extent", NAMESPACES)
            replacement, metadata = draw_scene(
                scene, labels, int(extent.get("cx")), index
            )
            figure["native"] = metadata
            parent = parents[drawing]
            position = list(parent).index(drawing)
            parent.remove(drawing)
            parent.insert(position, replacement)

    rewrite_docx(path, {"word/document.xml": replace})
    with zipfile.ZipFile(path) as package:
        members = {
            item.filename: package.read(item.filename) for item in package.infolist()
        }
    relationships = ET.fromstring(members["word/_rels/document.xml.rels"])
    for relationship in list(relationships):
        if relationship.get("Type", "").endswith("/image"):
            relationships.remove(relationship)
    ET.register_namespace(
        "", "http://schemas.openxmlformats.org/package/2006/relationships"
    )
    members["word/_rels/document.xml.rels"] = ET.tostring(
        relationships, encoding="utf-8", xml_declaration=True
    )
    content_types = ET.fromstring(members["[Content_Types].xml"])
    for content_type in list(content_types):
        if content_type.get("PartName", "").startswith("/word/media/"):
            content_types.remove(content_type)
    ET.register_namespace(
        "", "http://schemas.openxmlformats.org/package/2006/content-types"
    )
    members["[Content_Types].xml"] = ET.tostring(
        content_types, encoding="utf-8", xml_declaration=True
    )
    temporary = path.with_suffix(".native.docx")
    with zipfile.ZipFile(temporary, "w", zipfile.ZIP_DEFLATED) as package:
        for name, data in members.items():
            if not name.startswith("word/media/"):
                package.writestr(name, data)
    temporary.replace(path)
