# Packing Sparse Convolutional Neural Networks for Efficient Systolic Array Implementations: Column Combining Under Joint Optimization

- Citation key: `kung2019packing`.
- Authors: Kung, H. T.; McDanel, Bradley; Zhang, Sai Qian.
- Publication: ASPLOS, 2019.
- Source: [paper](https://doi.org/10.1145/3297858.3304028); [full text reviewed](https://www.eecs.harvard.edu/~htk/publication/2019-asplos-kung-mcdanel-zhang.pdf).
- Reviewed: 2026-11-14. Status: **full-text focused reading**.
- Reading focus: Sections 3–4: column conflicts, joint pruning/retraining, and packed systolic execution.
- Evidence: Algorithm/hardware co-design with ASIC/FPGA-based evaluation.

## What it establishes

Combines sparse filter columns into denser stored columns, pruning conflicts and retraining the remaining model.

## Relevance to our goals

An existing systolic packing mechanism against which to distinguish runtime activation compaction.

## Limits and transfer conditions

It changes weights and model preparation. Static filter grouping does not establish cheap regrouping of arbitrary live activations.
