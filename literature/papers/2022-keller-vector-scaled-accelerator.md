# A 17–95.6 TOPS/W Deep Learning Inference Accelerator with Per-Vector Scaled 4-bit Quantization for Transformers in 5nm

- Citation key: `keller2022vsqchip`.
- Authors: Keller, Ben; Venkatesan, Rangharajan; Dai, Steve; Tell, Stephen G.; Zimmer, Brian; Dally, William J.; Gray, C. Thomas; Khailany, Brucek.
- Publication: IEEE Symposium on VLSI Technology and Circuits, 2022.
- Source: [paper](https://d1qx31qr3h6wln.cloudfront.net/publications/C02-1.PDF).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Vector scaling datapath, nonlinear support, prototype, and quality conditions.
- Evidence: 5 nm inference-chip prototype and application evaluation.

## What it establishes

Implements per-vector scale handling with low-bit arithmetic and approximate nonlinear support, connecting numerical choices to a complete accelerator.

## Relevance to our goals

Silicon-level evidence that local scaling and its overhead belong in an inference hardware design.

## Limits and transfer conditions

Peak TOPS/W is not the energy benefit of activation adaptation alone. Quantization-aware fine-tuning and nonlinear approximations influence reported model quality.
