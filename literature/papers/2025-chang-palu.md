# Palu: KV-Cache Compression with Low-Rank Projection

- Citation key: `chang2025palu`.
- Authors: Chang, Chi-Chih; others.
- Publication: ICLR, 2025.
- Source: [paper](https://arxiv.org/abs/2407.21118v2); [full text reviewed](https://arxiv.org/pdf/2407.21118v2).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Projection, reconstruction, rank selection, and fused kernels.
- Evidence: KV-cache compression and GPU evaluation.

## What it establishes

Stores compressed low-rank intermediate states and reconstructs attention information with specialized kernels.

## Relevance to our goals

A comparison for projection/reconstruction cost and quantization compatibility.

## Limits and transfer conditions

The primary objective is KV-cache memory efficiency. It is not evidence of compute-bound activation-subspace savings on a systolic array.
