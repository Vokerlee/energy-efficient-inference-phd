# NAWQ-SR: A Hybrid-Precision NPU Engine for Efficient On-Device Super-Resolution

- Citation key: `venieris2023nawqsr`.
- Authors: Venieris, Stylianos I.; Almeida, Mario; Lee, Royson; Lane, Nicholas D..
- Publication: IEEE Transactions on Mobile Computing, 2023.
- Source: [paper](https://arxiv.org/abs/2212.09501v1); [full text reviewed](https://arxiv.org/pdf/2212.09501v1).
- Reviewed: 2026-11-14. Status: **full-text focused reading**.
- Reading focus: Sections 4.1–4.3: offline wordlength search, DRE layer selection, runtime quantization unit.
- Evidence: Framework design and mobile-NPU deployment evaluation.

## What it establishes

Chooses hybrid wordlengths and DRE layers offline; selected layers measure current activation ranges and update scales/zero points at runtime.

## Relevance to our goals

A deployed comparison for charging range scans, conversion, and dispatcher costs.

## Limits and transfer conditions

Executing the prepared layer schedule is not fresh per-input bitwidth selection. Runtime scaling is software/framework-controlled rather than proof of a new autonomous datapath policy.
