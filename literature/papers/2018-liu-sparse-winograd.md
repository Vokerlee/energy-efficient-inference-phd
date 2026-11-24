# Efficient Sparse-Winograd Convolutional Neural Networks

- Citation key: `liu2018sparsewinograd`.
- Authors: Xingyu Liu; Jeff Pool; Song Han; William J.Dally.
- Publication: ICLR2018; arXiv1802.06367v1.
- Source: [author manuscript](https://arxiv.org/abs/1802.06367).
- Reviewed:2026-11-24. Status: **full-text focused reading**, §3, especially§3.2.

## Contribution and relevance

Moves ReLU after the input Winograd transform, recovering dynamic activation
zeros, and trains/prunes transformed weights. Section3.2 explicitly states
that this network is not mathematically equivalent to the original network
and uses dense training, pruning and retraining.

## Comparison boundary

Dynamic transformed-activation sparsity already exists. Its altered network
semantics and training requirements distinguish it from approximating an
unchanged pretrained model at runtime. This does not by itself clear novelty
for activation gating: compare exact zero gating, approximate thresholds,
metadata and dense-array scheduling separately. MAC savings are not evidence
of total hardware energy savings.
