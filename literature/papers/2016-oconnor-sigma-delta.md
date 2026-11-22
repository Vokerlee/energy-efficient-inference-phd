# Sigma Delta Quantized Networks

- Citation key: `oconnor2016sigmadelta`.
- Authors: Peter O'Connor; Max Welling.
- Publication: arXiv author version, 2016; `1611.02024v1` reviewed.
- Source: [paper](https://arxiv.org/abs/1611.02024v1); [full text](https://arxiv.org/html/1611.02024v1).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Sections 3.1–3.4, 4 and Appendix A.

## What it establishes

Combines temporal differences, stateful quantized emissions and accumulated linear responses. Delta-herding relates emitted differences to a rounded network. Scale optimization trades numerical error against update work.

## Relevance to our goals

Foundational prior art for sparse quantized temporal updates and retained rounding residuals. Error feedback is not a newly uncovered mechanism.

## Limits and transfer conditions

Equivalence has stated operator and numerical conditions. Temporal state, nonlinear updates and sparse execution still cost work. Prepared scale optimization differs from autonomous runtime policy. Arithmetic/update counts do not establish energy on a fixed-size systolic array or whole-model diffusion quality.
