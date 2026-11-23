# NNSmith: Generating Diverse and Valid Test Cases for Deep Learning Compilers

- Citation key: `liu2023nnsmith`.
- Authors: Jiawei Liu; Jinkun Lin; Fabian Ruffy; Cheng Tan; Jinyang Li; Aurojit Panda; Lingming Zhang.
- Publication/version: 2023; version/source pinned below.
- Source: [primary source](https://arxiv.org/abs/2207.13066v2).
- Reviewed: 2026-11-24. Status: **Primary full text, focused Sections 2.3, 3.1–3.3 and 4; evaluation is not exhaustively reviewed.**

## Findings, relevance and limits

NNSmith generates graphs from lightweight operator specifications and SMT constraints. Bidirectional construction and attribute binning increase valid graph/shape diversity. Gradient-guided input/weight search avoids NaN/Inf throughout the graph, including cases where a later operator could hide an exceptional intermediate value. Differential execution then compares compiled outputs with a PyTorch reference. These are stronger baselines than arbitrary random tensors or output-only finite-value checks.

The inspected protocol targets compiler correctness and graph-generation coverage. It does not report our quantizer live/frozen decision-state intervention or optimization-ranking experiment. This is a narrow protocol comparison, not proof that NNSmith cannot express custom adaptive operators. For intentionally approximate arithmetic, a declared reference and acceptance contract are necessary before treating a discrepancy as a bug. Generated DAGs, differential testing and finite-input search are established techniques.
