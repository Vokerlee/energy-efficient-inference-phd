# DINOv3

- Citation key: `simeoni2025dinov3`.
- Authors: Oriane Siméoni; Huy V. Vo; Maximilian Seitzer; Federico Baldassarre; Maxime Oquab; and colleagues.
- Publication: author report, 2025; reviewed version `2508.10104v1`.
- Source: [paper](https://arxiv.org/abs/2508.10104v1); [full text](https://arxiv.org/html/2508.10104v1); [official implementation](https://github.com/facebookresearch/dinov3).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Reading focus: Sections 3.2, 5.2 and 7.1: transformer architecture, distilled family and global/dense evaluation.

## What it establishes

Provides self-supervised vision backbones, including distilled ViT and ConvNeXt
variants. Distinguishes global descriptors and dense patch representations;
downstream classification and dense tasks use their corresponding evaluation
protocols rather than treating every backbone as a pretrained classifier.

## Relevance to our goals

A modern vision workload for numerical changes to large projection/MLP
products, with feature-level and downstream evaluation requirements. Pinned
small-model checkpoints allow portable experiments before simulator work.

## Limits and transfer conditions

An embedding similarity measurement is not classification or segmentation
accuracy. The teacher's scale, outlier behavior and training settings do not
automatically describe every distilled checkpoint. Model FLOPs alone do not
identify target-array energy; record actual shapes, precision and operator
coverage at the chosen resolution.
