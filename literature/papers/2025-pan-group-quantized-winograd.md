# Data-Free Group-Wise Fully Quantized Winograd Convolution via Learnable Scales

- Citation key: `pan2025groupwinograd`.
- Authors: Shuokai Pan; Gerti Tuzi; Sudarshan Sreeram; Dibakar Gope.
- Source: [primary source](https://arxiv.org/abs/2412.19867v2).
- Publication: CVPR2025; reviewed author version2, 2025-04-01.
- Reviewed: 2026-11-24. Status: **primary full-text focused reading**.
- Reading focus: Sections3–4, Algorithm1 and Appendix13; results not reproduced.

## What it establishes

Combines fully quantized Winograd with dynamic group min/max activation scales.
Balances transform-domain ranges using learned diagonal transform scales; one
scale set is optimized across layers using synthetic Gaussian or uniform inputs.
Includes optimized group-quantized matrix kernels and evaluates diffusion models.

## Relevance and limits

Winograd plus dynamic group quantization for diffusion is direct prior art.
Data-free here excludes natural calibration images but still includes offline
scale optimization; it is not autonomous current-tile transform selection.
CPU kernel/quality results do not establish this target array's energy, buffers
or output-interface cost. Removing domain-specific calibration does not alone
prove distribution-independent model fidelity. Runtime post-product encoding,
separate transform stages and learned preparation must be compared explicitly.
