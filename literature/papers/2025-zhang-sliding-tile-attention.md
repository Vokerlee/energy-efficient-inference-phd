# Fast Video Generation with Sliding Tile Attention

- Citation key: `zhang2025sta`.
- Authors: Zhang, Peiyuan; Chen, Yongqi; Su, Runlong; Ding, Hangliang; Stoica, Ion; Liu, Zhengzhong; Zhang, Hao.
- Publication: ICML, 2025.
- Source: [paper](https://arxiv.org/abs/2502.04507v3); [full text reviewed](https://arxiv.org/pdf/2502.04507v3).
- Reviewed: 2026-11-14. Status: **full-text focused reading**.
- Reading focus: Sections 2–3: tile windows, mask regularity, producer/consumer execution, and profiling.
- Evidence: Hardware-aware attention algorithm and video-model GPU evaluation.

## What it establishes

Aligns spatial-temporal attention windows with compute tiles so retained blocks execute densely; profiles window choices per head.

## Relevance to our goals

Shows why fewer token interactions are insufficient when masks fragment physical blocks.

## Limits and transfer conditions

Separate the training-free profiled configuration from fine-tuned variants. Kernel speedups are neither end-to-end speedups nor energy measurements.
