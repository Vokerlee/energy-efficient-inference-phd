# HAP: Efficient Quantization Harnessing Adaptive Precision for DNN Hardware Acceleration

- Citation key: `luo2026hap`.
- Authors: Erjing Luo; Xinkuang Geng; Honglan Jiang; Leibo Liu; Jie Han.
- Source: [primary source](https://www.ece.ualberta.ca/~jhan8/publications/DAC2026_Camera_Ready.pdf).
- Publication: DAC2026; DOI10.1145/3770743.3804255.
- Reviewed: 2026-11-24. Status: **primary full-text focused reading**.
- Reading focus: Sections3.1–3.2 and4.1–4.3; evaluation not reproduced.

## What it establishes

Losslessly narrows existing activation integer codes with a per-group dynamic
zero point. Uses intra-channel grouping, outer-product reordering, bounded
register pages and a bit-serial array. Dynamic zero-point correction is computed
and scheduled explicitly rather than assumed free.

## Relevance and limits

Activation precision variability, bounded matching and the extra correction
path already have a dedicated hardware treatment. Initial affine quantization
uses calibrated intervals; enablement of the dynamic zero-point is profiled.
Lossless narrowing of those codes is distinct from calibration-free conversion
of arbitrary BF16 source groups. Bit-serial scheduling and its cycle equation
cannot be transferred directly to a BF16/FP8 array. Reordering preserves real
algebra, not every floating-point accumulation order.
