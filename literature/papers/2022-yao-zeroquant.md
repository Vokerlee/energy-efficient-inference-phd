# ZeroQuant: Efficient and Affordable Post-Training Quantization for Large-Scale Transformers

- Citation key: `yao2022zeroquant`.
- Authors: Yao, Zhewei; Yazdani Aminabadi, Reza; Zhang, Minjia; Wu, Xiaoxia; Li, Conglong; He, Yuxiong.
- Publication: NeurIPS, 2022.
- Source: [paper](https://arxiv.org/abs/2206.01861v1); [full text reviewed](https://arxiv.org/pdf/2206.01861v1).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Token-wise activation quantization and optimized execution backend.
- Evidence: GPU quantization implementation, model quality, and latency evaluation.

## What it establishes

Combines group-wise weights, token-wise activations, optional distillation, and backend optimization to manage quantization overhead.

## Relevance to our goals

A software-executed runtime baseline against which a hardware-autonomous mechanism must be distinguished.

## Limits and transfer conditions

Runtime quantization is not necessarily hardware-autonomous decision-making. Distillation and weight changes must be controlled in an activation-only comparison.
