# Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking

- Citation key: `federici2025dip`.
- Authors: Federici, Marco; Belli, Davide; van Baalen, Mart; Jalalirad, Amir; Skliar, Andrii; Major, Bence; Nagel, Markus; Whatmough, Paul.
- Publication: MLSys 2025; arXiv version 2.
- Source: [paper](https://arxiv.org/abs/2412.01380v2); [full text](https://arxiv.org/html/2412.01380v2).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Sections 4–5, especially cache-aware masking.

## What it establishes

DIP sparsifies inputs without a learned activation predictor. Its cache-aware variant reweights live activation scores using weight residency, trading approximation against transfers. Optional LoRA adaptation is a separate variant.

## Relevance to our goals

Already couples approximation decisions with memory state; cache-aware sparsity alone is not an unoccupied problem.

## Limits and transfer conditions

Targets Flash/DRAM-limited autoregressive decoding with simulated hardware. That setting differs from large matrix computation, but its policy mechanism remains a comparator. No absence of overlap follows merely from changing workloads.
