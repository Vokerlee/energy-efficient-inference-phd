# Gemma 2: Improving Open Language Models at a Practical Size

- Citation key: `gemmateam2024gemma2`.
- Authors: Gemma Team and others.
- Publication: technical report2408.00118v3,2024.
- Source: [full text](https://arxiv.org/html/2408.00118v3).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Focus: Section2 and parameter tables: attention structure, MLP, vocabulary and embedding storage.

## Findings, relevance and limits

Gemma2 combines grouped-query attention, alternating local/global attention, rotary positions and gated feed-forward processing. Parameter accounting separates a large vocabulary embedding from other model weights.

A text-conditioned generation pipeline may use its backbone as a prompt encoder without a language-model output head. Such full-sequence encoding is not autoregressive token-by-token decode. Count actual token lengths, padding, executed heads and repeated calls. Embedding-table size is not compulsory per-request memory traffic, and dense attention-shape MACs may differ from masked-kernel work. The checkpoint configuration and installed implementation govern a concrete profile. No model-quality or hardware-energy result was reproduced here.
