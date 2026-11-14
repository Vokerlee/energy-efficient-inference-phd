# QBitOpt: Fast and Accurate Bitwidth Reallocation during Training

- Citation key: `peters2023qbitopt`.
- Authors: Peters, Jorn; Fournarakis, Marios; Nagel, Markus; van Baalen, Mart; Blankevoort, Tijmen.
- Publication: ICCV Workshops, 2023; author preprint version 1 reviewed.
- Source: [paper](https://arxiv.org/abs/2307.04535v1); [full text](https://arxiv.org/html/2307.04535v1); [venue record](https://openaccess.thecvf.com/ICCV2023_workshops/RCV).
- Reviewed: 2026-11-15. Status: **full-text focused reading**.
- Reading focus: Sections 3.1–3.3 and Appendix A: sensitivities, allocation, and activation extension.
- Evidence: Constrained allocation during QAT; not reproduced here.

## What it establishes

QBitOpt updates bitwidth allocations during quantization-aware training using
sensitivity estimates and explicit resource constraints. Squared-gradient
estimates are smoothed over training iterations. Appendix A formulates
activation sensitivity through the downstream subnetwork's loss Hessian.

## Relevance to our goals

A baseline for prepared sensitivity and allocation. Sensitivity-based activation
precision cannot be treated as a new idea by itself.

## Limits and transfer conditions

Training-time allocation is distinct from a causal per-block inference policy.
Appendix A leaves separate activation/parameter constraint investigation open.
Resource-constraint satisfaction does not guarantee task quality or measured
energy; account for preparation and distinguish QAT from post-training methods.
