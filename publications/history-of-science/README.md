# History of science report

A Russian report titled *History of Energy-Efficient Neural Network Computing*.
It discusses publications from 1931 through the early 2020s. The latest selected
sources were published in 2023; that date describes the literature selection,
not an endpoint in the development of the field. The document contains a title
page, contents, introduction, four chapters, conclusion, and 53 linked sources.
The current build is 37 A4 pages, including the title page and bibliography.

The report focuses on general algorithmic, numerical, hardware, and system
approaches to reducing the energy required to execute neural networks. Topics
include model compression, compact architectures, distillation, sparsity,
conditional execution, data movement, quantization, hardware specialization,
and evaluation methods. Systolic organization is one historical example of
coordinating parallelism and locality, rather than the organizing theme.

Section 4.4 discusses deployment scenarios and workload organization; section
4.6 compares algorithmic and hardware approaches. Sections 2.5, 3.5, and 4.7
cover accelerator modeling, rounding and adaptive scaling, and reproducibility.
The first chapter includes Bush's differential analyzer (1931), Widrow's adaptive
circuits (1960), Landauer (1961), Bennett (1973), Wanlass and Sah's complementary
logic (1963), Wilkes's memory organization (1965), Amdahl's parallel speedup
limits (1967), and Mead's neuromorphic electronics (1990).

Periodization and comparisons between approaches are the report author's
analysis. Direct historical influence is not asserted without supporting
evidence. The structure is thematic; it does not promise chronological order.

## Official title-page template

The title page was translated into LaTeX from the supplied DOC template linked
on the [MIPT requirements page](https://mipt.ru/institute-departments/uchebno-nauchnyy-tsentr-gumanitarnykh-i-sotsialnykh-nauk/aspirant/requirements).
The original is retained as `source/title-page.doc` for comparison. Rights to
that template remain with its rights holder; the repository license for original
material does not apply to this file.

The institution and department names, heading, topic and student fields,
signature lines, supervisor and teacher blocks, and city are retained. The DOC
specifies A4, 3 cm left and 1.5 cm right margins, and 2 cm top and bottom margins.
Its main font is Times New Roman at 14 pt; the topic uses 20 pt bold, and field
explanations use 9 pt italic.

`metadata.tex` stores the report title, author Glaz R., year 2026, and the
provided enrollment details: group A01-603a, field 2.3 (Information Technologies
and Telecommunications), specialty Computing Systems and Their Elements, and
supervisor Arnold Leonidovich Plotkin, abbreviated on the title page. See the
metadata file for the exact Russian spellings. The original brackets, lines,
and field explanations are preserved. The completed group and field line uses
11 pt text to fit its existing space. The humanities-center teacher field remains
blank; sample names from the template are not treated as actual metadata.

The LaTeX text and lines remain editable; the title page is not a page image.
Wording and principal settings were checked against the DOC, but identical line
breaks and vertical positions in Microsoft Word are not guaranteed. Body settings
are Times New Roman, 14 pt, one-and-a-half spacing, and a 1.25 cm paragraph indent;
the bibliography uses 12 pt and single spacing. The dynamic requirements page
could not be extracted, so the body settings and length are not claimed as
independently confirmed MIPT requirements.

## Sources and verification

Bibliographic details and historical claims were checked against primary
publications, publisher pages, and author copies. Dates of the first electronic
publication and conference presentation are distinguished.

For the main architecture examples, the reviewed texts include Kung (1982),
Horowitz (2014), Eyeriss (2016), TPU (2017), Dynamic Stripes (2017), Bit Fusion
(2018), and Jacob et al. (2017/2018). Publication details and descriptions were
also checked for Timeloop (2019), Accelergy (2019), Gupta et al.'s stochastic
rounding work (2015), and Flexpoint (2017). Relevant full-text passages were
reviewed for the latter three; Timeloop was checked using the NVIDIA Research
publication page and available introduction. Other sources were checked through
available publication records, abstracts, and passages supporting the claims
made here. Complete reading of all 53 sources is not claimed.

The algorithmic and system context was checked against Hinton et al.'s
distillation work (2015), MobileNets (2017), EIE (2016), and BranchyNet (2016).
For BranchyNet, the 2016 conference publication is distinguished from the version
posted to arXiv in 2017. Fewer operations, smaller models, and lower energy are
not treated as interchangeable results.

The text distinguishes precision selected before execution from selection during
execution, exact elimination of zero contributions from approximate quantization,
storage compression from execution cost, and performance from energy.
Reported numerical advantages of different accelerators are not combined into
an overall ranking. Historical statements are tied to published sources, and
the author's comparisons are distinguished from those sources' results.

For the earlier history, eight primary publications from 1931–1990 were checked.
The reviewed material includes Bush's introduction and integrator description;
the summary, introduction, and memistor section of Widrow's scanned report;
available texts by Wilkes, Amdahl, and Mead; and available primary-text passages
and publication records for Landauer, Bennett, and Wanlass and Sah. Physical
limits, low-power circuit design, and neural-device energy measurements are
considered separately. Early machines are not assigned modern energy-saving
figures or undocumented influence on particular accelerators.

The account emphasizes historical research problems and results. Landauer and
Bennett are discussed through the development of questions about the physical
limits of computation. Formulas and detailed calculation procedures are omitted.
The comparison of Adaline and perceptron training was checked against Widrow and
Lehr (1995). Dennard scaling was checked against Table I of the 1974 paper.

The Eyeriss discussion includes the significance of data reuse, comparison
conditions, and the convolution-layer result for AlexNet: alternative dataflows
use 1.4–2.5 times the energy of RS in the configurations studied. The supporting
material is in sections V–VII and Figure 12 of the ISCA 2016 paper. This is
identified as an analytical comparison under specified hardware constraints.
Timeloop and Accelergy illustrate changes in research tools; HAWQ and FP8 are
placed in the history of numerical precision. Technical explanations are limited
to what is needed to understand differences between the publications.

The report uses formal scientific Russian as a standalone historical account.
References to recognition concern specific historical applications; general
statements concern the tasks solved by neural networks more broadly.

## Build

Requires GNU Make, `latexmk`, XeLaTeX, and the packages `extsizes`, `fontspec`,
`babel` with Russian support, `geometry`, `amsmath`, `setspace`, `indentfirst`,
`ragged2e`, `titlesec`, and `hyperref`. Install Times New Roman to match the
template; TeX Gyre Termes is the fallback.

```sh
make -C publications/history-of-science
```

The final PDF is `publications/history-of-science.pdf`. Auxiliary files remain
in the ignored `build/` directory. `make clean` removes generated outputs.
The title page is in `title.tex`, metadata in `metadata.tex`, the main driver
in `report.tex`, chapters in `parts/`, and the bibliography in `references.tex`.
