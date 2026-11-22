# Sana: Efficient High-Resolution Image Synthesis with Linear Diffusion Transformers

- Citation key: `xie2024sana`.
- Authors: Xie, Enze; Chen, Junsong; Chen, Junyu; and colleagues.
- Publication: arXiv author version, 2024; `2410.10629v1` reviewed.
- Source: [paper](https://arxiv.org/abs/2410.10629v1); [official checkpoint](https://huggingface.co/Efficient-Large-Model/Sana_600M_1024px).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Section 2.2, abstract deployment claim and official model card.

## What it establishes

Combines spatially compressed latents, ReLU linear attention and Mix-FFN with depthwise convolution. Linear attention forms reusable small products instead of a full quadratic token-interaction matrix.

## Relevance to our goals

An architectural contrast for checking whether a matrix optimization remains relevant after attention complexity changes.

## Limits and transfer conditions

Published deployment results are configuration-specific. The 600M checkpoint card contains a conflicting larger model-size description; verify configuration and actual parameters rather than copying prose. Do not assume a conventional two-linear MLP or free omission of depthwise operations.
