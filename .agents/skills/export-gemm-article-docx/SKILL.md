---
name: export-gemm-article-docx
description: Export and validate the GEMM simulator accuracy article as an editable journal-profile DOCX from its LaTeX sources, including TikZ figures, GOST references and Word mathematics. Use for this manuscript's conversion workflow and rendering defects.
---

# Export the GEMM article to Word

Locate the repository containing `publications/gemm-simulator-accuracy/article.tex`.
Read that article's [README](../../../publications/gemm-simulator-accuracy/README.md)
before editing conversion rules. It is the canonical source for the journal
profile, inspected published examples, build commands, known limitations and
the converter comparison. Do not duplicate those rules in this skill.

The article targets **Electronic Engineering. Series 3. Microelectronics**,
ISSN 2410-9932. Use modern editable OMML mathematics in DOCX. The old template's
Equation 3.0 wording does not require reintroducing legacy equation objects.

## Work on the correct layer

- Keep manuscript text and bibliography in LaTeX/BibTeX. Do not silently rewrite
  scientific claims, abbreviate the abstract, invent author information or
  translate missing front matter during conversion.
- Use `scripts/latex_source.py` for manuscript-specific source preparation and
  TikZ rendering, `scripts/word_document.py` for Word layout and math properties,
  and `scripts/check_docx.py` for content-preservation checks. The short
  `scripts/export_docx.py` orchestrates them. Keep Python typed and Ruff-formatted.
- Reuse the compiled LaTeX label map and GOST bibliography. Word references are
  regenerated static numbers; do not promise live Word fields.
- Render formulas directly from LaTeX to OMML, retaining editability. The PDF
  rendering path is for TikZ figures and document previews, not formula OCR.
- Treat the README's publication-page observations as layout evidence, distinct
  from mandatory submission rules. Do not copy publisher branding, blue banners,
  article DOI assignments, acceptance dates or production columns into a submission.

## Build and inspect

From the repository root, run `make -C publications docx-setup` once, then
`make -C publications docx` and `make -C publications docx-check`.
Use `make -C publications docx-preview` when LibreOffice is available. Check its
`build/docx/preview.log`; distinguish conversion diagnostics from rendering issues.
Final generated files belong directly in `publications/` and remain ignored.
Intermediate artifacts and reports belong in the article's `build/docx/`.

After changing conversion code, run a clean export and the checker, and check
Ruff with the exact version pinned in the article's `requirements.txt`.
Inspect representative fractions/norms, indices, accents, sums/products, gradient
decomposition, Cyrillic math text, equation numbers, tables, figures and references.
Counts alone do not establish mathematical equivalence or an acceptable layout.
For document-structure changes, test that deliberate content loss is rejected.

When a formula looks wrong, identify whether the defect is in the prepared
LaTeX, the native Word math, or the PDF renderer. Compare the same expression
across the original LaTeX PDF, DOCX and DOCX-derived PDF. Word and LibreOffice
rendering are separate checks. The README records a confirmed LibreOffice
parenthesis defect and the isolated preview-size setting; do not infer that
switching a converter automatically fixes either issue.

Document additional verified formatting observations in the article README,
with source URLs, dates, page pointers and their status. Do not commit downloaded
third-party papers or generated Word/PDF files. Final visual approval remains
separate from successful content-preservation checks; report exactly what was
tested and any outstanding Word/layout checks.
