# DRQ: Dynamic Region-Based Quantization for Deep Neural Network Acceleration

- Citation key: `song2020drq`.
- Authors: Zhuoran Song; Bangqi Fu; Feiyang Wu; Zhaoming Jiang; Li Jiang; Naifeng Jing; Xiaoyao Liang.
- Publication: ISCA 2020; DOI 10.1109/ISCA45697.2020.00086.
- Source: [author record](https://faculty.sjtu.edu.cn/songzhuoran/zh_CN/lwcg/579848/content/205926.htm); [author-uploaded full text](https://www.researchgate.net/publication/342905349_DRQ_Dynamic_Region-based_Quantization_for_Deep_Neural_Network_Acceleration).
- Reviewed: 2026-11-22. Status: **full-text focused reading**; supersedes metadata-only review.
- Reading focus: Sections III, IV-A–E and VI-B; author upload dated 2021-01-08.

## What it establishes

Mean-filtered current INT8 regions produce sensitivity masks selecting INT4/INT8 convolution. Producer-side pooling/prediction, packed im2col delivery and a variable-speed array support the policy. Region sizes and thresholds are chosen through per-network/layer offline exploration.

## Relevance to our goals

Closes the full-text dependency for live regional precision, producer statistics and physical scheduling. These broad mechanisms are already described.

## Limits and transfer conditions

This is a prepared regional sensitivity policy, not proof of every output-error controller. Both operand arithmetic and stalls change with the selected mode. Accelerator evaluation does not establish energy savings on another memory hierarchy. Results were not reproduced.
