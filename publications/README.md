# Publications

Manuscript sources are kept in one directory per article. The current
`gemm-simulator-accuracy` manuscript is the existing Russian article draft.

Requires GNU Make, `latexmk`, pdfLaTeX, BibTeX, and the LaTeX packages used by
the manuscript preamble, including Russian language/T2A fonts and TikZ.
The publications Makefile builds all articles; each article also has its own Makefile.
Generated PDFs are written directly to this directory, named after the article
(for example, `gemm-simulator-accuracy.pdf`). Auxiliary files stay in each
article's ignored `build/` directory. Generated PDFs are also ignored by Git.
The `clean` target removes generated files. Builds retain their PDF and log,
and run with shell escape disabled. `latexmk` invokes `pdflatex` explicitly and
handles any additional passes needed for references and bibliographies.

The [GEMM article README](gemm-simulator-accuracy/README.md) documents its editable
Word export, journal formatting evidence and optional DOCX-derived PDF preview.
Generated Word files also appear directly here and remain ignored by Git.

The repository-local [formal LaTeX writing skill](.agents/skills/formal-latex-writing/SKILL.md)
guides scientific prose, notation, quantitative comparisons and the distinction
between observed results, mathematical conclusions and hypotheses. Its local
context is confined to `publications`; it requires no global skill installation.
