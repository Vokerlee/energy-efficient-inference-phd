# Quantization-Friendly Winograd Transformations for Convolutional Neural Networks

- Citation key: `protsenko2024winograd`.
- Authors: Vladimir Protsenko; Vladimir Kryzhanovskiy; Alexander Filippov.
- Publication: ECCV 2024.
- Source: [primary source](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/07548.pdf).
- Reviewed: 2026-11-24. Status: **Full-text focused reading, Sections3.1–3.2 and introduction; experiments not reproduced.**

## Contribution and relevance

Uses particle-swarm optimization over convolution-preserving transforms to reduce transform norms. The resulting initialization is model/data-free; the subsequent training pipeline can learn transforms for a network.

## Comparison boundary

Changing transform matrices or accounting for inverse-transform amplification is established. Separate model-independent offline initialization, network training and live activation decisions. The paper does not establish that arbitrary perturbations always amplify; cancellation remains possible.
