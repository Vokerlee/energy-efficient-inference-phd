# Temporal Feature Matters: A Framework for Diffusion Model Quantization

- Citation key: `huang2025temporalfeatures`.
- Authors: Huang, Yushi; Gong, Ruihao; Liu, Xianglong; Liu, Jing; Li, Yuhang; Lu, Jiwen; Tao, Dacheng.
- Publication: IEEE TPAMI 47(10),8823–8837,2025; focused author version 2407.19547v2.
- Source: [focused full text](https://arxiv.org/html/2407.19547v2).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Focus: SectionsIV-A–IV-D,V-A andV-C: sensitivity, cached features, strategy selection and evaluation.

## Findings, relevance and limits

Extends TFMQ with offline optimized/cached temporal features and a disturbance-based choice between cached and reconstructed temporal information. The selection is prepared offline, not inferred from each current activation block. Hardware deployment evaluates implementation speed; it does not establish energy savings.

This is direct prior art for treating small conditioning paths as numerically important. Cached sample-independent features can remove computation; compare them when the required finite-set assumptions hold. Those assumptions cannot automatically be transferred to SANA-Sprint or arbitrary conditioned networks. Journal metadata is verified through the authors’ repository; the focused full text is the stated author version.
