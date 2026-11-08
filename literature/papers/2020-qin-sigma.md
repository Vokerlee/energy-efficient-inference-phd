# SIGMA: A Sparse and Irregular GEMM Accelerator with Flexible Interconnects for DNN Training

- Citation key: `qin2020sigma`.
- Authors: Qin, Eric; Samajdar, Ananda; Kwon, Hyoukjun; Nadella, Vineet; Srinivasan, Sudarshan; Das, Dipankar; Kaul, Bharat; Krishna, Tushar.
- Publication: HPCA, 2020.
- Source: [paper](https://bpb-us-e1.wpmucdn.com/sites.gatech.edu/dist/c/332/files/2020/01/sigma_hpca2020.pdf).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Flexible dot-product engine, forwarding adder network, and evaluation assumptions.
- Evidence: Training-oriented architecture study with physical-design estimates.

## What it establishes

Combines flexible operand distribution with tree-based reduction to handle irregular and sparse GEMMs. This trades systolic-style forwarding constraints for configurable communication.

## Relevance to our goals

Tests whether our algorithm's shape or sparsity requirements are specific to a systolic array.

## Limits and transfer conditions

The primary target is training. Inference energy and task-quality benefits cannot be imported from its performance comparisons.
