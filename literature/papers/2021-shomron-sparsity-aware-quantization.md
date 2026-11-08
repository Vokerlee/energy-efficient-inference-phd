# Post-Training Sparsity-Aware Quantization

- Citation key: `shomron2021sparq`.
- Authors: Shomron, Gil; Gabbay, Freddy; Kurzum, Samer; Weiser, Uri.
- Publication: NeurIPS, 2021.
- Source: [paper](https://arxiv.org/abs/2105.11010v2); [full text reviewed](https://arxiv.org/pdf/2105.11010v2).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Bit-window selection, paired activation budgets, and implementation.
- Evidence: Quantization-quality and hardware evaluation.

## What it establishes

Uses activation bit sparsity to select retained windows and shares a pair's bit budget when one activation is zero.

## Relevance to our goals

Direct prior art for combining runtime activation properties with reduced precision.

## Limits and transfer conditions

It operates above an INT8 representation and depends on its packing/arithmetic design. This SPARQ is distinct from other papers sharing the acronym.
