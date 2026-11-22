# NVIDIA Transformer Engine: FP8 Delayed Scaling

- Citation key: `nvidia2026delayedscaling`.
- Author: NVIDIA.
- Publication: official technical documentation; page identifies Transformer Engine 2.21.0, accessed 2026-11-22.
- Source: [official documentation](https://docs.nvidia.com/deeplearning/transformer-engine/features/low_precision_training/fp8_delayed_scaling/fp8_delayed_scaling.html).
- Reviewed: 2026-11-22. Status: **official documentation focused reading**.
- Reading focus: quantization process, current/delayed comparison and history management.

## What it establishes

Delayed scaling uses past maxima, casts with the chosen scale and records the current maximum for later updates. The documented tensor-level path contrasts one read with current scaling's two reads; out-of-range values are clipped.

## Relevance to our goals

An established historical-range baseline; predicting a scale or avoiding an amax scan alone is not new.

## Limits and transfer conditions

The documented training/library path is not an autonomous inference-chip policy. Its tensor-scan comparison does not prove that a producer with small local groups needs two expensive memory passes. It does not claim current-scale numerical equivalence. Page content is access-dated rather than an immutable artifact.
