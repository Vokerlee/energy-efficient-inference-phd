# ScalePredictor: Instance-aware Scale Learning for Accurate Quantization of Vision Transformers

- Citation key: `li2026scalepredictor`.
- Authors: Li, Changjun; Jiang, Runqing; Xu, Lian; Zhang, Ye; Hu, Qingyong; Guo, Yulan.
- Publication: arXiv preprint, 2026.
- Source: [paper](https://arxiv.org/abs/2606.21947v1); [full text reviewed](https://arxiv.org/pdf/2606.21947v1).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Shallow statistics, polynomial projection, and quality/overhead evaluation.
- Evidence: Instance-aware ViT quantization experiments.

## What it establishes

Predicts deeper-layer scales from shallow activation-range statistics using a learned polynomial projection.

## Relevance to our goals

Close prior art for causal prediction from information available earlier in a forward pass.

## Limits and transfer conditions

A learned predictor is not automatically hardware-autonomous or portable across models. Our target needs explicit state, arithmetic, buffering, and distribution-shift evaluation.
