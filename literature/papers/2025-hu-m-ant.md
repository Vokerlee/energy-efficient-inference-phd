# M-ANT: Efficient Low-bit Group Quantization for LLMs via Mathematically Adaptive Numerical Type

- Citation key: `hu2025mant`.
- Authors: Weiming Hu; Haoyan Zhang; Cong Guo; Yu Feng; Renyang Guan; Zhendong Hua; Zihan Liu; Yue Guan; Minyi Guo; Jingwen Leng.
- Publication: HPCA 2025; DOI 10.1109/HPCA61900.2025.00086.
- Source: [author version](https://arxiv.org/html/2502.18755v1); [publisher](https://ieeexplore.ieee.org/document/10946714/).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: V-A–C, VI-C and VII-A.

## What it establishes

Weight coefficients are prepared; activations use streaming maximum-based INT8.
KV format selection uses live variance with calibrated mapping. Real-time
units exploit systolic output timing. Verilog components are synthesized;
whole-system evaluation combines simulation and memory estimates.

## Relevance to our goals

Online statistics and dedicated quantization hardware already coexist here.
Separate current activation conversion from prepared decisions and KV policy.

## Limits and transfer conditions

This evidence is not fabricated silicon or an arbitrary activation-mask policy.
Its LLM memory argument does not establish compute-heavy vision energy savings.
