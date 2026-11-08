# Where Do the Joules Go? Diagnosing Inference Energy Consumption

- Citation key: `chung2026joules`.
- Authors: Chung, Jae-Won; Wu, Ruofan; Ma, Jeff J.; Chowdhury, Mosharaf.
- Publication: arXiv preprint, 2026.
- Source: [paper](https://arxiv.org/abs/2601.22076v2); [full text reviewed](https://arxiv.org/pdf/2601.22076v2).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Sections 2–5, especially batch size, FP8 comparisons, and latency constraints.
- Evidence: H100/B200 measurements: 46 models, seven tasks, 1,858 configurations.

## What it establishes

In its H100 FP8/BF16 comparison, FP8 consumes more energy in all seven reported small-batch comparisons (batch 8–16). Larger batches often reverse the result as overhead and utilization change.

## Relevance to our goals

Strong motivation to measure total energy and controller/conversion overhead rather than assuming lower precision always wins.

## Limits and transfer conditions

This is serving-stack evidence, not circuit-level attribution. Precision variants and software paths can differ; it does not isolate activation quantization alone or establish an NPU energy split.
