# Dither NN: Hardware/Algorithm Co-Design for Accurate Quantized Neural Networks

- Citation key: `ando2019dithernn`.
- Authors: Kota Ando; Kodai Ueyoshi; Yuka Oba; Kazutoshi Hirose; Ryota Uematsu; Takumi Kudo; Masayuki Ikebe; Tetsuya Asai; Shinya Takamaeda-Yamazaki; Masato Motomura.
- Publication: 2019.
- Source: [record](https://doi.org/10.1587/transinf.2019PAP0009); [reviewed text](https://www.jstage.jst.go.jp/article/transinf/E102.D/12/E102.D_2019PAP0009/_pdf).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Reading focus: Sections 3–6 and Appendix: spatial residual feedback, convolutional filtering, training and FPGA architectures.

## What it establishes

Diffuses activation quantization residuals spatially and adapts PE arithmetic/control to support the process. Tests trained/fine-tuned quantized models and FPGA resource overhead; the appendix discusses other quantization formats.

## Relevance to our goals

Spatial activation error feedback with a hardware implementation is established work, not an unexplored alternative to ordinary rounding.

## Limits and transfer conditions

Its accuracy experiments include modified training/backpropagation. They do not establish a calibration-free drop-in controller for every pretrained model. Kernel filtering, scan order, residual state and throughput are part of the mechanism; lower mean error alone does not guarantee task quality or lower energy.
