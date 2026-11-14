# Accumulation Bit-Width Scaling for Ultra-Low Precision Training of Deep Networks

- Citation key: `sakr2019accumulation`.
- Authors: Sakr, Charbel; Wang, Naigang; Chen, Chia-Yu; Choi, Jungwook; Agrawal, Ankur; Shanbhag, Naresh; Gopalakrishnan, Kailash.
- Publication: ICLR, 2019.
- Source: [paper](https://arxiv.org/abs/1901.06588v1); [full text reviewed](https://arxiv.org/pdf/1901.06588v1).
- Reviewed: 2026-11-14. Status: **full-text focused reading**.
- Reading focus: Section 4: statistical assumptions, variance retention, chunking, and sparsity.
- Evidence: Statistical accumulation analysis and training-convergence experiments.

## What it establishes

Relates mantissa precision and reduction length to variance loss from swamping; analyzes chunked accumulation and sparsity.

## Relevance to our goals

Prior art for deriving accumulator precision from numerical models rather than picking a conventional width.

## Limits and transfer conditions

Independent, zero-mean, equal-variance product assumptions need checking on inference data. Training convergence does not establish deterministic overflow safety or task quality for a live selector.
