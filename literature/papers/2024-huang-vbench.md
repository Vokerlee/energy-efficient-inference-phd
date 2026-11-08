# VBench: Comprehensive Benchmark Suite for Video Generative Models

- Citation key: `huang2024vbench`.
- Authors: Huang, Ziqi; others.
- Publication: CVPR, 2024.
- Source: [paper](https://arxiv.org/abs/2311.17982v1); [full text reviewed](https://arxiv.org/pdf/2311.17982v1).
- Reviewed: 2026-11-09. Status: **full-text focused reading**.
- Reading focus: Quality dimensions, prompts, and human-alignment evaluation.
- Evidence: Video-generation benchmark design and validation.

## What it establishes

Separates video quality into dimensions including consistency, motion, and temporal artifacts.

## Relevance to our goals

Prevents evaluating video inference only with image-level or single-frame metrics.

## Limits and transfer conditions

Automatic metrics are imperfect proxies. Pin the benchmark implementation and report dimensions rather than hiding regressions in one aggregate score.
