# Dual-side Sparse Tensor Core

- Citation key: `wang2021dualside`.
- Authors: Wang, Yang; Zhang, Chen; Xie, Zhiqiang; Guo, Cong; Liu, Yunxin; Leng, Jingwen.
- Publication: arXiv preprint, 2021.
- Source: [paper](https://arxiv.org/abs/2105.09564v1); [full text reviewed](https://arxiv.org/pdf/2105.09564v1).
- Reviewed: 2026-11-14. Status: **full-text focused reading**.
- Reading focus: Sections III–V and bitmap-im2col evaluation: sparse format, lowering, outer-product primitive.
- Evidence: Architecture/ISA proposal and GPU simulation with sparse-kernel evaluation.

## What it establishes

Co-designs bitmap-encoded operands, outer-product sparse matrix multiplication, and bitmap-based implicit im2col.

## Relevance to our goals

Direct sparse-lowering prior art linking a feeder's representation to the multiplier organization.

## Limits and transfer conditions

A proposed Tensor Core extension is not an existing mode available on every GPU. Sparse lowering can still exceed dense-lowering cost; formats and dataflow must be compared together.
