# FuSeConv: Fully Separable Convolutions for Fast Inference on Systolic Arrays

- Citation key: `selvam2021fuseconv`.
- Authors: Selvam, Surya; Ganesan, Vinod; Kumar, Pratyush.
- Publication: DATE, 2021.
- Source: [paper](https://arxiv.org/abs/2105.13434v1); [full text reviewed](https://arxiv.org/pdf/2105.13434v1).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Depthwise mapping, operator replacement, and quality evaluation.
- Evidence: Operator/hardware co-design with network training and systolic evaluation.

## What it establishes

Replaces depthwise convolution with separable computations designed for improved systolic mapping and modified dataflow.

## Relevance to our goals

Explains why short channel-wise reductions can underutilize a conventional array despite a low logical operation count.

## Limits and transfer conditions

It changes the network operator and requires training. Treat it separately from an exact im2col implementation or post-training activation policy.
