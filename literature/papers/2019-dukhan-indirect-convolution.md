# The Indirect Convolution Algorithm

- Citation key: `dukhan2019indirect`.
- Authors: Dukhan, Marat.
- Publication: arXiv preprint, 2019.
- Source: [paper](https://arxiv.org/abs/1907.02129v1); [full text reviewed](https://arxiv.org/pdf/1907.02129v1).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Indirection buffer, modified GEMM, initialization, and performance trade-offs.
- Evidence: Software algorithm and convolution benchmarks.

## What it establishes

Replaces copied im2col values with pointers to input pixel rows and a modified GEMM microkernel. Explicitly accounts for pointer loading and buffer setup.

## Relevance to our goals

Provides a CPU/reference baseline that exposes the cost of materializing windows without changing convolution semantics.

## Limits and transfer conditions

Pointer indirection is not a ready-made systolic feeder. A hardware implementation needs bounded address generation and buffering; 1×1 cases can lose performance.
