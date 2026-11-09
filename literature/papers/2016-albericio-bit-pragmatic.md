# Bit-Pragmatic Deep Neural Network Computing

- Citation key: `albericio2016pragmatic`.
- Authors: Albericio, Jorge; Judd, Patrick; Delmas, Alberto; Sharify, Sayeh; Moshovos, Andreas.
- Publication: arXiv preprint, 2016.
- Source: [paper](https://arxiv.org/abs/1610.06920v1); [full text reviewed](https://arxiv.org/pdf/1610.06920v1).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: On-the-fly bit representation and lane synchronization.
- Evidence: Data-dependent architecture proposal/evaluation.

## What it establishes

Converts operands into nonzero-bit terms at runtime and processes only those terms, with synchronization affecting realized performance.

## Relevance to our goals

Hardware data-dependent work selection exists independently of model-level precision search.

## Limits and transfer conditions

Bit-level work elimination is not a general quality-aware precision controller. Results depend on its serial datapath and older convolution workloads.
