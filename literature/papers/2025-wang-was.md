# Weight-Aware Activation Sparsity with Constrained Bayesian Optimization Scheduling for Large Language Models

- Citation key: `wang2025was`.
- Authors: Ming Wang; Miao Zhang; Xuebo Liu; Liqiang Nie.
- Publication: EMNLP 2025, pages 1086–1098.
- Source: [publisher](https://aclanthology.org/2025.emnlp-main.57/); [paper](https://aclanthology.org/2025.emnlp-main.57.pdf).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Sections 3.2–3.5.

## What it establishes

Derives activation importance from a receiving-weight L1-norm bound. Constrained Bayesian search allocates inter-block sparsity; greedy reconstruction allocates within blocks. A custom kernel includes weighted mask generation.

## Relevance to our goals

Weight-aware activation scoring and hardware-oriented execution are established beyond activation magnitude alone.

## Limits and transfer conditions

Sparsity allocation and threshold modeling use preparation/calibration. The norm surrogate does not preserve all signed cross terms. Decoder speedups are not evidence for energy savings on an independent systolic target. Experiments were not reproduced.
