"""Prepare the article for Word without changing its LaTeX sources."""

import hashlib
import re
import subprocess
from collections.abc import Sequence
from pathlib import Path
from typing import Any

from setup_docx import ARTICLE

BUILD = ARTICLE / "build" / "docx"


def run_command(
    arguments: Sequence[str | Path],
    *,
    data: str | None = None,
    log: Path | None = None,
    allow_diagnostics: bool = False,
) -> str:
    result = subprocess.run(
        [str(value) for value in arguments],
        cwd=ARTICLE,
        input=data,
        text=True,
        capture_output=True,
        check=False,
    )
    if log:
        log.write_text(result.stdout + result.stderr)
    if result.returncode:
        raise RuntimeError(
            f"Command failed: {arguments[0]}\n{result.stdout}\n{result.stderr}"
        )
    if result.stderr.strip() and not allow_diagnostics:
        raise RuntimeError(f"Unexpected conversion diagnostic:\n{result.stderr}")
    return result.stdout


def uncomment(source: str) -> str:
    return re.sub(r"(?<!\\)%[^\n]*", "", source)


def read_tex_group(source: str, start: int) -> tuple[str, int]:
    """Read a balanced TeX argument, respecting escaped braces."""
    if source[start] != "{":
        raise ValueError("Expected a braced TeX argument")
    depth = 1
    for position in range(start + 1, len(source)):
        if source[position] in "{}" and source[position - 1] != "\\":
            depth += 1 if source[position] == "{" else -1
            if not depth:
                return source[start + 1 : position], position + 1
    raise ValueError("Unclosed TeX argument")


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

    def convert(match: re.Match[str]) -> str:
        body = match[1]
        picture = re.search(
            r"\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}", body, re.S
        )
        label = re.search(r"\\label\{([^}]+)\}", body)
        caption_start = re.search(r"\\caption\s*\{", body)
        if not picture or not label or not caption_start:
            raise ValueError("Every exported figure needs TikZ, a label and a caption")
        caption, _ = read_tex_group(body, caption_start.end() - 1)
        scaled = re.search(r"\\resizebox\{([\d.]+)\\textwidth\}", body)
        fraction = float(scaled[1]) if scaled else 1.0
        if not 0 < fraction <= 1:
            raise ValueError("Figure width must fit the available text width")
        width_cm = 16 * fraction
        identifier = label[1]
        number = labels[identifier]
        stem = BUILD / f"figure-{number}"
        tex = (
            "\\documentclass[a4paper,12pt]{article}\n"
            + preamble
            + "\n\\usepackage[active,tightpage]{preview}\n"
            + "\\PreviewEnvironment{tikzpicture}\n\\setlength{\\PreviewBorder}{4pt}\n"
            + "\\begin{document}\n"
            + picture[0]
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

    return re.sub(
        r"\\begin\{figure\}(?:\[[^]]*\])?(.*?)\\end\{figure\}",
        convert,
        source,
        flags=re.S,
    ), pictures


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
