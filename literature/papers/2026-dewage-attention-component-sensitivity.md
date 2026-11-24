# Component Type, Not Reconstruction Error, Predicts Attention Quantization Sensitivity

- Citation key: `dewage2026componentsensitivity`.
- Authors: Kasun Dewage; Marianna Pensky; Suranadi De Silva.
- Source: [paper](https://arxiv.org/abs/2609.26173v1); [reviewed text](https://arxiv.org/html/2609.26173v1).
- Publication: author preprint; accepted IEEE ICMLA2026 according to author metadata.
- Reviewed: 2026-11-24. Status: **primary full-text focused reading**.
- Reading focus: SectionsIII, IV-D–F andV; results not reproduced.

## What it establishes

Quantizes one attention projection's weights at a time in nine LLMs, comparing
reconstruction diagnostics with perplexity changes. Component and layer identity
carry information that simple reconstruction error misses. V often dominates,
but the dominance is not universal across architectures or methods.

## Relevance and limits

Direct prior art against equating low receiving/weight error with end-task
sensitivity, and for component-aware precision comparison. Its intervention is
weight quantization, not current-input activation rounding or a vision-transformer
hardware controller. It does not establish the best Q/K/V activation allocation
for DINOv3. Treat component protection as a comparator, not a new generic idea.
