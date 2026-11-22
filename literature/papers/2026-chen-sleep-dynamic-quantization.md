# A Mixed-Precision CNN-LSTM Accelerator Featuring Long-Kernel Memory Reuse and Dynamic Quantization for Sleep Staging

- Citation key: `chen2026sleepdynamic`.
- Authors: Xinyu Chen; Yaqian Xu; Yuhan Hou; Bowen Liu; Andrew G. Richardson; Xilin Liu.
- Publication: 2026.
- Source: [paper](https://arxiv.org/abs/2611.00660v1); [reviewed text](https://arxiv.org/html/2611.00660v1).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Reading focus: Sections III-A–III-C and IV: serpentine reuse, online observer scope, bit-flexible MACs and measured ASIC.

## What it establishes

Combines temporal-convolution reuse, bit-flexible arithmetic and packed channel scheduling in a fabricated accelerator. CNN activation ranges remain calibrated; LSTM/MLP input ranges are measured online, with state reset per inference.

## Relevance to our goals

Hardware reuse plus dynamic quantization already exists; identify which layers, parameters and runtime choices actually adapt.

## Limits and transfer conditions

Layer bit widths are prepared rather than selected independently for every live tile. Long EEG convolutions and a small PE array are not short-window image inference. The paper calls the observer a histogram observer but describes extrema-based range updates; histogram computation should not be assumed from the label alone.
