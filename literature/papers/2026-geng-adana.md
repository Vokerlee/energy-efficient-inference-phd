# Adana: Accelerating Large Language Models via Adaptive Nonuniform Asymmetric Quantization

- Citation key: `geng2026adana`.
- Authors: Xinkuang Geng; Siting Liu; Hui Wang; Leibo Liu; Jie Han; Honglan Jiang.
- Publication: DAC2026; DOI10.1145/3770743.3804291.
- Source: [author paper](https://www.ece.ualberta.ca/~jhan8/publications/2026Adana.pdf); [official program](https://63dac.conference-program.com/presentation/?id=RESEARCH2184&sess=sess140); [author slides](https://www.ece.ualberta.ca/~jhan8/publications/dac26-adana.pdf).
- Reviewed: 2026-11-24. Status: **primary full-text focused reading**.
- Reading focus: Section4.2 Algorithm2 and Section5 architecture/dataflow. Earlier record used abstract/slides only.

## What it establishes

Uses integer and half-step rounding to select a nonuniform asymmetric subtype
for each activation group. Its approximate error metric replaces repeated
floating-point MSE evaluation with counters. A dedicated quantization engine
feeds the matrix engine.

## Relevance and limits

Cheap live format selection with dedicated hardware is already demonstrated
as an algorithm/architecture design. Merely replacing an expensive online
search with a small candidate set is insufficient differentiation. The metric
measures representation error rather than a general receiving-product objective.
LLM results do not establish energy gains for compute-heavy vision operators.
The focused review does not independently verify RTL or reported PPA results.
