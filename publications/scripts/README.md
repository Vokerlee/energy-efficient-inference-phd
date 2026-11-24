# Word equations

All shared publication converters live in this directory. Article directories
contain their manuscript sources and Makefiles, not copies of these modules.
Pinned dependencies and installed tools are shared in `../requirements.txt`
and the ignored `../.tools/` directory.

| Module | Responsibility and reuse |
|---|---|
| `tex_syntax.py` | Balanced arguments, comments and environment ranges; reused by source preparation, TikZ extraction and node instrumentation. |
| `tikz_figures.py` | Complete figures and subfigures, outer captions/labels, separate explanatory equations; independent of the renderer. |
| `tikz_images.py` | Separate panel graphics and publication assets; explanatory equations and panel captions remain Word content. |
| `tikz_scene.py`, `pdf_paths.py` | TeX-resolved node bounds and graphical paths for the native drawing backend. |
| `native_diagrams.py` | DrawingML canvases with native text and OMML labels. |
| `math_tex.py` | Mathematical LaTeX normalization before conversion. |
| `omml_format.py` | Native Word alignment, stretchable braces and upright word labels. |
| `omml_typography.py` | Explicit LaTeX math spaces and Greek variable italics, preserving intentional upright text. |
| `omml_validation.py` | Package validation independent of manuscript or visual profile. |
| `omml.py` | Shared public math API used by exporters, formatters and checks. |
| `word_document.py` | Word styles, equation numbering and package formatting. |
| `tool_process.py` | Shared command execution, diagnostics and logs. |
| `document_ast.py` | Structural/visible traversal and vertical grouped-figure flow without layout tables. |
| `export_docx.py`, `check_docx.py` | Build orchestration and article-level checks. |

Makefiles select the source through `PUBLICATION_SOURCE`; the default remains
`gemm-simulator-accuracy` for existing commands. Output names follow the selected
article directory. `make test` and `make lint` in this directory check the shared
implementation. The extraction API retains every panel of a grouped figure;
renderers choose whether panels become separate images or native canvases.

LaTeX is the source for mathematical structure. Pandoc writes every `Math`
node, including inline expressions and diagram-label mathematics, as native
Microsoft Word OMML in DOCX. The PDF is a visual reference, not an intermediate
source from which to reconstruct equations.

Explicit LaTeX spaces stay at their source positions: thin spaces (`\,`),
quads (`\quad`) and double quads (`\qquad`) become preserved Unicode math
spaces in OMML. Do not add ordinary spaces around every operator: Word applies
mathematical operator spacing itself. Lowercase Greek variables use math
italics; explicit Roman text and uppercase Greek retain their source style.
Cambria Math and the PDF font have different glyph metrics, so identical
source spacing does not imply pixel-identical rendering.

`omml.validate_omml` checks the actual output package. It rejects embedded
OLE/MathType objects, unconverted LaTeX, empty equations and missing source
expressions. Figure images are independent of mathematical expressions.

Keep the final document in DOCX. Do not add a DOCX-to-DOC step: the Word
97–2003 format does not retain modern equations as editable OMML. A PDF preview
must be rendered from the DOCX without saving a converted copy over it.

Passing structural checks does not establish Google Docs import fidelity or
Microsoft Word rendering; report which application was actually checked.
