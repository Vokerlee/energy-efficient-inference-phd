# MMA-Sim: Bit-Accurate Reference Model of Tensor Cores and Matrix Cores

- Citation key: `xie2025mmasim`.
- Authors: Xie, Peichen; Wang, Yang; Yang, Fan; Yang, Mao.
- Publication: arXiv preprint, 2025, version 1.
- Source: [arXiv v1](https://arxiv.org/abs/2511.10909v1).
- Reviewed: 2026-11-21. Status: **abstract and bibliographic verification only**.
- Evidence: Authors report a bit-accurate software model and hardware comparison.

## Scope and relevance

The abstract describes targeted and randomized tests for reconstructing the
arithmetic of GPU matrix units. Such references help distinguish agreement
with a software comparator from agreement with a specific hardware instruction.

## Limits

The full experimental protocol and instruction coverage have not been reviewed
here. The abstract does not establish that replacing a GEMM implementation
preserves a complete network's task quality.

Version discipline matters: v3 has a different title and an expanded author
list. This record deliberately describes v1; do not mix its metadata with v3.
