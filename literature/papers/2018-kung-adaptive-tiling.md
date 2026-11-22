# Adaptive Tiling: Applying Fixed-size Systolic Arrays To Sparse Convolutional Neural Networks

- Citation key: `kung2018adaptivetiling`.
- Authors: H. T. Kung; Bradley McDanel; Sai Qian Zhang.
- Publication: ICPR 2018, pages 1006–1011.
- Source: [author full text](https://www.eecs.harvard.edu/~htk/publication/2018-icpr-kung-mcdanel-zhang.pdf); [conference record](https://iapr.org/archives/icpr2018/rtf/ICPR18_ContentListWeb_2.html).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Sections II–III: sparse filter preparation, column allocation and physical array calls.

## What it establishes

Variable-width sparse-weight tiles combine data columns to reduce fixed-size array invocations. The evaluated Lasso-Mobile weights come from regularized training and pruning.

## Relevance to our goals

Direct prior art for sparsity-dependent tiling and physical-call accounting, earlier than recent activation methods.

## Limits and transfer conditions

Adaptivity here exploits prepared filter structure. It does not by itself establish input-dependent activation approximation, a new precision policy or affordable online regrouping. Fewer calls are not a complete energy ledger. Results were not reproduced.
