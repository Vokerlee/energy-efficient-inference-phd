# Syndrome Decoding for Silent Data Corruption in Quantized Integer GPU Arithmetic

- Citation key: `napolean2026sprobe`.
- Authors: Napolean, Pranav; Srivastava, Vikas; Periathambi, Napolean.
- Publication: arXiv preprint 2609.19743v1, 2026-09-17.
- Source: [record](https://arxiv.org/abs/2609.19743v1); [PDF](https://arxiv.org/pdf/2609.19743v1).
- Reviewed: 2026-11-15. Status: **full-text focused reading**.
- Reading focus: Sections II–III: fault model, placement, verification gate, and reread costs.
- Evidence: Finite-field fault checking, diagnosis, and reported GPU experiments; not reproduced here.

## What it establishes

Verifies integer GEMM results using a randomized gate and diagnoses sparse
faults using algebraic syndromes. A trailing verifier rereads operands and
outputs; the paper contrasts this with fused checksums.

## Relevance to our goals

Randomized checking already applies to quantized accelerator arithmetic.
It provides a concrete warning that observing a matrix product can require
substantial extra traffic.

## Limits and transfer conditions

Sparse hardware faults in exact integer products differ from dense, intentional
quantization residuals. Fault-detection probabilities do not transfer to real
error-energy estimates or task quality. Reported performance is not verified here.
