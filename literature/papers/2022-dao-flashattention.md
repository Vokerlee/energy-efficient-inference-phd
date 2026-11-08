# FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness

- Citation key: `dao2022flashattention`.
- Authors: Dao, Tri; Fu, Daniel Y.; Ermon, Stefano; Rudra, Atri; Re, Christopher.
- Publication: NeurIPS, 2022.
- Source: [paper](https://arxiv.org/abs/2205.14135v2); [full text reviewed](https://arxiv.org/pdf/2205.14135v2).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: IO-aware tiled attention, normalization state, and evaluation.
- Evidence: Algorithmic IO analysis and GPU implementation.

## What it establishes

Avoids materializing the complete attention matrix through tiled computation and online normalization.

## Relevance to our goals

A reference for respecting bounded local storage while composing matrix and nonlinear operations.

## Limits and transfer conditions

Exact attention means no structural attention approximation; floating-point ordering still matters. Training speedups are not inference energy measurements.
