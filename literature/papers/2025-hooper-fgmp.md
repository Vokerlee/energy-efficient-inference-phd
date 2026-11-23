# FGMP: Fine-Grained Mixed-Precision Weight and Activation Quantization for Hardware-Accelerated LLM Inference

- Citation key: `hooper2025fgmp`.
- Authors: Hooper, Coleman; Sakr, Charbel; Keller, Ben; Venkatesan, Rangharajan; Keutzer, Kurt; Shao, Sophia; Khailany, Bruce.
- Publication: arXiv preprint, 2025; version 1 reviewed.
- Source: [paper](https://arxiv.org/abs/2504.14152v1); [full text](https://arxiv.org/html/2504.14152v1).
- Reviewed: 2026-11-15. Status: **full-text focused reading**.
- Reading focus: Sections 3.1–3.4 and 4.1–4.2: preparation, live assignment, and datapath.
- Evidence: Online activation PPU; SystemC/HLS-generated RTL, simulation and 5-nm synthesis/activity-based power. Results not reproduced here.

## What it establishes

Prepared per-channel squared-gradient averages weight the live difference
between high- and low-precision activation reconstructions. A calibrated
threshold selects each block's format. The post-processing quantizer writes
FP8 or NVFP4 blocks; a VMAC design supports the operand-format pairs.
Its alternative local-output score uses other-operand second moments.

## Relevance to our goals

Direct prior art for sensitivity-aware online activation precision and hardware
selection. Compare against its prepared sensitivity and threshold baselines.

## Limits and transfer conditions

The diagonal surrogate uses statistical assumptions, not a task-quality
certificate. Its VMAC keeps throughput constant across formats; do not infer
systolic speedup from lower bits. Separate activation effects from prepared
weight changes and charge statistics, metadata, scaling, and control.

Section3.4 additionally weights coordinate-wise activation reconstruction errors
by receiving-weight second moments. Its baseline threshold is a dynamic
within-layer percentile, unlike the primary policy's calibrated global
threshold. A coarse group-moment surrogate is not an exact reproduction of
this channel-weighted baseline.
