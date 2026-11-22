# Regular-Activation Concentration: Characterizing Column-Level Output Sparsity Across Diffusion Model Architectures

- Citation key: `yang2026activationconcentration`.
- Authors: Yang, Dazhi; Anik, Shafayat Mowla; Lee, Byeong Kil; Ryoo, Jeeho.
- Publication: arXiv preprint, 2026; pinned author version.
- Source: [paper](https://arxiv.org/abs/2606.00567v1); [full text](https://arxiv.org/html/2606.00567v1).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Sections 2.3, 3.3, 4, 5.2–5.5 and discussion.

## What it establishes

Profiles thresholded GELU outputs across seven diffusion workloads. Scalar sparsity can substantially exceed entirely inactive-column sparsity. Uniform magnitude thresholds differ from calibrated per-layer target hot ratios; task quality can degrade sharply with threshold.

## Relevance to our goals

Evidence that activation sparsity must be evaluated at the execution granularity rather than by scalar zero counts.

## Limits and transfer conditions

Column skipping is a property of the evaluated FFN-Reuse mapping, not all systolic implementations. Cycle simulation uses a GDDR6-based memory system; its stalls/layout gains cannot be transferred to an on-chip hierarchy or called measured energy savings.
