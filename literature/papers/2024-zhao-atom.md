# Atom: Low-Bit Quantization for Efficient and Accurate LLM Serving

- Citation key: `zhao2024atom`.
- Authors: Zhao, Yilong; Lin, Chien-Yu; Zhu, Kan; Ye, Zihao; Chen, Lequn; Zheng, Size; Ceze, Luis; Krishnamurthy, Arvind; Chen, Tianqi; Kasikci, Baris.
- Publication: MLSys2024; author version2310.19102v3.
- Source: [primary source](https://arxiv.org/html/2310.19102v3).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Focus: Sections4.1–4.3 and4.5: calibrated channel identities, live data movement and group conversion.

## Findings, relevance and limits

Atom separates high-bit outlier channels from low-bit channels, reorders activations online using offline-calibrated channel IDs, and reorders weights once to preserve alignment. Runtime activation scales remain input-dependent. Fusing movement/conversion with preceding operators limits software overhead.

This establishes quantization plus regularized mixed-precision execution as prior art. The permutation acts along receiving input channels and requires corresponding weight changes; it is not inherently a live M-row precision partition. GPU throughput and movement results cannot be transferred to another array's energy, buffers or format-switch cost. No results were reproduced here.
