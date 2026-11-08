# Flexagon: A Multi-Dataflow Sparse-Sparse Matrix Multiplication Accelerator for Efficient DNN Processing

- Citation key: `munoz2023flexagon`.
- Authors: Munoz-Martinez, Francisco; Garg, Raveesh; Abellan, Jose L.; Pellauer, Michael; Acacio, Manuel E.; Krishna, Tushar.
- Publication: ASPLOS, 2023.
- Source: [paper](https://arxiv.org/abs/2301.10852v1); [full text reviewed](https://arxiv.org/pdf/2301.10852v1).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Sparse dataflow taxonomy, merger-reduction network, and evaluation.
- Evidence: Cycle-level sparse-accelerator simulation and implementation cost analysis.

## What it establishes

Supports inner-product, outer-product, and Gustavson-style sparse computation through a configurable merger/reduction substrate and tailored storage.

## Relevance to our goals

Shows that sparse execution efficiency depends on traversal, intermediate products, and merging rather than sparsity percentage alone.

## Limits and transfer conditions

Sparse-sparse assumptions differ from dense-weight activation-sparse inference. Simulated performance comparisons are not measured whole-network energy savings.
