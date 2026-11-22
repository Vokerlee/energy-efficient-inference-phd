# ViDiT-Q: Efficient and Accurate Quantization of Diffusion Transformers for Image and Video Generation

- Citation key: `zhao2025viditq`.
- Authors: Zhao, Tianchen; Fang, Tongcheng; Huang, Haofeng; Liu, Enshu; Wan, Rui; Soedarmadji, Widyadewi; Li, Shiyao; Lin, Zinan; Dai, Guohao; Yan, Shengen; Yang, Huazhong; Ning, Xuefei; Wang, Yu.
- Publication: International Conference on Learning Representations (ICLR), 2025.
- Source: [paper](https://arxiv.org/abs/2406.02540v3); [full text reviewed](https://arxiv.org/pdf/2406.02540v3).
- Reviewed: 2026-11-08. Status: **full-text focused reading**.
- Reading focus: Section 5.3 and Appendix E.2; full-model quality conditions. Supplement 2026-11-22: Appendix A.1 operator-latency breakdown.
- Evidence: Quantized diffusion-model quality, GPU latency, and memory measurements.

## What it establishes

Reports approximately 1.71× end-to-end speedup for W8A8 in its resource evaluation. W4A8 stores narrower weights but computes with upcast weights, illustrating a memory-saving change that does not provide faster arithmetic.

## Relevance to our goals

A relevant compute-intensive workload and a reminder to count conversions, nonquantized operators, and supported execution formats.

## Limits and transfer conditions

Latency and allocated-memory results do not measure energy. The tested GPU implementation does not establish that every diffusion configuration is compute-bound.

## Operator-profile supplement — 2026-11-22

Appendix A.1 reports that the attention-core products occupy 14.3% of an
STDiT block's latency when using FlashAttention. This category excludes
Q/K/V linear mappings and the output projection; those remain targets of
linear-layer quantization. It is one implementation's latency profile,
not a measured energy split or a universal statement about video attention.
