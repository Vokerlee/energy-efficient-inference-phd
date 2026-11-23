# BFP-CIM: Runtime Energy-Accuracy Scalable Computing-in-Memory-Based DNN Accelerator Using Dynamic Block-Floating-Point Arithmetic

- Citation key: `chang2024bfpcim`.
- Authors: Cheng-Yang Chang; Chi-Tse Huang; Yu-Chuan Chuang; Kuang-Chao Chou; An-Yeu Wu.
- Publication: 2024.
- Source: [record](https://doi.org/10.1109/TCSI.2023.3338378); [reviewed text](https://access.ee.ntu.edu.tw/files/journals/%282023%29BFP-CIM_Runtime_Energy-Accuracy_Scalable_Computing-in-Memory-Based_DNN_Accelerator_Using_Dynamic_Block-Floating-Point_Arithmetic.pdf).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Reading focus: Sections III–V: range-aware rounding, live exponent grouping, digital control and energy-model boundaries. Journal metadata checked through Crossref.

## What it establishes

Combines input-dependent rounding, exponent-based wordline scheduling and bit-zero skipping. Integer partial sums are shifted before updating output state. Evaluates model accuracy, synthesized digital control and a NeuroSim-based analog accelerator model.

## Relevance to our goals

Direct hardware prior art for runtime quantization together with sparsity and exponent grouping.

## Limits and transfer conditions

The initial uint8 tensor-maximum mapping also needs a collection/lifetime policy. Some lowest-bit results use retraining. The source is a hardware design with synthesis/model evidence, not a fabricated-chip energy measurement. ADC-dominated savings do not establish the same benefit in a digital systolic array.
