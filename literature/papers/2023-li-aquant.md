# Efficient Adaptive Activation Rounding for Post-Training Quantization

- Citation key: `li2023aquant`.
- Authors: Li, Zhengyi; Guo, Cong; Zhu, Zhanda; Zhou, Yangjie; Qiu, Yuxian; Gao, Xiaotian; Leng, Jingwen; Guo, Minyi.
- Publication: arXiv preprint; initially 2022, version 3 dated 2023 reviewed.
- Source: [paper](https://arxiv.org/abs/2208.11945v3); [full text](https://arxiv.org/html/2208.11945v3).
- Reviewed: 2026-11-15. Status: **full-text focused reading**.
- Reading focus: Sections 3–4: output-error objective and practical border function.
- Evidence: Rounding analysis and calibrated quantization method; not reproduced here.

## What it establishes

AQuant replaces a constant rounding threshold with an activation-dependent
border. Coarse sharing across a weight column lets each activation be rounded
once for reuse across output channels. Border parameters are learned during
calibration alongside other quantization parameters.

## Relevance to our goals

Output-error-aware activation quantization is established prior art. Rounding
adaptation is a useful comparator to changing precision or range.

## Limits and transfer conditions

This changes rounding rather than selecting a live bitwidth. Its ideal
elementwise analysis includes distribution assumptions; coarse calibration is
not a universal unbiased-error guarantee. Separate rounding improvements from
weight optimization and include border evaluation and conversion costs.
