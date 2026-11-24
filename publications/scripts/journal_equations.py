"""Keep every mathematical expression in Word's native equation editor."""

from copy import deepcopy
import unicodedata
import xml.etree.ElementTree as ET

from omml import MATH, WORD
from word_document import xml_child

M = "{" + MATH + "}"
W = "{" + WORD + "}"


def _inline_sum(operator: ET.Element) -> list[ET.Element] | None:
    """Use explicit side indices where importers ignore nary limit placement."""
    character = operator.find(M + "naryPr/" + M + "chr")
    if character is None or character.get(M + "val") != "∑":
        return None
    indices = []
    for kind in ("sub", "sup"):
        value = operator.find(M + kind)
        hidden = operator.find(M + "naryPr/" + M + kind + "Hide")
        if (
            value is not None
            and len(value)
            and not (
                hidden is not None and hidden.get(M + "val", "1") in {"1", "true", "on"}
            )
        ):
            indices.append((kind, value))
    run = ET.Element(M + "r")
    ET.SubElement(run, M + "t").text = "∑"
    if indices:
        tag = "sSubSup" if len(indices) == 2 else "s" + indices[0][0].title()
        symbol = ET.Element(M + tag)
        ET.SubElement(symbol, M + "e").append(run)
        for _, value in indices:
            symbol.append(deepcopy(value))
    else:
        symbol = run
    expression = operator.find(M + "e")
    return [symbol] + (
        [deepcopy(node) for node in expression] if expression is not None else []
    )


def apply_native_math(
    tree: ET.Element, *, family: str = "Cambria Math", half_points: int = 24
) -> dict:
    """Keep all notation in the equation engine with a single math font.

    Variable styles belong to OMML, rather than ordinary-text italic flags.
    Inline summation limits sit beside the operator, including in exponents.
    Displayed equations retain their source limit placement.
    """
    equations = list(tree.iter(M + "oMath"))
    parents = {child: parent for parent in tree.iter() for child in parent}
    inline_limits = 0
    for equation in equations:
        parent = parents[equation]
        style = parent.find(W + "pPr/" + W + "pStyle")
        display = parent.tag == M + "oMathPara" or (
            style is not None and style.get(W + "val") == "Equation"
        )
        if not display:
            for operator in reversed(list(equation.iter(M + "nary"))):
                compact = _inline_sum(operator)
                if compact is not None:
                    owner = next(
                        node for node in equation.iter() if operator in list(node)
                    )
                    index = list(owner).index(operator)
                    owner.remove(operator)
                    owner[index:index] = compact
                    inline_limits += 1
                    continue
                properties = operator.find(M + "naryPr")
                if properties is None:
                    properties = ET.Element(M + "naryPr")
                    operator.insert(0, properties)
                limit = properties.find(M + "limLoc")
                if limit is None:
                    limit = ET.Element(M + "limLoc")
                    # CT_NaryPr: chr, limLoc, grow, subHide, supHide, ctrlPr.
                    position = 1 if properties.find(M + "chr") is not None else 0
                    properties.insert(position, limit)
                limit.set(M + "val", "subSup")
                inline_limits += 1
        for run in equation.iter(M + "r"):
            text = "".join(node.text or "" for node in run.findall(M + "t"))
            properties = run.find(M + "rPr")
            if properties is None:
                properties = ET.Element(M + "rPr")
                run.insert(0, properties)
            if (
                text
                and all(
                    unicodedata.name(char, "").startswith("GREEK ") for char in text
                )
                and properties.find(M + "nor") is None
            ):
                style = properties.find(M + "sty")
                if style is None:
                    style = ET.Element(M + "sty")
                    position = next(
                        (
                            i
                            for i, node in enumerate(properties)
                            if node.tag in {M + "brk", M + "aln"}
                        ),
                        len(properties),
                    )
                    properties.insert(position, style)
                style.set(
                    M + "val", "b" if style.get(M + "val") in {"b", "bi"} else "p"
                )
            word = run.find(W + "rPr")
            if word is None:
                word = ET.Element(W + "rPr")
                position = next(
                    (i for i, node in enumerate(run) if node.tag == M + "t"), len(run)
                )
                run.insert(position, word)
            fonts = xml_child(
                word, "rFonts", ascii=family, hAnsi=family, cs=family, eastAsia=family
            )
            for key in list(fonts.attrib):
                if key.endswith("Theme"):
                    del fonts.attrib[key]
            for name in ("i", "iCs", "b", "bCs", "position", "vertAlign"):
                for node in word.findall(W + name):
                    word.remove(node)
            xml_child(word, "sz", val=half_points)
            xml_child(word, "szCs", val=half_points)
    return {
        "source_math": len(equations),
        "simple_text_math": 0,
        "native_equations": len(equations),
        "converted": [],
        "inline_side_limits": inline_limits,
        "family": family,
    }
