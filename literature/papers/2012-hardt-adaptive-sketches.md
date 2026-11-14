# How Robust are Linear Sketches to Adaptive Inputs?

- Citation key: `hardt2012adaptivesketches`.
- Authors: Hardt, Moritz; Woodruff, David P.
- Publication: arXiv preprint 1211.1056v1, submitted 2012-11-05.
- Source: [record](https://arxiv.org/abs/1211.1056v1); [full text](https://arxiv.org/html/1211.1056v1).
- Reviewed: 2026-11-15. Status: **full-text focused reading**.
- Reading focus: Introduction, adaptive-input discussion, Section 1.1 Theorem 1.1, and Section 2 definitions.
- Version detail: The downloaded v1 PDF is internally dated 2018-10-29; retain the arXiv identifier/version when citing.
- Evidence: Worst-case theoretical limitations of linear sketches under adaptive queries.

## What it establishes

Constructs adaptive queries on which low-dimensional linear norm sketches fail.
An input chosen using previous sketch answers need not satisfy guarantees
proved for inputs independent of the sketch.

## Relevance to our goals

Reusing a norm estimator to select numerical actions creates a dependence
requiring analysis. Independent monitoring and adversarial examples are useful
evaluation controls.

## Limits and transfer conditions

The attack theorem does not show that a particular inference controller fails
on natural workloads. Fresh independent monitoring restores a fixed-input
estimation setting only when it cannot influence the choices being assessed.
