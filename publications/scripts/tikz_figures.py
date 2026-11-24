"""Extract complete TikZ figures independently of their rendering backend."""

from collections.abc import Callable
from dataclasses import dataclass
import re

from tex_syntax import environments, mask_comments, read_argument


@dataclass(frozen=True)
class TikzFigure:
    start: int
    end: int
    body: str
    scene: str
    pictures: tuple[str, ...]
    label: str
    caption: str
    width_fraction: float


@dataclass(frozen=True)
class TikzPanel:
    picture: str
    caption: str
    label: str


def extract_panels(figure: TikzFigure) -> tuple[TikzPanel, ...]:
    panels = []
    for span in environments(figure.body, "subfigure"):
        body = figure.body[span.body_start : span.body_end]
        pictures = environments(body, "tikzpicture")
        captions, labels = _commands(body, "caption"), _commands(body, "label")
        if len(pictures) != 1 or len(captions) != 1 or len(labels) != 1:
            raise ValueError("A panel must contain one picture, caption and label")
        picture = pictures[0]
        panels.append(
            TikzPanel(body[picture.start : picture.end], captions[0][2], labels[0][2])
        )
    return tuple(panels)


def split_standalone_math(picture: str) -> tuple[str, tuple[str, ...]]:
    """Separate anonymous equation annotations for native Word rendering.

    The renderer opts in for panels whose anonymous math nodes are explanatory
    equations. Named nodes, edge labels and every graphical path are retained.
    """
    equations, edits = [], []
    for match in re.finditer(r"\\node\s+at\s*\([^)]*\)\s*\{", mask_comments(picture)):
        text, end = read_argument(picture, match.end() - 1)
        text = text.strip()
        if not (text.startswith("$") and text.endswith("$")):
            continue
        while picture[end].isspace():
            end += 1
        if picture[end] != ";":
            raise ValueError("Unterminated standalone equation node")
        equations.append(text[1:-1].strip())
        edits.append((match.start(), end + 1))
    for start, end in reversed(edits):
        picture = picture[:start] + picture[end:]
    return picture, tuple(equations)


def _commands(body: str, name: str) -> list[tuple[int, int, str]]:
    masked = mask_comments(body)
    for environment in environments(body, "subfigure") + environments(
        body, "tikzpicture"
    ):
        masked = (
            masked[: environment.start]
            + " " * (environment.end - environment.start)
            + masked[environment.end :]
        )
    commands = []
    for match in re.finditer(r"\\" + name + r"(?![A-Za-z])", masked):
        position = match.end()
        while position < len(masked) and masked[position].isspace():
            position += 1
        if name == "caption" and masked[position] == "[":
            _, position = read_argument(body, position, "[")
            while masked[position].isspace():
                position += 1
        value, end = read_argument(body, position)
        commands.append((match.start(), end, value))
    return commands


def extract_figures(source: str) -> list[TikzFigure]:
    figures = []
    spans = environments(source, "figure") + environments(source, "figure*")
    for span in sorted(spans, key=lambda item: item.start):
        body = source[span.body_start : span.body_end]
        body = re.sub(r"^\s*\[[^]]*\]", "", body, count=1)
        pictures = tuple(
            body[item.start : item.end] for item in environments(body, "tikzpicture")
        )
        captions, labels = _commands(body, "caption"), _commands(body, "label")
        if len(captions) != 1 or not labels or not pictures:
            raise ValueError(
                "Each figure needs TikZ pictures, one outer caption and an outer label"
            )
        scene = body
        for start, end, _ in sorted((captions[0], labels[-1]), reverse=True):
            scene = scene[:start] + scene[end:]
        scaled = re.search(r"\\resizebox\{([\d.]+)\\textwidth\}", mask_comments(body))
        fraction = float(scaled[1]) if scaled else 1.0
        if not 0 < fraction <= 1:
            raise ValueError("Figure width must fit the text width")
        figures.append(
            TikzFigure(
                span.start,
                span.end,
                body,
                scene,
                pictures,
                labels[-1][2],
                captions[0][2],
                fraction,
            )
        )
    return figures


def replace_figures(source: str, renderer: Callable[[TikzFigure], str]) -> str:
    replacements = [
        (figure.start, figure.end, renderer(figure))
        for figure in extract_figures(source)
    ]
    for start, end, replacement in reversed(replacements):
        source = source[:start] + replacement + source[end:]
    return source
