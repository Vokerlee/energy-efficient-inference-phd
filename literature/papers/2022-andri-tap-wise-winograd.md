# Going Further With Winograd Convolutions: Tap-Wise Quantization for Efficient Inference on 4x4 Tiles

- Citation key: `andri2022tapwise`.
- Authors: Renzo Andri; Beatrice Bussolino; Antonio Cipolletta; Lukas Cavigelli; Zhe Wang.
- Publication: MICRO 2022; reviewed version `2209.12982v1`.
- Source: [full text](https://arxiv.org/html/2209.12982v1).
- Reviewed: 2026-11-24. Status: **full-text focused reading**, Sections III–IV, especially Listing 1 and producer/consumer rates.

## Contribution and relevance

Combines tap-wise power-of-two quantization with dedicated Winograd transforms
and software-managed matrix/vector/memory pipelines. Its quantization uses
training/calibration; it does not establish current-block, calibration-free
selection. Input-transform throughput, output-buffer capacity, fractal layouts
and transformed-weight delivery are explicit design constraints.

## Comparison boundary

A strong hardware comparator: adding Winograd to im2col or moving quantization
into a transform engine is insufficient as a novelty claim. Reproduce its
rate-matching logic before attributing savings to fewer products. Reported
hardware results are source claims, not independently reproduced here.
