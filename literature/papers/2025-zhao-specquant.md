# SpecQuant: Spectral Decomposition and Adaptive Truncation for Ultra-Low-Bit LLMs Quantization

- Citation key: `zhao2025specquant`.
- Authors: Zhao, Zhixiong; Liu, Fangxin; Wang, Junjie; Guan, Chenyang; Wang, Zongwu; Jiang, Li; Guan, Haibing.
- Publication: arXiv preprint, 2025; version 1 reviewed.
- Source: [paper](https://arxiv.org/abs/2511.11663v1); [full text](https://arxiv.org/html/2511.11663v1).
- Reviewed: 2026-11-15. Status: **full-text focused reading**.
- Reading focus: Method, implementation details, and Appendix Algorithm 1.
- Evidence: Proposed spectral decomposition and quantized inference; not reproduced here.

## What it establishes

SpecQuant combines activation smoothing with a Fourier-derived weight branch
and a quantized residual branch. The main method allocates frequency retention
using activation–weight importance; Algorithm 1 instead uses spectral entropy.

## Relevance to our goals

A decomposition comparator for outlier handling. Spectral reconstruction of
weights is distinct from measuring activation error or selecting arithmetic
precision autonomously.

## Limits and transfer conditions

The allocation descriptions need reconciliation before reproducing the method.
The abstract's runtime-adaptivity claim alone does not establish a causal
hardware controller. Charge reconstruction and both branches. Smoothness
assumptions and spectral-energy bounds do not guarantee final task quality.
