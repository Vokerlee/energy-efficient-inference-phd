# FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision

- Citation key: `shah2024flashattention3`.
- Authors: Shah, Jay; Bikshandi, Ganesh; Zhang, Ying; Thakkar, Vijay; Ramani, Pradeep; Dao, Tri.
- Publication: arXiv preprint, 2024.
- Source: [paper](https://arxiv.org/abs/2407.08608v2); [full text reviewed](https://arxiv.org/pdf/2407.08608v2).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Asynchronous scheduling, block quantization, and incoherent processing.
- Evidence: Hopper GPU implementation and numerical evaluation.

## What it establishes

Overlaps data movement, matrix computation, and softmax while supporting a low-precision attention path.

## Relevance to our goals

Shows that precision and scheduling/fusion must be designed together.

## Limits and transfer conditions

Hardware-specific mechanisms and local numerical comparisons do not establish complete-model energy gains or direct portability to a systolic ASIC.
