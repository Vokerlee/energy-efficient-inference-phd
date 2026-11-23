# Eliminating Unstable Tests in Floating-Point Programs

- Citation key: `titolo2018unstabletests`.
- Authors: Laura Titolo and Cesar A. Muñoz and Marco A. Feliu and Mariano M. Moscato.
- Publication/version: arXiv 1808.04289v2.
- Source: [primary paper](https://arxiv.org/abs/1808.04289v2).
- Reviewed: 2026-11-24. Status: **Primary full text, focused Sections 2–3 and Theorem 1; author-hosted draft checked alongside the pinned arXiv version.**

## Findings and relevance

Transforms floating-point guards using bounds on expression errors. The resulting program either follows a stable path and returns the original floating-point result, or warns that stability cannot be established. Correctness is formalized in PVS. A margin-based quantizer-scale guard therefore specializes an existing stable-test idea; it is not a novel general theorem.

## Limits and comparison

A sound guard needs a valid perturbation bound and exact boundary semantics. A bound fitted to one observed backend pair cannot certify unseen hardware. Unknown does not mean a decision actually changed. This paper is a required baseline for selective reference execution, not evidence that a full neural controller has been verified.
