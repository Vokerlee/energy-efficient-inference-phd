# Efficient Precision-Scalable Hardware for Microscaling (MX) Processing in Robotics Learning

- Citation key: `cuyckens2025mxrobot`.
- Authors: Cuyckens, Stef; Yi, Xiaoling; Murthy, Nitish Satya; Fang, Chao; Verhelst, Marian.
- Publication: ISLPED, 2025.
- Source: [paper](https://arxiv.org/abs/2505.22404v1); [full text reviewed](https://arxiv.org/pdf/2505.22404v1).
- Reviewed: 2026-11-14. Status: **full-text focused reading**.
- Reading focus: Arithmetic unit and Section IV/Figure 7: implementation energy breakdown and training scope.
- Evidence: Synthesized precision-scalable hardware and robotics-training evaluation.

## What it establishes

Supports multiple MX types and square exponent groups, with a component-level breakdown showing substantial floating-point accumulation cost.

## Relevance to our goals

Additional hardware evidence for including reduction and accumulator activity in the cost model.

## Limits and transfer conditions

The breakdown uses specified random-input activity and a particular macro/design. It is not the energy split of every NPU or an inference-only activation policy.
