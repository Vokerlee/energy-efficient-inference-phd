# SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features

- Citation key: `tschannen2025siglip2`.
- Authors: Tschannen, Michael; Gritsenko, Alexey; Wang, Xiao; and colleagues.
- Publication: arXiv author version, 2025; `2502.14786v1` reviewed.
- Source: [paper](https://arxiv.org/abs/2502.14786v1); [official checkpoint](https://huggingface.co/google/siglip2-base-patch16-224).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Section 2.1 and official model-card task protocol.

## What it establishes

Fixed-resolution encoders use a standard ViT with attention pooling; NaFlex supports varying sequence lengths and aspect ratios. The paper evaluates zero-shot classification and retrieval.

## Relevance to our goals

A frozen model family with final-task metrics for testing changes to vision activations.

## Limits and transfer conditions

Vision-tower size is not total vision-language checkpoint size. Preserve pooling, preprocessing, label prompts and text embeddings in comparisons. Published architecture and scores do not establish new quantization/sparsity headroom or local GPU memory fit.
