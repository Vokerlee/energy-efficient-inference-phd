# Computing Extremely Accurate Quantiles Using t-Digests

- Citation key: `dunning2019tdigest`.
- Authors: Dunning, Ted; Ertl, Otmar.
- Publication: arXiv preprint, 2019.
- Source: [paper](https://arxiv.org/abs/1902.04023v1); [full text reviewed](https://arxiv.org/pdf/1902.04023v1).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Streaming summaries, centroids, merging, and tail quantiles.
- Evidence: Streaming-statistics algorithm and evaluation.

## What it establishes

Approximates rank statistics using compact summaries rather than retaining and sorting all observations.

## Relevance to our goals

A software reference for evaluating whether richer tail statistics improve quantization decisions.

## Limits and transfer conditions

This is not a neural-accelerator circuit. Sorting/merging, state, update latency, and nonstationary-window behavior require separate hardware analysis.
