# Is Your NPU Ready for LLMs? Dissecting the Hidden Efficiency Bottlenecks in Mobile LLM Inference

- Citation key: `cai2026mobilenpu`.
- Authors: Cai, Guanyu; Tian, Ruiming; Yang, Lang; Ren, Zhouhong; Yuan, Jinliang; Li, Lingkun; Wang, Jiliang.
- Publication: arXiv preprint, 2026.
- Source: [paper](https://arxiv.org/abs/2607.05475v2); [full text reviewed](https://arxiv.org/pdf/2607.05475v2).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Methodology, hardware microbenchmarks, phase characterization, and limitations.
- Evidence: Four-phone Qualcomm CPU/GPU/NPU measurement study.

## What it establishes

Finds different backend preferences for prefill and decode, with energy also influenced by host scheduling and accelerator invocation. Uses hardware microbenchmarks and backend-specific telemetry to interpret behavior.

## Relevance to our goals

Extends the review beyond GPUs and highlights control/host costs that a matrix-only model can miss.

## Limits and transfer conditions

Frameworks use differing representations and execution paths. Backend-specific attribution is not a multiplier/SRAM energy decomposition. Current public evidence is the 2026 preprint, despite its stated future publication/acceptance.
