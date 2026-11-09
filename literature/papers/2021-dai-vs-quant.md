# VS-Quant: Per-vector Scaled Quantization for Accurate Low-Precision Neural Network Inference

- Citation key: `dai2021vsquant`.
- Authors: Dai, Steve; Venkatesan, Rangharajan; Ren, Haoxing; Zimmer, Brian; Dally, William J.; Khailany, Brucek.
- Publication: MLSys, 2021.
- Source: [paper](https://arxiv.org/abs/2102.04503v1); [full text reviewed](https://arxiv.org/pdf/2102.04503v1).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Vector grouping, two-level scales, and accelerator overhead.
- Evidence: Inference-quality experiments and hardware cost evaluation.

## What it establishes

Uses small vectors with separate scales and a two-level scale representation to improve low-precision inference.

## Relevance to our goals

A baseline for scale granularity and hardware support while keeping activation adaptation central.

## Limits and transfer conditions

Group-wise scaling already exists. Distinguish calibration, runtime scale generation, and variable precision; this paper does not establish that our proposed autonomous policy is new.
