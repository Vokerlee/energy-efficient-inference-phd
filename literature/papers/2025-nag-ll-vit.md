# LL-ViT: Edge Deployable Vision Transformers with Look Up Table Neurons

- Citation key: `nag2025llvit`.
- Authors: Shashank Nag, Alan T. L. Bacellar, Zachary Susskind and colleagues.
- Publication: International Conference on Field Programmable Technology, 2025; arXiv:2511.00812v1 reviewed.
- Source: [versioned paper](https://arxiv.org/abs/2511.00812v1); [full text](https://arxiv.org/html/2511.00812v1).
- Reviewed: 2026-11-22. Status: **full-text focused reading**.
- Reading focus: Sections III-A and IV; Tables I, II and VI, FPGA estimation assumptions.
- Evidence: RTL synthesis and FPGA power/energy estimates; not physical energy measurements.

## What it establishes

Table VI gives an INT8 I-ViT-T baseline encoder-block breakdown on a 32-by-32
systolic design: two MLP layers total 188.70 microjoules, Q/K/V plus the
parameterized output stage total 94.36, and the two attention-core products
total 55.04, summing to 338.10 microjoules. These are approximately 55.8%,
27.9% and 16.3% of that subtotal. The paper calls its parameterized output
stage “Multi-Head Concat”; Table I assigns it a square weight matrix.

The alternative replaces trained channel mixers with learned lookup-table
neurons; it requires model training, rather than a transparent runtime policy.

## Relevance to our goals

Provides architecture-specific evidence for examining MLP and projection
operations, not only attention-core products. Arithmetic and weight storage
both matter in the channel mixer.

## Limits and transfer conditions

Power uses AMD Power Design Manager with 12.5% default switching activity.
Table VI omits Softmax, GELU and LayerNorm. Its subtotal is not a complete
chip/system energy ledger, and does not isolate MAC versus buffer costs.
The baseline is already quantized; these shares do not predict additional
savings from adaptive activation precision or transfer to another array.
