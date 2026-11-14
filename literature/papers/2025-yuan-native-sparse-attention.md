# Native Sparse Attention: Hardware-Aligned and Natively Trainable Sparse Attention

- Citation key: `yuan2025nsa`.
- Authors: Yuan, Jingyang; Gao, Huazuo; Dai, Damai; Luo, Junyu; Zhao, Liang; Zhang, Zhengyan; Xie, Zhenda; Wei, Y. X.; Wang, Lean; Xiao, Zhiping; Wang, Yuqing; Ruan, Chong; Zhang, Ming; Liang, Wenfeng; Zeng, Wangding.
- Publication: ACL; author preprint reviewed, 2025.
- Source: [paper](https://arxiv.org/abs/2502.11089v2); [full text reviewed](https://arxiv.org/pdf/2502.11089v2).
- Reviewed: 2026-11-14. Status: **full-text focused reading**.
- Reading focus: Sections 3.1–3.3: arithmetic intensity, compression/selection/window branches, block scoring.
- Evidence: Trained attention architecture and long-context model/kernel experiments.

## What it establishes

Combines learned compressed representations, dynamically selected blocks, and a local window, with gated branch outputs.

## Relevance to our goals

A hardware-aligned adaptive-attention comparison beyond vision, with compute/memory phase distinctions.

## Limits and transfer conditions

Native training changes the model. It is not evidence for inserting the same mechanism into arbitrary pretrained diffusion models without adaptation.
