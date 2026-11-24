"""Retain TeX-resolved node bounds and original editable label source."""

import re
from dataclasses import asdict, dataclass
from pathlib import Path

from pdf_paths import read_paths
from tex_syntax import read_argument as argument

PT_TO_PDF = 72 / 72.27


@dataclass
class Label:
    name: str
    tex: str
    options: str
    font_size: float = 12
    bounds: tuple[float, float, float, float] = (0, 0, 0, 0)


def expand_loops(source: str) -> str:
    """Expand the literal coordinate-list foreach used by the hierarchy plot."""
    pattern = re.compile(r"\\foreach\s+((?:\\[A-Za-z]+/?)+)\s+in\s*")
    while match := pattern.search(source):
        values, end = argument(source, match.end())
        start = end
        while source[start].isspace():
            start += 1
        body, end = argument(source, start)
        variables = re.findall(r"\\[A-Za-z]+", match[1])
        expanded = []
        for item in values.split(","):
            parts = [
                part.strip().removeprefix("{").removesuffix("}")
                for part in item.strip().split("/")
            ]
            if len(parts) != len(variables):
                raise ValueError(
                    "Only literal TikZ foreach coordinate lists are supported"
                )
            replacements = dict(zip(variables, parts))
            expanded.append(
                re.sub(
                    r"\\[A-Za-z]+",
                    lambda token: replacements.get(token[0], token[0]),
                    body,
                )
            )
        source = source[: match.start()] + "\n".join(expanded) + source[end:]
    return source


def instrument(source: str) -> tuple[str, list[Label]]:
    source = expand_loops(source)
    labels: list[Label] = []
    edits: list[tuple[int, int, str]] = []
    for match in re.finditer(r"\\node\b|(?<![\\A-Za-z])node\b", source):
        cursor = match.end()
        while source[cursor].isspace():
            cursor += 1
        options = ""
        if source[cursor] == "[":
            options, cursor = argument(source, cursor, "[")
        while source[cursor].isspace():
            cursor += 1
        name = f"docxnode{len(labels) + 1}"
        if source[cursor] == "(":
            name, cursor = argument(source, cursor, "(")
        location_start = cursor
        while source[cursor].isspace():
            cursor += 1
        if source[cursor : cursor + 2] == "at":
            cursor = source.index("(", cursor)
            _, cursor = argument(source, cursor, "(")
        while source[cursor].isspace():
            cursor += 1
        if source[cursor] != "{":
            continue
        text, _ = argument(source, cursor)
        labels.append(Label(name, text, options))
        hook = r"execute at end node={\DocxFont{" + name + "}}"
        header = f"{match[0]}[{options + ', ' if options else ''}{hook}] ({name})"
        header += source[location_start:cursor]
        edits.append((match.start(), cursor, header))
    for start, end, replacement in reversed(edits):
        source = source[:start] + replacement + source[end:]
    measurements = "\n".join(
        r"\DocxCorner{"
        + label.name
        + "}{south west}{SW}"
        + r"\DocxCorner{"
        + label.name
        + "}{north east}{NE}"
        for label in labels
    )
    measurements += (
        r"\DocxCorner{current bounding box}{south west}{BBOXSW}"
        r"\DocxCorner{current bounding box}{north east}{BBOXNE}"
    )
    return source.replace(
        r"\end{tikzpicture}", measurements + r"\end{tikzpicture}"
    ), labels


def measurement_preamble(filename: str) -> str:
    return (
        r"\newwrite\docxout"
        + "\n"
        + r"\immediate\openout\docxout="
        + filename
        + "\n"
        + r"\makeatletter"
        + "\n"
        + r"\def\DocxFont#1{\immediate\write\docxout{FONT #1 \f@size}}"
        + "\n"
        + r"\def\DocxCorner#1#2#3{\pgfpointanchor{#1}{#2}"
        + r"\immediate\write\docxout{#3 #1 \the\pgf@x\space\the\pgf@y}}"
        + "\n"
        + r"\makeatother"
        + "\n"
    )


def read_scene(pdf: Path, labels: list[Label]) -> dict:
    width, height, paths = read_paths(pdf)
    measurements: dict[tuple[str, str], tuple[float, float]] = {}
    sizes: dict[str, float] = {}
    for line in pdf.with_suffix(".nodes").read_text().splitlines():
        parts = line.split()
        if parts[0] == "FONT":
            sizes[parts[1]] = float(parts[2])
        else:
            name = parts[1] if parts[0] in ("SW", "NE") else "bbox"
            measurements[(parts[0], name)] = tuple(
                float(v.removesuffix("pt")) for v in parts[-2:]
            )
    left, bottom = measurements[("BBOXSW", "bbox")]
    right, top = measurements[("BBOXNE", "bbox")]
    if (
        abs((right - left + 8) * PT_TO_PDF - width) > 0.1
        or abs((top - bottom + 8) * PT_TO_PDF - height) > 0.1
    ):
        raise ValueError("TeX node coordinates disagree with the cropped PDF bounds")
    for label in labels:
        x1, y1 = measurements[("SW", label.name)]
        x2, y2 = measurements[("NE", label.name)]
        label.bounds = tuple(
            (value - origin + 4) * PT_TO_PDF
            for value, origin in [(x1, left), (y1, bottom), (x2, left), (y2, bottom)]
        )
        label.font_size = sizes[label.name] * PT_TO_PDF
    return {
        "width": width,
        "height": height,
        "paths": [path.to_dict() for path in paths],
        "labels": [asdict(label) for label in labels],
    }
