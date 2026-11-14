# SQ-DM: Accelerating Diffusion Models with Aggressive Quantization and Temporal Sparsity

- Citation key: `fan2025sqdm`.
- Authors: Fan, Zichen; Dai, Steve; Venkatesan, Rangharajan; Sylvester, Dennis; Khailany, Brucek.
- Publication: arXiv preprint, 2025.
- Source: [paper](https://arxiv.org/abs/2501.15448v1); [full text reviewed](https://arxiv.org/html/2501.15448v1).
- Reviewed: 2026-11-14. Status: **full-text focused reading**.
- Reading focus: Sections III–IV: calibrated bitwidths, ReLU fine-tuning, channel classification, dense/sparse datapaths.
- Evidence: Modified-model quality evaluation and simulated hardware design.

## What it establishes

Combines mixed-precision quantization with ReLU-promoted activation sparsity and live per-channel routing to dense or sparse engines.

## Relevance to our goals

A direct joint-policy comparison requiring separation of offline precision choices from online sparsity detection.

## Limits and transfer conditions

Replacing SiLU and fine-tuning changes the checkpoint. Sparse-path gains cannot be attributed solely to a detector on unchanged pretrained activations.
