# MIAO: Microscaling Intermediate Accumulation Optimization

- Citation key: `wong2026miao`.
- Authors: Chloe Wong; Nicolas Rakela; Man Shi; Hansung Kim; Ruohan Richard Yan; Coleman Richard Charles Hooper; Yakun Sophia Shao.
- Publication: 2026; author version `2611.19722v1`.
- Source: [paper](https://arxiv.org/abs/2611.19722v1); [full text](https://arxiv.org/html/2611.19722v1).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Reading focus: Sections 2.2–4: weight-stationary stages, scale calibration, datapath and precision search.

## What it establishes

Jointly selects product and row-dependent floating-point accumulator formats in a weight-stationary MX array. Scale shifts and an accuracy predictor are calibrated; candidate configurations receive bit-exact end-to-end evaluation.

## Relevance to our goals

Direct hardware/software precedent for changing intermediate precision with operand quantization. Compare its optimized datapath before claiming savings against uniform accumulation.

## Limits and transfer conditions

Row-dependent hardware widths and prepared configurations do not establish a calibration-free decision from each live activation tile. Conversely, prepared selection does not remove its hardware contribution. Cross-tile accumulation remains BF16 in the reviewed design. Reported component/system savings are configuration-specific and not reproduced here.
