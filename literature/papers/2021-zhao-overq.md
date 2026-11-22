# OverQ: Opportunistic Outlier Quantization for Neural Network Accelerators

- Citation key: `zhao2021overq`.
- Authors: Ritchie Zhao; Jordan Dotzel; Zhanqiu Hu; Preslav Ivanov; Christopher De Sa; Zhiru Zhang.
- Publication: 2021.
- Source: [paper](https://arxiv.org/abs/1910.06909v2); [reviewed text](https://arxiv.org/html/1910.06909v2).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Reading focus: Sections 3–5: range/precision overwrite, cascading, calibrated clipping and PE implementation.

## What it establishes

Reallocates nearby zero slots to activation range or precision bits, with cascading and weight-stationary systolic support. The evaluation profiles activation statistics on training images and sweeps clipping thresholds.

## Relevance to our goals

Using spare zero slots for outliers, including hardware routing, is existing work. Compare against it before proposing an im2col-tail variant.

## Limits and transfer conditions

The reviewed evaluation is not calibration-free. Its reliance on data zeros differs from known invalid input positions, but that distinction alone is not a new mechanism. No task-quality or target-energy result transfers automatically to GELU/SiLU models or a differently connected array.
