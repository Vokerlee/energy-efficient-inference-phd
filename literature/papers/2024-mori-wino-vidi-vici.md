# Wino Vidi Vici: Conquering Numerical Instability of 8-Bit Winograd Convolution for Accurate Inference Acceleration on Edge

- Citation key: `mori2024wino`.
- Authors: Pierpaolo Mori; Lukas Frickenstein; Shambhavi Balamuthu Sampath; Moritz Thoma; Nael Fasfous; Manoj Rohit Vemparala; Alexander Frickenstein; Christian Unger; Walter Stechele; Daniel Mueller-Gritschneder; Claudio Passerone.
- Publication: WACV 2024.
- Source: [primary source](https://openaccess.thecvf.com/content/WACV2024/html/Mori_Wino_Vidi_Vici_Conquering_Numerical_Instability_of_8-Bit_Winograd_Convolution_WACV_2024_paper.html).
- Reviewed: 2026-11-24. Status: **Primary indexed abstract and Section3.3 excerpts; direct publisher fetch returned HTTP403. Full paper not read.**

## Contribution and relevance

Addresses numerical instability in quantized Winograd execution. The inspected clipping-factor passage adjusts activation/weight factors through gradient descent training, then applies prepared scaling during inference.

## Comparison boundary

Dynamically adjustable during training is distinct from a causal hardware rule observing each current activation block. Do not infer exact hardware implementation or energy gains from the inspected excerpts.
