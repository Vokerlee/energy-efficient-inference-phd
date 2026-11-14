# CADyQ: Content-Aware Dynamic Quantization for Image Super-Resolution

- Citation key: `hong2022cadyq`.
- Authors: Hong, Cheeun; Baik, Sungyong; Kim, Heewon; Nah, Seungjun; Lee, Kyoung Mu.
- Publication: ECCV, 2022.
- Source: [paper](https://arxiv.org/abs/2207.10345); [full text reviewed](https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136670360.pdf).
- Reviewed: 2026-11-14. Status: **full-text focused reading**.
- Reading focus: Sections 3.3–3.4: selector inputs, training, and fixed-weight handling.
- Evidence: Trained selector and super-resolution quality/bit-operation evaluation.

## What it establishes

Selects activation precision per layer and image patch using channel-wise feature deviation and patch gradients; weights use fixed precision.

## Relevance to our goals

An existing feature-driven precision policy, including the cost of gathering its input statistics.

## Limits and transfer conditions

Learned preparation and BitOP results do not demonstrate an autonomous systolic controller or measured chip energy.
