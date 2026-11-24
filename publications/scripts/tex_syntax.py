"""Small shared TeX readers; preserve offsets into the original source."""

from dataclasses import dataclass
import re


def escaped(source: str, position: int) -> bool:
    count = 0
    while position > 0 and source[position - 1] == "\\":
        count += 1
        position -= 1
    return bool(count % 2)


def mask_comments(source: str) -> str:
    pieces = []
    for line in source.splitlines(keepends=True):
        for match in re.finditer("%", line):
            if not escaped(line, match.start()):
                end = len(line.rstrip("\r\n"))
                line = line[: match.start()] + " " * (end - match.start()) + line[end:]
                break
        pieces.append(line)
    return "".join(pieces)


def read_argument(source: str, start: int, opening: str = "{") -> tuple[str, int]:
    closing = {"{": "}", "[": "]", "(": ")"}[opening]
    if start >= len(source) or source[start] != opening:
        raise ValueError(f"Expected {opening!r} at offset {start}")
    masked = mask_comments(source)
    depth = 1
    for position in range(start + 1, len(masked)):
        if not escaped(masked, position):
            depth += (masked[position] == opening) - (masked[position] == closing)
            if depth == 0:
                return source[start + 1 : position], position + 1
    raise ValueError(f"Unclosed TeX argument at offset {start}")


@dataclass(frozen=True)
class Environment:
    start: int
    end: int
    body_start: int
    body_end: int


def environments(source: str, name: str) -> list[Environment]:
    pattern = re.compile(r"\\(begin|end)\{" + re.escape(name) + r"\}")
    stack = []
    found = []
    for match in pattern.finditer(mask_comments(source)):
        if match[1] == "begin":
            stack.append((match.start(), match.end()))
        elif not stack:
            raise ValueError(f"Unmatched end of {name}")
        else:
            start, body_start = stack.pop()
            found.append(Environment(start, match.end(), body_start, match.start()))
    if stack:
        raise ValueError(f"Unclosed {name}")
    return sorted(found, key=lambda item: item.start)
