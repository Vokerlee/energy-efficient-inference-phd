# Fast Linear Algebra is Stable

- Citation key: `demmel2007stable`.
- Authors: Demmel, James; Dumitriu, Ioana; Holtz, Olga.
- Publication: arXiv preprint, 2007.
- Source: [paper](https://arxiv.org/abs/math/0612264v3); [full text reviewed](https://arxiv.org/pdf/math/0612264v3).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Stability definitions, precision assumptions, and scope.
- Evidence: Numerical-analysis results.

## What it establishes

Establishes stability properties for classes of fast linear-algebra algorithms under explicit precision/error assumptions.

## Relevance to our goals

Prevents rejecting fast multiplication solely because its operation ordering differs.

## Limits and transfer conditions

Asymptotic stability does not guarantee acceptable BF16/FP8 neural quality or a useful finite-size hardware crossover.
