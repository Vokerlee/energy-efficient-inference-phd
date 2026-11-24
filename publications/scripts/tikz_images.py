"""Render figure panels; leave equations and subcaptions to Word's writer."""

import hashlib
from pathlib import Path
import re
from tool_process import run_tool

from tikz_figures import extract_panels, replace_figures, split_standalone_math


def render_figures(
    source: str,
    labels: dict[str, str],
    *,
    destination: Path,
    preamble: str,
    working_directory: Path,
    width_cm: float = 15,
    dpi: int = 600,
    extract_panel_equations: bool = False,
    caption_transform=str,
):
    records = []

    def graphic(scene: str, stem: str) -> dict:
        path = destination / stem
        for suffix in (".tif", ".tiff"):
            path.with_suffix(suffix).unlink(missing_ok=True)
        document = (
            preamble
            + "\\begin{document}\n\\color[cmyk]{0,0,0,1}\n\\begin{journalfigure}\n"
            + scene
            + "\n\\end{journalfigure}\n\\end{document}\n"
        )
        path.with_suffix(".tex").write_text(document)
        commands = [
            [
                "xelatex",
                "-no-shell-escape",
                "-interaction=nonstopmode",
                "-halt-on-error",
                f"-output-directory={destination}",
                str(path.with_suffix(".tex")),
            ],
            [
                "pdftocairo",
                "-png",
                "-singlefile",
                "-r",
                str(dpi),
                str(path.with_suffix(".pdf")),
                str(path),
            ],
            [
                "pdftops",
                "-eps",
                str(path.with_suffix(".pdf")),
                str(path.with_suffix(".eps")),
            ],
        ]
        for command in commands:
            log = path.with_suffix(".build.log") if command[0] == "xelatex" else None
            run_tool(command, cwd=working_directory, log=log, allow_diagnostics=True)
        return {
            "pdf": path.with_suffix(".pdf").name,
            "png": path.with_suffix(".png").name,
            "width_cm": width_cm,
            "pdf_sha256": hashlib.sha256(
                path.with_suffix(".pdf").read_bytes()
            ).hexdigest(),
        }

    def image(asset: dict) -> str:
        return (
            f"\\includegraphics[width={width_cm:g}cm]{{"
            + str(destination / asset["png"])
            + "}\n"
        )

    def render(figure):
        number = int(labels[figure.label])
        caption = caption_transform(figure.caption)
        record = {
            "number": number,
            "label": figure.label,
            "caption_tex": caption,
            "tikz_panels": len(figure.pictures),
        }
        parts = extract_panels(figure)
        if parts:
            record["panels"] = []
            content = []
            for index, part in enumerate(parts):
                letter = chr(ord("a") + index)
                scene, equations = (
                    split_standalone_math(part.picture)
                    if extract_panel_equations
                    else (part.picture, ())
                )
                scene = re.sub(r"\\path\[use as bounding box\][^;]*;", "", scene)
                asset = graphic(scene, f"figure-{number:02d}-{letter}")
                record["panels"].append(
                    {
                        **asset,
                        "letter": letter,
                        "caption_tex": part.caption,
                        "equations": equations,
                        "label": part.label,
                    }
                )
                content.append(image(asset))
                content.extend("\\[ " + equation + " \\]\n" for equation in equations)
                content.append(
                    "\\par\\textnormal{(" + letter + ") " + part.caption + "}\\par\n"
                )
            rendered = "".join(content)
        else:
            record.update(graphic(figure.scene, f"figure-{number:02d}"))
            rendered = image(record)
        records.append(record)
        return (
            "\n\\begin{figure}\n"
            + rendered
            + "\\caption{"
            + caption
            + "}\\label{"
            + figure.label
            + "}\n\\end{figure}\n"
        )

    return replace_figures(source, render), records
