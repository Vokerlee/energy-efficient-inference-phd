# DBFS: Dynamic Bitwidth-Frequency Scaling for Efficient Software-defined SIMD

- Citation key: `yu2024dbfs`.
- Authors: Pengbo Yu; Flavio Ponzina; Alexandre Levisse; Dwaipayan Biswas; Giovanni Ansaloni; David Atienza; Francky Catthoor.
- Publication: ISVLSI 2024; DOI `10.1109/ISVLSI61997.2024.00046`.
- Source: [publisher record](https://doi.org/10.1109/ISVLSI61997.2024.00046); [author PDF](https://infoscience.epfl.ch/bitstreams/f90a1a8d-81b4-47ad-83b1-786ee19f3efb/download).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Reading focus: Sections II–V: shift-add SIMD, guard bits, repacking, critical paths and post-layout evaluation.

## What it establishes

Adapts clock frequency to selected subword widths in a shift-add SIMD datapath.
Carry boundaries shorten effective timing paths. Accumulation repacking, reuse
registers and a separate pack unit are explicit architectural components.
Evaluation uses post-layout simulation rather than a fabricated-device result.

## Relevance to our goals

Precision can affect frequency and packing as well as multiplier cost. Include
repacking and control when comparing a variable-width execution scheme.

## Limits and transfer conditions

Runtime width support does not itself establish a calibration-free rule for
choosing precision from live activation values. Ripple-carry shift-add timing
does not transfer directly to a pipelined systolic multiplier. The reported
benefits depend on the complete datapath and its comparison baseline.
