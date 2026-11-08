# The ML.ENERGY Benchmark: Toward Automated Inference Energy Measurement and Optimization

- Citation key: `chung2025mlenergy`.
- Authors: Chung, Jae-Won; Ma, Jeff J.; Wu, Ruofan; Liu, Jiachen; Kweon, Oh Jun; Xia, Yuxuan; Wu, Zhiyu; Chowdhury, Mosharaf.
- Publication: Advances in Neural Information Processing Systems, Datasets and Benchmarks Track, 2025.
- Source: [paper](https://arxiv.org/abs/2505.06371v2); [full text reviewed](https://arxiv.org/pdf/2505.06371v2).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Measurement principles, phase-aware accounting, Sections 4.1–4.2, and limitations.
- Evidence: GPU inference-energy measurements across six generative tasks.

## What it establishes

Benchmarks 40 model architectures using realistic serving configurations. Shows that replacing measured power with TDP can overestimate energy substantially, reaching 4.1× in one reported case.

## Relevance to our goals

Provides reusable accounting concepts for batching, steady-state serving, diffusion requests, and time–energy comparisons.

## Limits and transfer conditions

GPU energy excludes parts of the host/platform. Steady-state per-request attribution is an allocation convention, not a direct measurement of each concurrent request's isolated causal cost.
