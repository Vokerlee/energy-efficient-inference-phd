# A 28nm 244.45TOPS/W Winograd-Standard Fusion Accelerator with Symmetric Hybrid Domain CIM Groups for Edge AI Devices

- Citation key: `guo2025winogradcim`.
- Authors: An Guo; Zhichao Liu; Wentao Zheng; Yutong Zhang; Tianhui Jiao; Fangyuan Dong; Mingzi Wang; Shaochen Li; Zhican Zhang; Yuhui Shi; Xing Wang; Xin Si; Xin Wang; Wenwu Zhu.
- Source: [author manuscript](https://mn.cs.tsinghua.edu.cn/xinwang/PDF/papers/2025_A%2028nm%20244.45TOPSW%20Winograd-Standard%20Fusion%20Accelerator%20with%20Symmetric%20Hybrid%20Domain%20CIM%20Groups%20for%20Edge%20AI%20Devices.pdf).
- Reviewed: 2026-11-24. Status: **full-text focused reading**, three-page manuscript, architecture and component breakdown.
- Publication scope: labeled ASSCC2025; session/paper placeholders remain. Proceedings metadata not independently verified.

## Relevance and limits

Reports fabricated hybrid analog/digital CIM with Winograd preprocessing and
advanced output aggregation. Its component breakdown assigns72.2% of power to
post-macro processing. Retraining is used for the reported detector result.
These are source measurements, not reproduced here.

A concrete warning against inferring energy from MAC count: an efficient matrix
core can leave surrounding transforms dominant. Its bit-serial processing,
accumulators and mixed-domain circuit differ from a BF16/FP32 systolic interface.
Partial output-transform acceleration is already architectural prior art.
