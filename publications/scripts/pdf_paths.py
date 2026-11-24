"""Read painted PGF paths, retaining geometry rather than outlining PDF text."""

from copy import deepcopy
from dataclasses import asdict, dataclass, field
from pathlib import Path

from pypdf import PdfReader

Point = tuple[float, float]
Matrix = tuple[float, float, float, float, float, float]
IDENTITY: Matrix = (1, 0, 0, 1, 0, 0)


@dataclass
class Paint:
    matrix: Matrix = IDENTITY
    stroke: str = "000000"
    fill: str = "000000"
    width: float = 0.4
    dash: list[float] = field(default_factory=list)
    cap: int = 0
    join: int = 0
    stroke_alpha: float = 1
    fill_alpha: float = 1


@dataclass
class VectorPath:
    commands: list[tuple[str, list[Point]]]
    stroke: str | None
    fill: str | None
    width: float
    dash: list[float]
    cap: int
    join: int
    stroke_alpha: float
    fill_alpha: float

    @property
    def bounds(self) -> tuple[float, float, float, float]:
        points = [point for _, vertices in self.commands for point in vertices]
        return (
            min(x for x, _ in points),
            min(y for _, y in points),
            max(x for x, _ in points),
            max(y for _, y in points),
        )

    def to_dict(self) -> dict:
        return asdict(self)


def transform(point: Point, matrix: Matrix) -> Point:
    x, y = point
    a, b, c, d, e, f = matrix
    return a * x + c * y + e, b * x + d * y + f


def compose(left: Matrix, right: Matrix) -> Matrix:
    a, b, c, d, e, f = left
    g, h, i, j, k, offset_y = right
    return (
        a * g + c * h,
        b * g + d * h,
        a * i + c * j,
        b * i + d * j,
        a * k + c * offset_y + e,
        b * k + d * offset_y + f,
    )


def color(values: list[float]) -> str:
    return "".join(f"{round(max(0, min(1, value)) * 255):02X}" for value in values)


def read_paths(path: Path) -> tuple[float, float, list[VectorPath]]:
    reader = PdfReader(path)
    if len(reader.pages) != 1:
        raise ValueError("Each TikZ scene must compile to exactly one PDF page")
    page = reader.pages[0]
    state = Paint()
    stack: list[Paint] = []
    commands: list[tuple[str, list[Point]]] = []
    painted: list[VectorPath] = []
    text_operators = {
        b"BT",
        b"ET",
        b"Tf",
        b"Tj",
        b"TJ",
        b"Td",
        b"TD",
        b"Tm",
        b"T*",
        b"Tc",
        b"Tw",
        b"Tz",
        b"TL",
        b"Tr",
        b"Ts",
        b"'",
        b'"',
    }
    for operands, operator in page.get_contents().operations:
        if operator in text_operators:
            continue
        if operator == b"q":
            stack.append(deepcopy(state))
        elif operator == b"Q":
            state = stack.pop()
        elif operator == b"cm":
            state.matrix = compose(state.matrix, tuple(float(x) for x in operands))
        elif operator in (b"m", b"l", b"c"):
            points = [
                transform((float(operands[i]), float(operands[i + 1])), state.matrix)
                for i in range(0, len(operands), 2)
            ]
            commands.append(
                ({b"m": "move", b"l": "line", b"c": "curve"}[operator], points)
            )
        elif operator == b"re":
            x, y, width, height = map(float, operands)
            points = [
                transform(point, state.matrix)
                for point in [
                    (x, y),
                    (x + width, y),
                    (x + width, y + height),
                    (x, y + height),
                ]
            ]
            commands.extend(
                [
                    ("move", points[:1]),
                    *[("line", [p]) for p in points[1:]],
                    ("close", []),
                ]
            )
        elif operator == b"h":
            commands.append(("close", []))
        elif operator in (b"S", b"s", b"f", b"f*", b"B", b"B*", b"b", b"b*"):
            if operator in (b"s", b"b", b"b*"):
                commands.append(("close", []))
            if commands:
                painted.append(
                    VectorPath(
                        commands,
                        None if operator in (b"f", b"f*") else state.stroke,
                        None if operator in (b"S", b"s") else state.fill,
                        state.width,
                        state.dash.copy(),
                        state.cap,
                        state.join,
                        state.stroke_alpha,
                        state.fill_alpha,
                    )
                )
            commands = []
        elif operator == b"n":
            commands = []
        elif operator == b"w":
            state.width = float(operands[0])
        elif operator == b"d":
            state.dash = [float(value) for value in operands[0]]
        elif operator in (b"J", b"j"):
            setattr(state, "cap" if operator == b"J" else "join", int(operands[0]))
        elif operator in (b"RG", b"rg", b"G", b"g"):
            values = [float(value) for value in operands]
            if len(values) == 1:
                values *= 3
            setattr(
                state, "stroke" if operator in (b"RG", b"G") else "fill", color(values)
            )
        elif operator == b"gs":
            settings = page["/Resources"]["/ExtGState"][operands[0]].get_object()
            state.stroke_alpha = float(settings.get("/CA", state.stroke_alpha))
            state.fill_alpha = float(settings.get("/ca", state.fill_alpha))
        elif operator not in (b"M", b"i", b"ri", b"BMC", b"BDC", b"EMC"):
            raise ValueError(
                f"Unsupported PDF drawing operator: {operator!r}; no image fallback"
            )
    if stack:
        raise ValueError("Unbalanced PDF graphics state")
    return float(page.mediabox.width), float(page.mediabox.height), painted
