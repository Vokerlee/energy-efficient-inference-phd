# MXDOTP: A RISC-V ISA Extension for Enabling Microscaling (MX) Floating-Point Dot Products

- Citation key: `islamoglu2025mxdotp`.
- Authors: Islamoglu, Gamze; Bertaccini, Luca; Prasad, Arpan Suravi; Conti, Francesco; Garofalo, Angelo; Benini, Luca.
- Publication: ASAP; author preprint reviewed, 2025.
- Source: [paper](https://arxiv.org/abs/2505.13159v1); [full text reviewed](https://arxiv.org/pdf/2505.13159v1).
- Reviewed: 2026-11-14. Status: **full-text focused reading**.
- Reading focus: Section III: eight-element datapath, early accumulation, fixed-point width, and FP32 rounding.
- Evidence: ISA/datapath design and implementation-based cluster/kernel evaluation.

## What it establishes

Combines scaled FP8 products and the shifted accumulator before final FP32 conversion, using a wide fixed-point intermediate.

## Relevance to our goals

Shows that narrow input representations can require substantial internal precision and explicit scale handling.

## Limits and transfer conditions

Its fixed arithmetic contract is not runtime accumulator adaptation. Eight-element issue width is not automatically the quantization-group size; software-conversion baselines differ from native array execution.
