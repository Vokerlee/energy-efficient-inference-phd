# SPOTS: An Accelerator for Sparse Convolutional Neural Networks Leveraging Systolic General Matrix-Matrix Multiplication

- Citation key: `soltaniyeh2022spots`.
- Authors: Soltaniyeh, Mohammadreza; Martin, Richard P.; Nagarakatte, Santosh.
- Publication: ACM Transactions on Architecture and Code Optimization, 2022.
- Source: [paper](https://doi.org/10.1145/3532863); [full text reviewed](https://arxiv.org/pdf/2107.13386v2).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Patch units, overlap buffers, zero-block tags, and evaluation.
- Evidence: Accelerator design and implementation/simulation evaluation.

## What it establishes

Pipelines hardware window generation with configurable systolic GEMM. Distributed local patch storage reuses overlapping input values, while tagged zero blocks support sparse execution.

## Relevance to our goals

A close baseline for im2col plus systolic sparsity; establishes that this combination alone is not a new contribution.

## Limits and transfer conditions

The reviewed technical-report version predates the journal publication. Supported shapes, pruning format, local storage, and reconfiguration costs matter; element zeros do not imply skippable blocks.
