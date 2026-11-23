# DeepSeek-V4: Towards Highly Efficient Million-Token Context Intelligence

- Citation key: `deepseek2026v4`.
- Authors: DeepSeek-AI.
- Publication: author report, 2026; reviewed version `2606.19348v1`.
- Source: [report](https://arxiv.org/abs/2606.19348v1); [reviewed text](https://arxiv.org/html/2606.19348v1).
- Reviewed: 2026-11-23. Status: **full-text focused reading of Section 5.2.1 only**.
- Reading focus: lossless FP4-to-FP8 widening during quantization-aware training, not a review of the complete model.

## What it establishes

Describes losslessly absorbing fine FP4 subblock scales into a wider FP8
representation when scale ratios inside the receiving block permit it. Applies
this to expert-weight simulation in a QAT pipeline; inference uses native
quantized weights. Model training is part of its workflow.

## Relevance to our goals

Direct prior art for lossless scale absorption and wider-format reuse. These
general operations cannot be claimed as new merely by moving between low-bit
source storage and a wider matrix input interface.

## Limits and transfer conditions

The reviewed section concerns prepared weights and FP8 representability.
It does not establish a live activation INT8-lane selector, a photonic input
contract or the cost of buffering mixed-scale convolution sources. Conversely,
those distinctions alone do not prove a new hardware contribution. Exact
representation transfer also does not guarantee identical accumulation order.
