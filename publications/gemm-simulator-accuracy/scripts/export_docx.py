#!/usr/bin/env python3
"""Build and validate this article's editable Word document."""

import argparse
import hashlib
import json
import shutil
import sys

from latex_source import BUILD, labels_from_aux, prepare_tex, run_command
from native_diagrams import replace_images
from setup_docx import ARTICLE, PANDOC, VERSION
from word_document import (
    MATH_SIZE,
    create_reference_docx,
    format_document,
    format_math_settings,
    prepare_document_ast,
    rewrite_docx,
    walk_nodes,
)

OUTPUT = ARTICLE.parent / "gemm-simulator-accuracy.docx"


def preview_profile() -> str:
    """Set Math's import size in an isolated, disposable LibreOffice profile."""
    profile = BUILD / "office-profile"
    user = profile / "user"
    user.mkdir(parents=True, exist_ok=True)
    settings = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<oor:items xmlns:oor="http://openoffice.org/2001/registry">'
        '<item oor:path="/org.openoffice.Office.Math/StandardFormat">'
        '<prop oor:name="BaseSize" oor:op="fuse">'
        f"<value>{MATH_SIZE // 2}</value></prop></item></oor:items>"
    )
    (user / "registrymodifications.xcu").write_text(settings)
    return profile.as_uri()


def preview() -> None:
    office = shutil.which("libreoffice") or shutil.which("soffice")
    if not office:
        raise RuntimeError(
            "Install LibreOffice Writer to use --preview (not needed for DOCX export)"
        )
    destination = BUILD / "preview"
    destination.mkdir(exist_ok=True)
    rendered = destination / OUTPUT.with_suffix(".pdf").name
    rendered.unlink(missing_ok=True)
    run_command(
        [
            office,
            f"-env:UserInstallation={preview_profile()}",
            "--headless",
            "--convert-to",
            "pdf",
            "--outdir",
            destination,
            OUTPUT,
        ],
        log=BUILD / "preview.log",
        allow_diagnostics=True,
    )
    if not rendered.is_file() or not rendered.read_bytes().startswith(b"%PDF-"):
        raise RuntimeError(
            "LibreOffice did not produce a PDF; see build/docx/preview.log"
        )
    shutil.copyfile(
        rendered,
        OUTPUT.with_name(OUTPUT.stem + "-docx-preview.pdf"),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--preview", action="store_true", help="Also render the DOCX with LibreOffice"
    )
    args = parser.parse_args()
    if not PANDOC.exists():
        raise SystemExit("Run make docx-setup first")
    BUILD.mkdir(parents=True, exist_ok=True)
    labels, citations = labels_from_aux()
    source, manifest = prepare_tex(labels, citations)
    (BUILD / "article.tex").write_text(source)
    document = json.loads(
        run_command([PANDOC, "-f", "latex", "-t", "json"], data=source)
    )
    document = prepare_document_ast(document, labels)
    (BUILD / "article.json").write_text(
        json.dumps(document, ensure_ascii=False, indent=2)
    )
    staged = BUILD / OUTPUT.name
    run_command(
        [
            PANDOC,
            "-f",
            "json",
            "-t",
            "docx",
            "--standalone",
            "--reference-doc",
            create_reference_docx(),
            "-M",
            "lang=ru-RU",
            "-o",
            staged,
        ],
        data=json.dumps(document),
    )
    rewrite_docx(
        staged,
        {
            "word/document.xml": format_document,
            "word/settings.xml": format_math_settings,
        },
    )
    replace_images(staged, manifest["figures"])
    manifest.update(
        pandoc=VERSION,
        math_count=sum(n["t"] == "Math" for n in walk_nodes(document)),
        table_count=sum(n["t"] == "Table" for n in walk_nodes(document)),
    )
    inputs = [
        ARTICLE / "article.tex",
        ARTICLE / "Makefile",
        ARTICLE / "requirements.txt",
        ARTICLE / "literature.bib",
        ARTICLE / "ugost2008l.bst",
    ]
    for directory, extension in (
        ("include", "*.tex"),
        ("parts", "*.tex"),
        ("scripts", "*.py"),
    ):
        inputs.extend((ARTICLE / directory).glob(extension))
    manifest["source_sha256"] = {
        str(path.relative_to(ARTICLE)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(inputs)
    }
    (BUILD / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    )
    print(
        run_command([sys.executable, ARTICLE / "scripts/check_docx.py", staged]), end=""
    )
    shutil.copyfile(staged, OUTPUT)
    print(f"Exported {OUTPUT}")
    if args.preview:
        preview()


if __name__ == "__main__":
    main()
