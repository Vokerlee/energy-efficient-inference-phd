# GEMM simulator accuracy

This publication uses the repository's [CC BY 4.0 license](../../LICENSE).
The bundled GOST bibliography style retains its own notices.

## LaTeX and Word workflow

Edit `article.tex`, `include/`, `parts/`, and `literature.bib`. The Word file is
generated from those sources; do not maintain a second manuscript in Word.
Export targets **Electronic Engineering. Series 3. Microelectronics**
(ISSN 2410-9932). Modern editable Word equations (OMML) are the chosen format.

From the repository root:

```sh
make -C publications docx-setup
make -C publications docx
make -C publications docx-check
make -C publications docx-preview
```

The first command installs checksum-pinned Pandoc 3.14 inside this article's
ignored `.tools/` directory (Linux x86-64), creates `.tools/python/`, and installs
`requirements.txt`: pypdf 7.1.1 for reading TikZ geometry and Ruff 0.14.5 for
formatting/checking Python. Conversion also needs Python 3.10+, the existing
LaTeX toolchain and Poppler's `pdftocairo`. Make targets use the local Python
environment; do not install these dependencies globally.

`docx-preview` additionally requires LibreOffice Writer. It renders the actual
DOCX, not the original LaTeX PDF. Install Times New Roman and Cambria Math on
the viewing/rendering machine; font names in a document do not install fonts.
Do not redistribute proprietary fonts with the repository.

Outputs appear directly in `publications/`:

- `gemm-simulator-accuracy.pdf`: the original LaTeX rendering;
- `gemm-simulator-accuracy.docx`: editable Word export;
- `gemm-simulator-accuracy-docx-preview.pdf`: optional rendering of that DOCX.

Generated documents are ignored. Intermediate figures, the prepared source,
Pandoc AST, input hashes, conversion logs and `validation.json` stay in
`build/docx/`. `clean` removes documents and intermediate files, retaining
installed tools. Re-run export after changing the manuscript or converter.

The exporter uses the compiled LaTeX labels and GOST `.bbl` bibliography to
preserve numbering and reference order. Cross-references in Word are regenerated
numbers, not live Word fields. All seven TikZ figures become native Word
DrawingML canvases containing editable shapes and text. Formulas inside their
labels use OMML; data tables also remain native Word objects. Vector notation
uses bold symbols in the export, as requested by the journal template.

### Native TikZ diagrams

TikZ remains the only diagram source. During export, TeX resolves node positions
and font sizes. pypdf extracts the painted paths from the cropped figure PDF;
PDF glyphs are ignored. Pandoc converts the original node-label TeX into Word
text and OMML, and the exporter combines them with native DrawingML geometry.
Thus labels remain text, rather than outlines of individual letters. Curved
arrows, rounded boxes, dashed boundaries and the logarithmic scale retain their
geometry. In Word, select a drawing canvas and then its individual objects to
edit their text, shape or position.

The current manuscript produces seven canvases, 200 shape objects and 82 editable
labels containing 65 OMML expressions. These are additional to the 290 math
objects in the article body. The final DOCX contains no image parts or image
relationships. PNG files in `build/docx/` are temporary Pandoc layout placeholders
and visual references; the native objects replace them before validation.

Arrows are editable freeform paths and arrowhead shapes, not attached connectors:
moving a block does not automatically reroute its arrows. Text layout depends on
Word's fonts and can differ from TeX. This converter supports the TikZ constructs
used by this manuscript, including its literal coordinate-list `foreach` loop;
it is not a general TikZ interpreter. Unsupported PDF drawing operations fail
export rather than silently falling back to an image. New diagram constructs
need an explicit conversion/visual check.

The representation uses Microsoft's [WordprocessingML drawing extensions](https://learn.microsoft.com/en-us/openspecs/office_standards/ms-odrawxml/87221dc8-13de-4885-89b8-429c078ed191).
The generated document was checked with Microsoft Open XML SDK 3.3.0 against
Office 2019 schemas with zero validation errors. This checks document structure,
not visual layout or interactive editing in Word.

Regression checks, after building the DOCX:

```sh
cd publications/gemm-simulator-accuracy
.tools/python/bin/python -m unittest discover -s scripts -p 'test_*.py' -v
.tools/python/bin/ruff check scripts
.tools/python/bin/ruff format --check scripts
```


## Formatting sources

Checked **2026-11-21**. Keep this section as the shared formatting reference for
future export sessions. Distinguish the author instructions from observations
of published pages and from implementation choices. Published examples do not
override explicit submission instructions.

The current scripts provide a technical baseline; final visual approval remains
a separate editing step. Do not describe the generated file as submission-ready.

The [Forum author-instructions page](https://microelectronica.pro/uchastnikam/trebovaniya-k-tezisam-i-dokladam)
links the journal's [Word template](https://2025.microelectronica.online/print/%D0%AD%D0%9B%D0%95%D0%9A%D0%A2%D0%A0%D0%9E%D0%9D%D0%9D%D0%90%D0%AF_%D0%A2%D0%95%D0%A5%D0%9D%D0%98%D0%9A%D0%90.doc).
This is an undated legacy template, not a verified newly issued 2026 standard.
Its Equation 3.0 requirement is deliberately replaced here by modern OMML.

### Structure of the article

Rechecked the template linked by the Forum 2026 author page on 2026-11-21.
It specifies front matter, abstracts, keywords, body formatting, equations,
tables, figures, references and author details. It does **not** prescribe
mandatory body-section titles, their number, an IMRAD sequence or heading
numbering. The headings in the template such as “Формулы” and “Таблицы”
organize its formatting instructions; they are not required manuscript sections.
Choose the manuscript sections to follow its research argument. This finding
concerns the available undated template, not an independently dated 2026
editorial policy.

The template also explicitly requires abbreviation definitions and explanations
of figure labels; it disallows shortened words in table cells except units. Diagrams must remain legible when reduced; illustrations
must be inserted at the relevant point in the text. For this manuscript, figure
labels use the same base font size as body text without scaling the entire
diagram. Relative speedup ranges are outward-rounded bounds of existing
measurements, not invented samples or confidence intervals.

### Complete published examples inspected for formatting

The [journal archive](https://www.niime.ru/science/) identifies the journal and
issues. Its linked 2025/2026 regular-issue PDFs examined here contain contents
and abstracts, not complete articles; they are insufficient for checking body
layout. Full articles were inspected in these accessible publications:

| Publication | Pages inspected and purpose |
|---|---|
| N. A. Vologzhanin, I. A. Golubeva, *Research and development of a method for constructing neural operators for a digital twin software platform*, 2026, 1S(202), pp. 87–100, DOI 10.7868/S2410993226050118 | Printed pp. 87–90, 98–100: bilingual front matter, numbered headings, display mathematics and figure captions. |
| A. M. Kulish, *GaAs low-noise amplifiers manufactured using the GA05-D-L-01 technological process*, 2026, 1S(202), pp. 245–255, DOI 10.7868/S2410993226050337 | Printed pp. 245–255: plotted figures, subfigure markers, captions, tables and bibliography. |
| I. A. Golubeva, L. G. Gagarina, N. A. Vologzhanin, *Predictive maintenance in the domain*, 2026, 1S(202), pp. 378–385, DOI 10.7868/S2410993226050520 | Printed pp. 378–385: table before body discussion, mathematical notation, subheadings and references. |
| A. S. Shalimov, *A method of removing a random constant component from an input signal under strong noise and a priori uncertainty*, 2018, 3(171), pp. 37–43 | Historical cross-check, printed pp. 37–39: single-column layout and right-aligned equation numbers. Not evidence of current submission rules. |

The [Kulish publication page](https://www.mwsystems.ru/publications.html/id/139)
links a [full 2026 special-issue PDF](https://www.mwsystems.ru/attach/article/139.pdf)
containing all three 2026 examples, not just that one article. PDF page numbers
are one greater than the printed article pages: e.g. printed p. 87 is PDF p. 88.
The historical example is in the publisher's
[complete 2018 issue](https://www.niime.ru/upload/zhurnal-mikroelektronika/3%20%D0%9D%D0%BE%D0%BC%D0%B5%D1%80%20%D0%B6%D1%83%D1%80%D0%BD%D0%B0%D0%BB%D0%B0%202018.pdf#page=37).
These are formatting inspections, not reviews of the papers' scientific claims.
Keep third-party PDFs outside Git; retain these source links and page pointers.

### Reusable formatting rules

| Element | Rule for this manuscript | Basis |
|---|---|---|
| Main text | Times New Roman, 14 pt, 1.5-line spacing. | Author template. |
| Front matter | UDC; Russian title, authors, affiliations, abstract and keywords; English counterparts; full author/contact details. Never invent missing information during export. | Author template; bilingual ordering also visible on 2026 pp. 87, 245, 378. |
| Abstracts and keywords | At most 500 characters per abstract and five keywords per language. Measure after rendering textual markup; do not silently shorten the article. | Author template. |
| Headings | Preserve section hierarchy and existing numbering; keep headings with the following paragraph. Use semantic Word styles. | Numbered and unnumbered headings both occur in the inspected articles. |
| Equations | Editable mathematics, consistent math font/size, centered display expressions, parenthesized numbers at the right. Keep numbers outside mathematical content. Number only equations referred to in the text. | Author template; historical pp. 38–39 show equation-number placement. Modern examples also contain unnumbered displays. |
| Mathematical notation | Italic scalar variables, upright function names/text/units, bold vectors without arrows; preserve all indices, accents and delimiters. | Author template; checked against the mathematical examples. |
| Tables | Native Word tables, numbered caption above, width at most 16 cm. Retain merged headers, units and footnotes; repeat header rows when split across pages. | Native format, captions and width: author template. Repeated headers: export convention. |
| Figures | Preserve aspect ratio and readable labels; keep captions below, prefixed `Рис. N.`. Keep the image with its caption and preserve subfigure markers. | Author template and the 2026 examples. |
| Bibliography | Heading `Литература`, sequential entries and square-bracket citations consistent with the compiled GOST bibliography. Preserve DOI/URL text. | Author template and inspected reference lists. |
| Pagination and decoration | Single-column submission document. Do not copy issue headers, blue banners, publisher logos, DOI assignments or acceptance dates from published pages. | Submission choice: the 2026 two-column production layout is different from the 2018 layout and is not a submission requirement. |

### Export checks and final layout pass

The checker compares prepared non-mathematical text against Word XML, verifies
input hashes, editable equation counts, native table counts, native diagram
geometry/label hashes and baseline font/spacing settings. It rejects embedded
pictures, lost shapes, altered labels and missing diagram mathematics. It rejects unresolved references and
unconverted raw TeX. Counts do not prove mathematical equivalence or good layout.

Numbered displays use separate Word text for the number and explicit center/right
tab stops. The DOCX declares Cambria Math at 14 pt; the isolated LibreOffice
preview profile also sets Math's import default to 14 pt. Parentheses surrounding
normal text are placed outside `\text{…}` during export to avoid LibreOffice's
escaped-parenthesis import defect. The LaTeX sources are not rewritten.

Before submission, compare representative original and exported equations:
fractions/norms, nested indices, accents, Jacobian products, sums, the gradient
decomposition and Cyrillic text inside mathematics. Check Word and LibreOffice
separately: their math rendering differs. In particular, a LibreOffice rendering
probe exposed literal escaped parentheses for `\text{(…)}`; a successful export
alone does not establish correct visual rendering.

Microsoft Word was not available for rendering in the development environment.
LibreOffice Writer 24.2.7.2 and 26.8.3.1 were used for native-diagram preview
checks. Both open the document, but some elements of the hierarchy diagram shift
when the canvas occurs inside the paginated full article. The same native canvas
renders in its expected positions in an isolated DOCX. Therefore the full-article
LibreOffice PDF is currently unsuitable for approving diagram placement. It also
selects its own mathematical fonts. Check the final document in Microsoft Word;
XML validation and standalone rendering do not establish Word's visual result.

The current export remains a draft. The final visual pass is separate from
content preservation: inspect page breaks, long equations, equation-number
alignment, table widths, captions and figure labels. Missing translations,
UDC and author details remain manuscript work, not automatic converter guesses.

## Existing converters considered

- [Pandoc](https://github.com/jgm/pandoc) remains the parsing and OMML backend.
  The local scripts adapt this specific manuscript and the journal profile;
  they do not implement a general LaTeX parser or mathematical typesetter.
- [tex2word](https://github.com/yfyang86/tex2word), version 1.2.0, was tried on
  the prepared article source. It produced seven tables and seven figures,
  reporting 287 OMML objects and no warnings. The Pandoc route produced 290:
  the three additional objects are the mathematical `*`/dagger footnote
  markers that tex2word represents differently, not evidence of three lost
  scientific expressions. Its LibreOffice preview reproduced the escaped
  parentheses defect. This trial did not establish better formula fidelity,
  so it has not replaced the current backend.
- [latex2word](https://github.com/54cwh/latex2word) also uses Pandoc for
  mathematics and a separate Word layout layer. Its documentation was inspected;
  it was not executed on this article.

The tex2word trial used an isolated temporary environment: tex2word 1.2.0,
lxml 6.1.3, pylatexenc 2.11 and latex2mathml 3.81.1. These are not runtime
dependencies of the retained exporter. Reassess alternatives against actual
article content and rendering, rather than README feature claims alone.
