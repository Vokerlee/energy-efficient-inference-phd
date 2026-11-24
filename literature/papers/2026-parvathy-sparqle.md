# SPARQLe: Sub-Precision Activation Representation for Quantized LLM Inference

- Citation key: `parvathy2026sparqle`.
- Authors: Aradhana Mohan Parvathy; Soumendu Kumar Ghosh; Shamik Kundu; Arnab Raha; Souvik Kundu; Deepak A. Mathaikutty; Anand Raghunathan.
- Source: [paper](https://arxiv.org/abs/2606.00365v1); [reviewed text](https://arxiv.org/html/2606.00365v1).
- Publication: author preprint, version1.
- Reviewed: 2026-11-24. Status: **primary full-text focused reading**.
- Reading focus: Sections3.1–3.2; architecture/evaluation not independently checked.

## What it establishes

Represents an existing quantized activation using dense low bits, sparse high
bits and a precision bitmap. Adds a weight-informed selective clipping method
to increase high-bit sparsity and describes a dedicated datapath for that format.

## Relevance and limits

Activation sub-precision sparsity and co-designed execution already have a
concrete representation. Logical narrowing, bitmap overhead and realized array
skipping must be separated. A decomposition of unchanged codes differs from
lossy current-group rounding; the sparsity enhancement changes values. LLM
results do not automatically transfer to source-before-im2col vision workloads
or the target BF16/FP8 interface. No reported PPA result was reproduced.
