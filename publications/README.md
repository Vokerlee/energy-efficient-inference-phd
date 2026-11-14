# Publications

Manuscript sources are kept in one directory per article. The current
`gemm-simulator-accuracy` manuscript is an empty, buildable LaTeX document.

Requires GNU Make, `latexmk`, and pdfLaTeX with Russian language and T2A font support.
The publications Makefile builds all articles; each article also has its own Makefile.
Generated PDFs are written directly to this directory, named after the article
(for example, `gemm-simulator-accuracy.pdf`). Auxiliary files stay in each
article's ignored `build/` directory. Generated PDFs are also ignored by Git.
The `clean` target removes generated files. Builds retain their PDF and log,
and run with shell escape disabled. `latexmk` invokes `pdflatex` explicitly and
handles any additional passes needed for references and bibliographies.
