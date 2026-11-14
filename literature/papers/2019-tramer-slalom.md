# Slalom: Fast, Verifiable and Private Execution of Neural Networks in Trusted Hardware

- Citation key: `tramer2019slalom`.
- Authors: Tramèr, Florian; Boneh, Dan.
- Publication: ICLR 2019; arXiv 1806.03287v2, 2019-02-27.
- Source: [paper](https://arxiv.org/abs/1806.03287v2); [PDF](https://arxiv.org/pdf/1806.03287v2).
- Reviewed: 2026-11-15. Status: **full-text focused reading**.
- Reading focus: Sections 2.2 and 3.1–3.2; Table 2 and Lemma 3.1.
- Evidence: Randomized verification of outsourced linear operators and implementation results; not reproduced here.

## What it establishes

Uses Freivalds-style identities to verify linear layers. For convolution it
checks projected outputs using projected kernels. Fixed-weight preprocessing
reduces online verification work; batching provides another amortization path.

## Relevance to our goals

Direct precedent for associating a neural matrix product with a small projected
computation. Charge formation and reuse of operand projections explicitly.

## Limits and transfer conditions

Finite-field integrity checks are different from estimating real quantization
error and selecting precision. Its secrecy-based reuse argument does not give
an accuracy theorem for a controller that observes and acts on its sketch.
