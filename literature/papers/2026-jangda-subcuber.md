# Compiling Strassen-like Matrix Multiplication Algorithms to Fast CUDA Kernels

- Citation key: `jangda2026subcuber`.
- Authors: Jangda, Abhinav.
- Publication: PLDI 2026; DOI 10.1145/3808267.
- Source: [primary source](https://www.microsoft.com/en-us/research/publication/compiling-strassen-like-matrix-multiplication-algorithms-to-fast-cuda-kernels/).
- Reviewed: 2026-11-22. Status: **Publisher/author abstract and publication metadata only; full-paper review pending.**

## What it establishes

SubCuber constructs dependency graphs and selects fused CUDA schedules according to recursion depth, matrix shape and GPU. The abstract reports FP32/FP16 evaluations on A100 and H200.

## Relevance to our goals

A direct implementation comparator for shape-dependent Strassen scheduling. Compiler generation and memory fusion are existing mechanisms.

## Limits and transfer conditions

The abstract does not establish custom-array energy savings or low-precision whole-model quality. Reported performance was not reproduced. Numerical conditions and complete kernels remain to inspect.
