# Product-Aware Deterministic Rounding for Quantized Matrix Multiplication

- Citation key: `sao2026productrounding`.
- Authors: Sao, Piyush; Miniskar, Narasinga; Valero-Lara, Pedro; Teranishi, Keita; Seal, Sudip.
- Publication: arXiv preprint, 2026; version 1.
- Source: [paper](https://arxiv.org/abs/2609.31641v1); [full text](https://arxiv.org/html/2609.31641v1).
- Reviewed: 2026-11-24. Status: **full-text focused reading**.
- Reading focus: Sections 3, 6.1 and 8; Appendix B Algorithms 1–2 and the head/tail discussion. Proofs not independently audited.

## What it establishes

Studies coordinated dynamic rounding on fixed grids to reduce receiving-product error. Its construction uses null-space reduction and conditional-expectation completion with a stated approximation bound.

## Relevance to our goals

Output-aware rounding and coordinated errors are explicit prior art, beyond activation-domain MSE.

## Limits and transfer conditions

The direct construction includes rank/factorization and optimization work. The authors distinguish polynomial accuracy guarantees from throughput and leave kernel acceleration outside the study. It is not a lightweight streaming selector merely because activation rounding is dynamic.

## Reuse and implementation limits

Section8.2 explicitly asks how one rounded activation copy can serve multiple
output blocks. Per-block low rank is insufficient; joint receiving geometry
matters. The reported direct implementation uses repeated rank/SVD work and
distinguishes accuracy guarantees from kernel throughput. Conditional-expectation
completion with a running product-error state is already an existing algorithm.
A reduced-state implementation needs its own tail-error, reuse and actual
network evidence; it cannot inherit the full construction's certificate.
