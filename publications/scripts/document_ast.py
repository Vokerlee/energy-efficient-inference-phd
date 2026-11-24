"""Shared Pandoc traversal in structural and visible reading order."""

from collections.abc import Iterator
from typing import Any


def walk_nodes(value: Any) -> Iterator[dict[str, Any]]:
    if isinstance(value, dict):
        if "t" in value:
            yield value
        for child in value.values():
            yield from walk_nodes(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_nodes(child)


def expand_grouped_figures(document: dict[str, Any]) -> dict[str, Any]:
    """Keep panel images, displayed math and captions in vertical Word flow.

    Pandoc's compound-figure writer otherwise makes a layout table. Separate
    blocks avoid shrinking panels or treating captions as table data.
    """
    blocks = []
    for block in document["blocks"]:
        if (
            block["t"] != "Figure"
            or sum(node["t"] == "Image" for node in walk_nodes(block["c"][2])) < 2
        ):
            blocks.append(block)
            continue
        content = []
        for item in block["c"][2]:
            if item["t"] not in {"Para", "Plain"}:
                content.append(item)
                continue
            pending = []
            for inline in item["c"]:
                if inline["t"] == "Math" and inline["c"][0]["t"] == "DisplayMath":
                    if pending:
                        content.append({"t": "Para", "c": pending})
                        pending = []
                    content.append({"t": "Para", "c": [inline]})
                else:
                    pending.append(inline)
            if pending:
                content.append({"t": "Para", "c": pending})
        for caption in block["c"][1][1]:
            content.append(
                {
                    "t": "Div",
                    "c": [["", [], [["custom-style", "Image Caption"]]], [caption]],
                }
            )
        blocks.append({"t": "Div", "c": [block["c"][0], content]})
    document["blocks"] = blocks
    return document


def visible_nodes(value: Any) -> Iterator[dict[str, Any]]:
    """Ignore image alt text and place figure captions after their panels."""
    if isinstance(value, dict):
        kind = value.get("t")
        if kind == "Image":
            return
        if kind == "Figure":
            yield from visible_nodes(value["c"][2])
            yield from visible_nodes(value["c"][1][1])
            return
        if kind is not None:
            yield value
        for child in value.values():
            yield from visible_nodes(child)
    elif isinstance(value, list):
        for child in value:
            yield from visible_nodes(child)
