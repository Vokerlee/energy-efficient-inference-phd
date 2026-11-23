# Noise-Shaping Quantization Harmonized by Training Data for Compaction of Neural Networks

- Citation key: `tsubone2024noiseshaping`.
- Authors: Tsubone, Naoki; Minami, Yuki; Ishikawa, Masato.
- Publication: Transactions of the Institute of Systems, Control and Information Engineers37(10),257–264,2024; J-STAGE release2025-01-15.
- Source: [publisher record and English abstract](https://www.jstage.jst.go.jp/article/iscie/37/10/37_257/_article/-char/en); [DOI](https://doi.org/10.5687/iscie.37.257).
- Reviewed: 2026-11-23. Status: **primary English abstract/metadata only; full-text review pending**.

## Findings, relevance and limits

The abstract describes quantizing trained network weights while distributing the resulting error over coefficients not yet quantized. Training data determine the magnitude of that redistribution. Image classification is the reported validation setting; the authors relate the method to time-signal quantization in dynamic systems.

This is additional neural-network prior art for data-dependent noise shaping. Distinguish prepared weight updates from live activation feedback, calibration data from current inference statistics, and amplitude adaptation from a proven hardware controller. The abstract does not establish the exact filter, state, information deadline or fixed-point realization. Do not infer that adaptive noise shaping is new, or that this work covers every causal source-activation implementation. No results were reproduced here.
