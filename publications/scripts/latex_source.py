"""Prepare the article for Word without changing its LaTeX sources."""

import hashlib
import json
import re
from collections.abc import Sequence
from pathlib import Path
from typing import Any

from setup_docx import ARTICLE
from tool_process import run_tool
from tikz_scene import instrument, measurement_preamble, read_scene
from tikz_figures import TikzFigure, replace_figures

BUILD = ARTICLE / "build" / "docx"


def run_command(
    arguments: Sequence[str | Path],
    *,
    data: str | None = None,
    log: Path | None = None,
    allow_diagnostics: bool = False,
) -> str:
    return run_tool(
        arguments, cwd=ARTICLE, data=data, log=log, allow_diagnostics=allow_diagnostics
    )


def uncomment(source: str) -> str:
    return re.sub(r"(?<!\\)%[^\n]*", "", source)


def expand_inputs(source: str, stack: tuple[Path, ...] = ()) -> str:
    def expand(match: re.Match[str]) -> str:
        path = (ARTICLE / match[1]).resolve()
        if not path.is_relative_to(ARTICLE) or path in stack:
            raise ValueError(f"Invalid or recursive input: {path}")
        return expand_inputs(uncomment(path.read_text()), (*stack, path))

    return re.sub(r"\\input\{([^}]+)\}", expand, source)


def labels_from_aux() -> tuple[dict[str, str], dict[str, str]]:
    source = (ARTICLE / "build/article.aux").read_text()
    labels = dict(re.findall(r"\\newlabel\{([^}]+)\}\{\{([^}]+)\}", source))
    citations = dict(re.findall(r"\\bibcite\{([^}]+)\}\{(\d+)\}", source))
    if not labels or not citations:
        raise ValueError("Build the LaTeX manuscript before exporting DOCX")
    return labels, citations


def render_figures(
    source: str, labels: dict[str, str]
) -> tuple[str, list[dict[str, str]]]:
    pictures = []
    preamble = (ARTICLE / "include/preambule.tex").read_text()

    def convert(figure: TikzFigure) -> str:
        if len(figure.pictures) != 1:
            raise ValueError(
                "The native-canvas backend needs one TikZ picture per figure; use a panel-aware renderer for grouped figures"
            )
        caption = figure.caption
        width_cm = 16 * figure.width_fraction
        identifier = figure.label
        number = labels[identifier]
        stem = BUILD / f"figure-{number}"
        editable_picture, node_labels = instrument(figure.pictures[0])
        tex = (
            "\\documentclass[a4paper,12pt]{article}\n"
            + preamble
            + "\n\\usepackage[active,tightpage]{preview}\n"
            + "\\PreviewEnvironment{tikzpicture}\n\\setlength{\\PreviewBorder}{4pt}\n"
            + measurement_preamble(stem.name + ".nodes")
            + "\\begin{document}\n"
            + editable_picture
            + "\n\\end{document}\n"
        )
        stem.with_suffix(".tex").write_text(tex)
        run_command(
            [
                "pdflatex",
                "-no-shell-escape",
                "-interaction=nonstopmode",
                "-halt-on-error",
                f"-output-directory={BUILD}",
                stem.with_suffix(".tex"),
            ],
            log=stem.with_suffix(".console.log"),
        )
        scene = read_scene(stem.with_suffix(".pdf"), node_labels)
        stem.with_suffix(".scene.json").write_text(
            json.dumps(scene, ensure_ascii=False, indent=2)
        )
        run_command(
            [
                "pdftocairo",
                "-png",
                "-singlefile",
                "-r",
                "300",
                stem.with_suffix(".pdf"),
                stem,
            ]
        )
        pictures.append(
            {
                "label": identifier,
                "number": number,
                "file": stem.name + ".png",
                "scene_file": stem.name + ".scene.json",
                "sha256": hashlib.sha256(
                    stem.with_suffix(".png").read_bytes()
                ).hexdigest(),
            }
        )
        return (
            "\n\\begin{figure}\n"
            + f"\\includegraphics[width={width_cm:g}cm]{{{stem.with_suffix('.png')}}}\n"
            + f"\\caption{{{caption}}}\\label{{{identifier}}}\n\\end{{figure}}\n"
        )

    return replace_figures(source, convert), pictures


def prepare_tex(
    labels: dict[str, str], citations: dict[str, str]
) -> tuple[str, dict[str, Any]]:
    driver = uncomment((ARTICLE / "article.tex").read_text())
    body = driver.split(r"\begin{document}", 1)[1].split(r"\end{document}", 1)[0]
    body = expand_inputs(body)
    # Keep the actual title/authors/affiliation, not the PDF running-header commands.
    body = body[body.index(r"\begin{center}") :]
    body = re.sub(r"\\cmidrule(?:\([^)]*\))?\{[^}]+\}", "", body)
    body, figures = render_figures(body, labels)
    references = []

    def reference(match: re.Match[str]) -> str:
        key = match[2]
        if key not in labels:
            raise ValueError(f"Unresolved reference: {key}")
        references.append(key)
        return f"({labels[key]})" if match[1] == "eqref" else labels[key]

    body = re.sub(r"\\(eqref|ref)\{([^}]+)\}", reference, body)
    cited = []

    def citation(match: re.Match[str]) -> str:
        keys = [key.strip() for key in match[2].split(",")]
        cited.extend(keys)
        values = sorted({int(citations[key.strip()]) for key in keys})
        numbers = ", ".join(map(str, values))
        suffix = ", " + match[1] if match[1] else ""
        return "[" + numbers + suffix + "]"

    body = re.sub(r"\\cite(?:\[([^]]*)\])?\{([^}]+)\}", citation, body)
    equations = []

    def equation(match: re.Match[str]) -> str:
        content = match[1]
        keys = re.findall(r"\\label\{([^}]+)\}", content)
        if len(keys) != 1:
            raise ValueError("Every numbered equation needs exactly one label")
        number = labels[keys[0]]
        equations.append({"label": keys[0], "number": number})
        content = re.sub(r"\\label\{[^}]+\}", "", content)
        return "\n\\[" + content + f"\\qquad\\text{{({number})}}" + "\\]\n"

    body = re.sub(
        r"\\begin\{equation\}(.*?)\\end\{equation\}", equation, body, flags=re.S
    )
    body = re.sub(
        r"\\begin\{equation\*\}(.*?)\\end\{equation\*\}",
        lambda m: "\\[" + m[1] + "\\]",
        body,
        flags=re.S,
    )

    def statement(match: re.Match[str]) -> str:
        return "\\textbf{Утверждение " + labels[match[2]] + " (" + match[1] + ").} "

    body = re.sub(r"\\begin\{statement\}\[([^]]+)\]\\label\{([^}]+)\}", statement, body)
    body = body.replace(r"\end{statement}", "")
    body = re.sub(r"\\addcontentsline\{[^}]*\}\{[^}]*\}\{[^}]*\}", "", body)
    bbl = (ARTICLE / "build/article.bbl").read_text()
    items = re.findall(
        r"\\bibitem\{([^}]+)\}(.*?)(?=\\bibitem|\\end\{thebibliography\})", bbl, re.S
    )
    bibliography = []
    for key, entry in items:
        entry = re.sub(r"\\selectlanguageifdefined\{[^}]+\}", "", entry)
        entry = entry.replace(r"\BibDash", " --- ").replace(r"\newblock", " ")
        entry = entry.replace(r"\BibEmph", r"\emph").replace(r"\BibUrl", r"\url")
        bibliography.append(f"\\noindent {citations[key]}. {entry.strip()}\n\n")
    if set(cited) != {key for key, _ in items}:
        raise ValueError("Citations and compiled bibliography disagree")
    body = re.sub(
        r"\\bibliography\{[^}]+\}",
        lambda _: "\\section*{Литература}\n" + "".join(bibliography),
        body,
    )
    macros = "\\newcommand{\\Vec}[1]{\\mathbf{#1}}\n\\newcommand{\\fitwidth}[1]{#1}\n"
    return macros + body, {
        "figures": figures,
        "equations": equations,
        "labels": labels,
        "references": references,
        "citations": citations,
        "bibliography_keys": [key for key, _ in items],
    }
