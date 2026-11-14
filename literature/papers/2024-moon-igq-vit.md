# Instance-Aware Group Quantization for Vision Transformers

- Citation key: `moon2024igqvit`.
- Authors: Moon, Jaehyeon; Kim, Dohyung; Cheon, Junyong; Ham, Bumsub.
- Publication: CVPR, 2024; author preprint version 1 reviewed.
- Source: [paper](https://arxiv.org/abs/2404.00928v1); [full text](https://arxiv.org/html/2404.00928v1).
- Reviewed: 2026-11-15. Status: **full-text focused reading**.
- Reading focus: Sections 3.2–3.3: grouping, preparation, and inference overhead.
- Evidence: Instance-dependent assignments and calibrated quantizers; not reproduced here.

## What it establishes

IGQ-ViT assigns activation channels to quantizer groups using current min/max
statistics. Quantizer parameters are fixed after calibration; assignments vary
per input. It extends grouping to softmax-attention rows and prepares layer
group counts under a BOP constraint.

## Relevance to our goals

Dynamic activation grouping is established. This distinguishes live membership
selection from choosing new group counts or scales online.

## Limits and transfer conditions

Include statistics, assignment, groupwise products, and floating-point output
combination. A BOP count is not hardware energy. Noncontiguous memberships
need an explicit physical layout/schedule; a representation group is not
automatically a systolic execution tile.
