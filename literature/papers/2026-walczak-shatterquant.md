# ShatterQuant: Breaking Uniform Precision with Block-Wise Mixed-Precision on a Systolic Transformer Hardware Accelerator

- Citation key: `walczak2026shatterquant`.
- Authors: Walczak, Mikolaj; Humes, Edward; Fang, Chao; Verhelst, Marian; Mohsenin, Tinoosh.
- Publication: ICCAD 2026; pinned author version.
- Source: [paper](https://arxiv.org/abs/2610.00207v1); [full text](https://arxiv.org/html/2610.00207v1).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Sections 3.2–3.4 and conclusion.

## What it establishes

Assigns 1/2/4/8-bit weight blocks through hardware-aware post-training preparation. Precision changes effective PE block dimensions; rescaling and accumulation support heterogeneous blocks. Activations remain 8-bit with calibrated scales.

## Relevance to our goals

Shows that precision and physical execution granularity are already co-designed. Its broad title does not imply a live activation-width selector.

## Limits and transfer conditions

The reviewed implementation uses a 16nm design kit; this is not evidence of fabricated-chip measurements. Extension to mixed-precision activations is stated as future work. That difference alone proves no general novelty claim.
