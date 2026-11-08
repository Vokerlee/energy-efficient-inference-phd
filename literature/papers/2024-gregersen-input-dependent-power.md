# Input-Dependent Power Usage in GPUs

- Citation key: `gregersen2024inputpower`.
- Authors: Gregersen, Theo; Patel, Pratyush; Choukse, Esha.
- Publication: arXiv preprint, 2024.
- Source: [paper](https://arxiv.org/abs/2409.18324v1); [full text reviewed](https://arxiv.org/pdf/2409.18324v1).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Experiment setup, input-pattern sweeps, and discussion.
- Evidence: CUTLASS GEMM measurements on an A100 PCIe VM.

## What it establishes

Holding matrix dimensions and kernels fixed, different operand patterns change reported power by up to approximately 38%, while iteration times remain similar. Experiments use repeated 2048-square GEMMs.

## Relevance to our goals

Motivates distinguishing operation count from data-dependent switching activity when evaluating activation transformations.

## Limits and transfer conditions

Synthetic patterns, coarse power sampling, and proprietary GPU internals limit mechanism attribution. These observations do not establish the same savings for natural activations or our hardware.
