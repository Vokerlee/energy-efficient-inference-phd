# PixArt-Sigma: Weak-to-Strong Training of Diffusion Transformer for 4K Text-to-Image Generation

- Citation key: `chen2024pixartsigma`.
- Authors: Chen, Junsong; Ge, Chongjian; Xie, Enze; and colleagues.
- Publication: arXiv author version, 2024; `2403.04692v1` reviewed.
- Source: [paper](https://arxiv.org/abs/2403.04692v1); [official checkpoint](https://huggingface.co/PixArt-alpha/PixArt-Sigma-XL-2-1024-MS).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Section 3.2 and official model card.

## What it establishes

Describes a 0.6B diffusion transformer and spatial key/value compression for high-resolution generation while retaining query tokens. Conditioning uses a separate text encoder and latent autoencoder.

## Relevance to our goals

A reproducible diffusion family with explicit attention, projection and conditioning boundaries.

## Limits and transfer conditions

Compression is architecture/checkpoint-dependent. Inspect actual configuration rather than assigning equal query/key lengths from the paper title. Denoiser-only measurements exclude text encoding and decoding; offload and cached conditioning must be disclosed. No energy or approximation result was reproduced.
