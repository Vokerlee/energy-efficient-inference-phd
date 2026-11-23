# TFMQ-DM: Temporal Feature Maintenance Quantization for Diffusion Models

- Citation key: `huang2024tfmq`.
- Authors: Huang, Yushi; Gong, Ruihao; Liu, Jing; Chen, Tianlong; Liu, Xianglong.
- Publication: CVPR 2024; author version 2311.16503v3.
- Source: [focused full text](https://arxiv.org/html/2311.16503v3).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Focus: Sections4.1–4.3 and5.1: temporal sensitivity, block reconstruction and finite-set calibration.

## Findings, relevance and limits

Time embeddings can perturb the denoising trajectory disproportionately. The method isolates a Temporal Information Block, adjusts its weights against a temporal-feature reconstruction objective, and calibrates separate activation parameters for finite timesteps. This establishes temporal-feature protection as prior art.

Its model-specific preparation and timestep calibration differ from a calibration-free live source-statistics controller. A shape-only high-precision fallback is not a reproduction. The finite-timestep/sample-independence assumptions require rechecking for continuous-time samplers and conditional embeddings. No reported quality or efficiency result was reproduced here.
