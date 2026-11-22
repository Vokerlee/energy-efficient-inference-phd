# Runtime-Certified Bounded-Error Quantized Attention

- Citation key: `calver2026runtimecertified`.
- Authors: Calver, Dean.
- Publication: arXiv preprint, 2026; pinned author version.
- Source: [paper](https://arxiv.org/abs/2605.20868v1); [full text](https://arxiv.org/html/2605.20868v1).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Sections 2–3 and reference-output definitions; complete proof audit pending.

## What it establishes

Stores compressed KV on GPU and retains FP16 originals in system RAM. An INT8 scoring pass estimates block mass before adaptive promotion and an attend pass. Online local bounds govern recovery.

## Relevance to our goals

Runtime output-error-aware precision and fallback already have explicit prior art.

## Limits and transfer conditions

Count scoring, sorting, retained originals and page-in; the selector is not a free scalar decision. The certificate has a specified reference numerical path. Local attention bounds do not guarantee whole-model task quality. Proofs and reported results were not independently validated.
