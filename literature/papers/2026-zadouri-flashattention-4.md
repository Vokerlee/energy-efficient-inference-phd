# FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling

- Citation key: `zadouri2026flashattention4`.
- Authors: Zadouri, Ted; Hoehnerbach, Markus; Shah, Jay; Liu, Timmy; Thakkar, Vijay; Dao, Tri.
- Publication: arXiv preprint, 2026.
- Source: [paper](https://arxiv.org/abs/2603.05451v1); [full text reviewed](https://arxiv.org/pdf/2603.05451v1).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Blackwell pipeline balance, softmax, and hardware asymmetry.
- Evidence: GPU kernel/algorithm evaluation.

## What it establishes

Reworks attention pipelines as matrix throughput grows faster than other execution resources.

## Relevance to our goals

A current example of bottlenecks moving after matrix acceleration.

## Limits and transfer conditions

Blackwell-specific throughput results do not characterize our hardware. Separate forward inference from backward/training results.
