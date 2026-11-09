# Sparseloop: An Analytical Approach To Sparse Tensor Accelerator Modeling

- Citation key: `wu2022sparseloop`.
- Authors: Wu, Yannan Nellie; Tsai, Po-An; Parashar, Angshuman; Sze, Vivienne; Emer, Joel S..
- Publication: MICRO, 2022.
- Source: [paper](https://arxiv.org/abs/2205.05826v3); [full text reviewed](https://arxiv.org/pdf/2205.05826v3).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Representation, gating/skipping taxonomy, density models, and validation.
- Evidence: Analytical model validated against selected sparse accelerators; expanded arXiv version.

## What it establishes

Models sparse-format overhead and distinguishes gating from skipping while estimating action counts using density models.

## Relevance to our goals

A method for testing whether sparsity avoids cycles, traffic, or only switching.

## Limits and transfer conditions

Validation on selected patterns does not guarantee accuracy for correlated runtime activation masks. New metadata and control actions need explicit characterization.
