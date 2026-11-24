# Efficient Super-Resolution System with Block-Wise Hybridization and Quantized Winograd on FPGA

- Citation key: `shi2023winogradsr`.
- Authors: Bizhao Shi; Jiaxi Zhang; Zhuolun He; Xuechao Wei; Sicheng Li; Guojie Luo; Hongzhong Zheng; Yuan Xie.
- Publication: IEEE TCAD2023,42(11),3910–3924; DOI10.1109/TCAD.2023.3247621.
- Source: [institutional publication record](https://researchportal.hkust.edu.hk/en/publications/efficient-super-resolution-system-with-block-wise-hybridization-a/).
- Reviewed:2026-11-24. Status: **primary institutional abstract and metadata only**; full method not read.

## Contribution and relevance

Combines block-wise hybrid super-resolution, specialized Winograd transposed
convolution and quantization in an FPGA system. Joint upsampling/transform/
quantization optimization is already explicit prior art.

## Comparison boundary

The abstract does not establish whether scales, clipping or decisions are
calibrated, trained or observed per live group. Do not infer either an offline
restriction or coverage of a particular online support-conditioned rounding
mechanism without the full paper. Reported output rates are source-specific,
not a cost estimate for a different memory hierarchy.
