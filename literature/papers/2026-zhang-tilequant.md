# TileQuant: Tile as the Precision-Allocation Unit for LLM Mixed-Precision Post-Training Quantization

- Citation key: `zhang2026tilequant`.
- Authors: Zhang, Hanzhi; Zhang, Qiao; Cao, Qinglei; Fan, Heng; Huang, Yan; Sha, Kewei; Feng, Yunhe.
- Publication: arXiv2611.07217v1,2026.
- Source: [primary source](https://arxiv.org/html/2611.07217v1).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Focus: Sections4.2–4.3 andAppendicesD.3,E.1–E.3,G.2: static maps, packing, activation preparation and scheduling.

## Findings, relevance and limits

Calibrated weight-tile scores determine a fixed8/16-bit retention map. Precision-specific buffers and indices support dense tile products and local FP32 accumulation. Runtime activation scales and row-tile/split choices adapt to input shape while the precision map remains fixed.

This is recent prior art for precision allocation coupled to storage and execution. Its row-order metadata describes packed weight tiles, not automatically live grouping of activation rows by their current errors. Complete-input maxima and shape-based chunking have different stream/buffer requirements from bounded causal source decisions. Compare allocation axes and actual state/traffic assumptions; neither static maps nor GPU speed establish a dedicated array's energy. No results were reproduced.
