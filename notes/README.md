# Mathematical notes

Independent pieces of mathematical background for reuse in research and
publications. Each note contains its context, assumptions, notation, derivation,
examples, limits, and references in one standalone LaTeX source.

## Index

| Note | What it explains | Files |
|---|---|---|
| Activation-error direction and matrix-output error | Why equal activation-error norms can produce different matrix-output errors; the Gram-matrix identity, reinforcement and cancellation, spectral bounds, and cross terms between finite reduction blocks. | [PDF](activation-error-direction.pdf) · [LaTeX](activation-error-direction.tex) |
| Systematic and random components of propagated error | How mean error and centered fluctuations propagate through fixed linear maps; cross-covariance terms, directional versus RMS gains, normalization, and the assumptions behind linear versus square-root growth. Includes a first-order network interpretation and literature references. | [PDF](systematic-and-random-error-propagation.pdf) · [LaTeX](systematic-and-random-error-propagation.tex) |

These are mathematical background notes. A worked example or identity does not
by itself establish behavior in trained networks, a new inference algorithm,
or preserved task quality. Check each note's assumptions before reusing it.

## Build

Run from this directory with `latexmk` and `pdflatex` installed:

```sh
make
make activation-error-direction.pdf
make systematic-and-random-error-propagation.pdf
make clean
```

PDFs are written beside their sources. Auxiliary files stay in `build/`.
`make clean` removes generated PDFs as well as auxiliary files; run `make`
again to regenerate them. Published sources and their compiled PDFs are tracked.

## Reuse

Use the source linked in the index to copy a derivation together with its symbol
definitions and assumptions. Retain the citations supporting reused results and
distinguish them from the note's own derivations and examples. Each source embeds
its bibliography so it can compile independently. Update this index when adding
a note; describe its precise content so related results can be found quickly.
