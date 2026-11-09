# HAQ: Hardware-Aware Automated Quantization with Mixed Precision

- Citation key: `wang2019haq`.
- Authors: Wang, Kuan; Liu, Zhijian; Lin, Yujun; Lin, Ji; Han, Song.
- Publication: CVPR, 2019.
- Source: [paper](https://arxiv.org/abs/1811.08886v3); [full text reviewed](https://arxiv.org/pdf/1811.08886v3).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Offline policy search, hardware feedback, and model adaptation.
- Evidence: Reinforcement-learning search with hardware-model feedback.

## What it establishes

Searches layer-wise mixed-precision policies using latency/energy feedback rather than operation-count proxies alone.

## Relevance to our goals

A baseline for hardware-aware offline policy selection.

## Limits and transfer conditions

An offline search agent is not a controller inspecting live activations. Simulator feedback and fine-tuning conditions must remain distinct from measured deployment energy.
