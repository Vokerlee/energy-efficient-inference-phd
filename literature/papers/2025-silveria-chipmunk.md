# Chipmunk: Training-Free Acceleration of Diffusion Transformers with Dynamic Column-Sparse Deltas

- Citation key: `silveria2025chipmunk`.
- Authors: Silveria, Austin; Govande, Soham V.; Fu, Daniel Y..
- Publication: arXiv preprint, 2025; version 1.
- Source: [paper](https://arxiv.org/abs/2506.03275v1); [full text](https://arxiv.org/html/2506.03275v1).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Sections 3.2–3.3 and Appendix C, Algorithms 5–7.

## What it establishes

Recomputes selected column-chunk deltas and caches other contributions. Tokens in each chunk share indices; kernels gather retained channels into dense tiles. Algorithm 7 multiplies chunk-mean inputs by weights to predict MLP changes.

## Relevance to our goals

Grouped masks, compaction and temporal reuse already occur together. The extra prediction product must be charged even though it is smaller than the full operation.

## Limits and transfer conditions

Reviewed kernels use a fixed chunk size and temporal state. GPU timings do not prove systolic energy gains. Full-model quality and cache/selection costs remain necessary; reported results were not reproduced.
