# Prox: Training-Free FFN Activation Sparsity via Approximate Intermediate-Channel Salience in LLMs

- Citation key: `liu2026prox`.
- Authors: Liu, Jinyi; Chen, Wei; Chen, Pengyu; Yuan, Xinyi; Bai, Minghe; Wu, Guoquan; Wei, Jun.
- Publication: arXiv preprint, 2026; version 1.
- Source: [paper](https://arxiv.org/abs/2607.27591v1); [full text](https://arxiv.org/html/2607.27591v1).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Section 4, limitation paragraph and Appendix A.7.

## What it establishes

A quantized proxy computes approximate intermediate-channel importance, then selected SwiGLU channels are recomputed with original weights. One mask spans up/gate/down projections; thresholds are calibrated and fixed during inference.

## Relevance to our goals

An important example of sparsity plus quantization and of paying extra computation to avoid more expensive work.

## Limits and transfer conditions

The shared mask links projections; it does not by itself mean a common mask across many tokens. Primary scope is single-batch decoding. Proxy matrix operations, extra weights and calibration distinguish it from a reduction-only selector; energy benefits require separate evidence.
