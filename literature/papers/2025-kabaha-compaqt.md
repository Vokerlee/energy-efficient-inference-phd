# Quantization with Guaranteed Floating-Point Neural Network Classifications

- Citation key: `kabaha2025compaqt`.
- Authors: Anan Kabaha; Dana Drachsler Cohen.
- Publication: 2025; DOI `10.1145/3763118`.
- Source: [publisher](https://doi.org/10.1145/3763118).
- Author full text: [PDF](https://ddana.net.technion.ac.il/files/2025/08/CoMPAQt.pdf).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Reading focus: Sections 3–5, especially Algorithm 2: prepared QEF bounds and online precision refinement.

## What it establishes

Computes class/precision-specific confidence bounds using MILP-based analysis. At inference, adaptive precision refinement accepts a sufficiently confident quantized prediction or executes another precision, ultimately using the reference network when needed.

## Relevance to our goals

Online refinement and claimed classification consistency already have formal-method precedents; this is not an offline-only algorithm.

## Limits and transfer conditions

Bounds and quantization schemes are prepared for a specified network. Classification consistency is not a general diffusion-quality certificate. The network abstraction uses real-valued neuron expressions with explicit quantization; do not infer bit-accurate accelerator arithmetic from the title. Solver, repeated-inference and fallback costs belong in comparisons.
