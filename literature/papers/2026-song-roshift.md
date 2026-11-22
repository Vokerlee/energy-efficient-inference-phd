# RoShift: Lazy Shift and Weight-aware Rotation for Activation Sparsity in LLM Inference

- Citation key: `song2026roshift`.
- Authors: Song, Geunsoo; Seo, Jiwon; Yang, Hoeseok; Yi, Youngmin.
- Publication: arXiv author version, 2026; `2611.20549v1` reviewed.
- Source: [paper](https://arxiv.org/abs/2611.20549v1); [full text](https://arxiv.org/html/2611.20549v1).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Weight-aware selection, Appendix A rotation construction and implementation discussion.

## What it establishes

Combines calibrated activation covariance and receiving-weight Gram information to prepare rotations. Runtime weight-aware selection and correction fusion exploit the transformed activations.

## Relevance to our goals

Receiving-weight geometry and shared-projection Gram objectives already appear in activation-sparsity research.

## Limits and transfer conditions

The reviewed geometry informs prepared rotations, rather than establishing every bounded local runtime mask evaluator. Calibration, basis transitions, transformed weights and correction must be counted. Removing a rotation is not by itself a novel algorithm.
