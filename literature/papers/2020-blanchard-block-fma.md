# Mixed Precision Block Fused Multiply-Add: Error Analysis and Application to GPU Tensor Cores

- Citation key: `blanchard2020blockfma`.
- Authors: Blanchard, Pierre; Higham, Nicholas J.; Lopez, Florent; Mary, Theo; Pranesh, Srikara.
- Publication: SIAM Journal on Scientific Computing, 2020.
- Source: [paper](https://doi.org/10.1137/19M1289546); [full text reviewed](https://eprints.maths.manchester.ac.uk/2749/1/paper.pdf).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Block-FMA rounding model, matrix multiplication, and GPU checks; author preprint.
- Evidence: Numerical analysis with hardware experiments.

## What it establishes

Analyzes mixed-precision block operations rather than treating every multiply/add as identical scalar arithmetic.

## Relevance to our goals

A basis for specifying rounding at physical block and accumulation boundaries.

## Limits and transfer conditions

The analysis assumes stated arithmetic behavior. It does not establish our hardware's reduction order or end-to-end neural quality.
