# Error Diffusion: Post Training Quantization with Block-Scaled Number Formats for Neural Networks

- Citation key: `khodamoradi2024ed`.
- Authors: Alireza Khodamoradi; Kristof Denolf; Eric Dellinger.
- Publication: 2024.
- Source: [record](https://arxiv.org/abs/2410.11203v1); [reviewed text](https://arxiv.org/html/2410.11203v1).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Reading focus: Sections 2–4 and 8: inherited DAG errors, calibration updates, block-scale direction and limitations.

## What it establishes

Uses calibration inputs to update quantized weights while accounting for errors inherited from previous layers. Also updates layers retained at higher precision. Supports block-scaled formats and provides the TensorCast emulator.

## Relevance to our goals

A concrete comparator for distinguishing local quantization error from error propagated through a model DAG.

## Limits and transfer conditions

Hyperparameter-free does not mean calibration-free: sample activations and weight adjustments are part of the method. Its diffusion operates during model preparation, rather than serving as a demonstrated live source-activation feedback controller. Hardware implementation remains a separate contribution, with preparation and execution costs distinguished.
