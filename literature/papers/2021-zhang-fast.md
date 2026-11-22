# FAST: DNN Training Under Variable Precision Block Floating Point with Stochastic Rounding

- Citation key: `zhang2021fast`.
- Authors: Sai Qian Zhang; Bradley McDanel; H. T. Kung.
- Publication: 2021; author version `2110.15456v1`.
- Source: [paper](https://arxiv.org/abs/2110.15456v1); [full text](https://arxiv.org/html/2110.15456v1).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Reading focus: Sections III–V: BFP dot products, live precision criterion and fMAC systolic execution.

## What it establishes

Selects BFP mantissa precision from a relative quantization-improvement criterion during training. A variable-precision fMAC executes higher mantissa widths through additional small-bit passes in a systolic engine.

## Relevance to our goals

Established live precision decisions coupled to a native arithmetic implementation, with explicit conversion and multi-pass work.

## Limits and transfer conditions

Training strategy, gradient rounding and changing model parameters differ from fixed-weight inference. Additional bit passes are actual work. Neither BFP support alone nor live precision alone establishes a new inference mechanism; compare decision cadence and full operator costs.
