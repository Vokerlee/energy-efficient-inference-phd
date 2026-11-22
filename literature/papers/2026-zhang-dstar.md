# DSTAR: Accelerating Diffusion Transformers via Spatial and Temporal Redundancy Reduction

- Citation key: `zhang2026dstar`.
- Authors: Zhang, Chi; Zhao, Jieru; Feng, Yu; Zhang, Chen; Chen, Quan; Guo, Minyi.
- Publication: arXiv preprint, 2026; pinned author version.
- Source: [paper](https://arxiv.org/abs/2607.15846v1); [full text](https://arxiv.org/html/2607.15846v1).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Sections 3.1–3.2, 4 and 5.1.

## What it establishes

Selects 2/4/6/8-bit differential-activation groups from live maxima. A dataset-profiled base and fixed thresholds avoid a global scale pass. Bit-slice reordering supports execution; attention uses profiled block masks and periodic reuse.

## Relevance to our goals

A close joint precision/sparsity/dataflow comparator. Live decisions coexist with prepared model-dependent parameters.

## Limits and transfer conditions

Simulation and hardware estimates are not silicon energy measurements. History, reordering, scaling and refresh have costs. Conference status was not independently verified; the reviewed arXiv version is the pinned source.
