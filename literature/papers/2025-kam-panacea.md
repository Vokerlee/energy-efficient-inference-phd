# Panacea: Novel DNN Accelerator using Accuracy-Preserving Asymmetric Quantization and Energy-Saving Bit-Slice Sparsity

- Citation key: `kam2025panacea`.
- Authors: Kam, Dongyun; Yun, Myeongji; Yoo, Sunwoo; Hong, Seungwoo; Zhang, Zhengya; Lee, Youngjoo.
- Publication: HPCA, 2025.
- Source: [paper](https://arxiv.org/abs/2412.10059v1); [full text reviewed](https://arxiv.org/pdf/2412.10059v1).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Asymmetric codes, frequent slices, compensation, and tiled dataflow.
- Evidence: Algorithm/accelerator evaluation.

## What it establishes

Exploits frequent bit slices under asymmetric quantization using specialized compression and compensation rather than only skipping zero slices.

## Relevance to our goals

Shows that representation choice and exploitable bit structure must be co-designed.

## Limits and transfer conditions

Calibrated representation transformations and specialized hardware are not a free autonomous activation policy. Zero-point and compensation costs must remain explicit.
