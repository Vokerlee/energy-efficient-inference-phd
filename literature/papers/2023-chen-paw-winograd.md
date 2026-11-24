# Towards Efficient and Accurate Winograd Convolution via Full Quantization

- Citation key: `chen2023paw`.
- Authors: Tianqi Chen; Weixiang Xu; Weihan Chen; Peisong Wang; Jian Cheng.
- Source: [primary source](https://papers.nips.cc/paper_files/paper/2023/hash/400a2e6a82520b690810b97fd67fcc4e-Abstract-Conference.html).
- Publication: NeurIPS2023.
- Reviewed: 2026-11-24. Status: **primary abstract only**.

## Findings and relevance

PAW jointly optimizes Winograd stages for post-training quantization and
introduces factorized scale quantization for transformed-domain range differences.
Full quantization and scale balancing across transforms are therefore existing
methods; they cannot be claimed from a new implementation alone.

## Limits

The abstract does not establish a particular calibration-free online controller,
output-buffer codec or target-array schedule. Details of parameter fitting and
hardware costs remain a full-method comparison dependency. No reported accuracy
or implementation result was reproduced.
