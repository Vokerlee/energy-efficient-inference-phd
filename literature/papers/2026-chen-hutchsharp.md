# Hutch#: Optimal non-adaptive Frobenius norm estimation

- Citation key: `chen2026hutchsharp`.
- Authors: Chen, Tyler; Halikias, Diana; Musco, Christopher; Persson, David.
- Publication: arXiv preprint 2609.28472v2, posted 2026-10-01; PDF internally dated 2026-10-02.
- Source: [record](https://arxiv.org/abs/2609.28472v2); [PDF](https://arxiv.org/pdf/2609.28472v2).
- Reviewed: 2026-11-15. Status: **full-text focused reading**.
- Reading focus: Sections 1–2, Eqs. (1)–(3), Theorem 1.1, and Section 3's sketch-reuse qualification.
- Evidence: Implicit norm-estimation theory and numerical evaluation; not reproduced here.

## What it establishes

Combines independent left/right Gaussian projections to reduce Frobenius-norm
estimation variance without adaptive matrix-vector queries or orthogonalization.
Its oracle includes products with both the matrix and its transpose.

## Relevance to our goals

A recent estimator comparator when choosing observation cost versus precision.
One-sided random-projection error estimation is not a new contribution.

## Limits and transfer conditions

Non-adaptive oracle queries do not mean robustness to an error matrix chosen
from estimator feedback. Two-sided products and auxiliary computations may
cost more than a one-sided hardware observation. The paper itself qualifies
dependencies introduced by a practical sketch-reuse shortcut.
