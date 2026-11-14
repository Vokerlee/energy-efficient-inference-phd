# PIVOT: Input-aware Path Selection for Energy-efficient ViT Inference

- Citation key: `moitra2024pivot`.
- Authors: Moitra, Abhishek; Bhattacharjee, Abhiroop; Panda, Priyadarshini.
- Publication: DAC; author preprint reviewed, 2024.
- Source: [paper](https://arxiv.org/abs/2404.15185v1); [full text reviewed](https://arxiv.org/pdf/2404.15185v1).
- Reviewed: 2026-11-14. Status: **full-text focused reading**.
- Reading focus: Sections 3.1–3.2: prediction entropy, second inference, offline path search.
- Evidence: Prepared ViT paths and FPGA/processor evaluation.

## What it establishes

Runs a low-effort attention-skipping model, then uses prediction entropy to decide whether to run a higher-effort model.

## Relevance to our goals

A controller baseline for using available outputs and explicitly paying fallback recomputation.

## Limits and transfer conditions

The model is prepared through search/training. Prediction entropy is a confidence proxy, and path skipping differs from activation quantization or within-layer sparse attention.
