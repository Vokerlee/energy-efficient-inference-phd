# OliVe: Accelerating Large Language Models via Hardware-friendly Outlier-Victim Pair Quantization

- Citation key: `guo2023olive`.
- Authors: Guo, Cong; Tang, Jiaming; Hu, Weiming; Leng, Jingwen; Zhang, Chen; Yang, Fan; Liu, Yunxin; Guo, Minyi; Zhu, Yuhao.
- Publication: ISCA, 2023.
- Source: [paper](https://arxiv.org/abs/2304.07493v1); [full text reviewed](https://arxiv.org/pdf/2304.07493v1).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Outlier-victim encoding, pruning, and hardware alignment.
- Evidence: Algorithm/architecture evaluation.

## What it establishes

Sacrifices nearby ordinary values to encode outliers in a memory-aligned representation for weights and activations.

## Relevance to our goals

Shows why local pairing and encoding can matter more than raw outlier count.

## Limits and transfer conditions

Victim removal is an additional approximation. Locality assumptions and quality loss must be checked; activation-only gains cannot be inferred from combined weight/activation changes.
