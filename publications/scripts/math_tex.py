"""Normalize mathematical LaTeX before the shared Pandoc OMML backend."""

import re


def normalize_math_tex(source: str) -> str:
    """Make paired norm bars delimiter structures, rather than text glyphs."""
    if re.search(r"\\(?:big|Big|bigl|bigr|Bigl|Bigr)\\\|", source):
        return source
    bars = re.compile(r"(\\(?:left|right)\s*)?\\\|")
    if sum(match[1] is None for match in bars.finditer(source)) % 2:
        raise ValueError("Unpaired norm delimiters in LaTeX math")
    opening = True

    def delimiter(match: re.Match[str]) -> str:
        nonlocal opening
        if match[1] is not None:
            return match[0]
        value = (r"\left" if opening else r"\right") + match[0]
        opening = not opening
        return value

    return bars.sub(delimiter, source)
