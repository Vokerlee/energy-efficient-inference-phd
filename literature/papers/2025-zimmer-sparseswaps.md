# SparseSwaps: Tractable LLM Pruning Mask Refinement at Scale

- Citation key: `zimmer2025sparseswaps`.
- Authors: Zimmer, Max; Roux, Christophe; Wagner, Moritz; Hendrych, Deborah; Pokutta, Sebastian.
- Publication: arXiv author version, 2025; `2512.10922v1` reviewed.
- Source: [paper](https://arxiv.org/abs/2512.10922v1); [full text](https://arxiv.org/html/2512.10922v1).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Sections 2.1–2.2 and Algorithm 1.

## What it establishes

Refines parameter-pruning masks using a quadratic loss expressed through a calibration-activation Gram matrix. Scalar swap scores avoid retaining all individual products.

## Relevance to our goals

A clear comparator against claiming that Gram-based mask optimization or pairwise interactions are new mathematical ideas.

## Limits and transfer conditions

The Gram matrix summarizes calibration inputs and supports prepared weight masks. That differs from fixed receiving-weight metadata and input-dependent activation masks, but transposing the algebra alone is not a demonstrated contribution. Whole-model and runtime costs remain separate.
