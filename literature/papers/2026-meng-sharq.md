# SharQ: Bridging Activation Sparsity and FP4 Quantization for LLM Inference

- Citation key: `meng2026sharq`.
- Authors: Meng, Haoqian; Luo, Yilun; Zhao, Yafei; Liu, Wenyuan; Zheng, Huaqing; Ma, Xindian; Zhang, Peng.
- Publication: arXiv preprint, 2026.
- Source: [paper](https://arxiv.org/abs/2606.26587v1); [full text reviewed](https://arxiv.org/pdf/2606.26587v1).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Online decomposition, quantized-backbone residual, preparation fusion, and evaluations.
- Evidence: GPU implementation with language, multimodal, and video-generation tests.

## What it establishes

Uses an input-adaptive N:M sparse FP4 backbone and a dense FP4 residual that compensates for masking and backbone quantization.

## Relevance to our goals

Close existing prior art for jointly exploiting runtime activation structure and low precision.

## Limits and transfer conditions

Both paths use FP4; this is not simply a sparse high-precision exception path. GPU speedups do not establish custom-array energy or eliminate preparation costs.
