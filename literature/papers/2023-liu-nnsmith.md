# NNSmith: Generating Diverse and Valid Test Cases for Deep Learning Compilers

- Citation key: `liu2023nnsmith`.
- Authors: Jiawei Liu; Jinkun Lin; Fabian Ruffy; Cheng Tan; Jinyang Li; Aurojit Panda; Lingming Zhang.
- Publication/version: 2023; version/source pinned below.
- Source: [primary source](https://arxiv.org/abs/2207.13066v2).
- Reviewed: 2026-11-24. Status: **Primary abstract and indexed author-paper Section3.2; full-method review pending.**

## Findings, relevance and limits

Generates valid diverse graphs, searches inputs avoiding exceptional values and differentially tests compiler outputs. The author paper describes constraint-guided graph generation. Differential testing and generated DAGs are established approaches. Intentionally approximate arithmetic needs a declared acceptance contract; a difference is not automatically a compiler bug. Causal controller-state and energy comparisons require separate verification of the full method.
