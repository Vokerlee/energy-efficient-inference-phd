# TVM: An Automated End-to-End Optimizing Compiler for Deep Learning

- Citation key: `chen2018tvm`.
- Authors: Chen, Tianqi; Moreau, Thierry; Jiang, Ziheng; Zheng, Lianmin; Yan, Eddie; Cowan, Meghan; Shen, Haichen; Wang, Leyuan; Hu, Yuwei; Ceze, Luis; Guestrin, Carlos; Krishnamurthy, Arvind.
- Publication: OSDI, 2018.
- Source: [paper](https://arxiv.org/abs/1802.04799v3); [full text reviewed](https://arxiv.org/pdf/1802.04799v3).
- Reviewed: 2026-11-09. Status: **full-text focused reading**.
- Reading focus: Tensor expressions, tensorization, memory scopes, and accelerator lowering.
- Evidence: Compiler design and implemented CPU/GPU/FPGA evaluation.

## What it establishes

Separates computation descriptions from schedules and declares tensor intrinsics with their behavior and lowering rules.

## Relevance to our goals

A useful precedent for exposing finite hardware operations while keeping model semantics separate from target execution.

## Limits and transfer conditions

The paper is a historical design reference, not current TVM API documentation. A compiler performance result does not validate a new activation controller or its numerical behavior.
