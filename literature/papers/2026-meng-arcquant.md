# ARCQuant: Boosting NVFP4 Quantization with Augmented Residual Channels for LLMs

- Citation key: `meng2026arcquant`.
- Authors: Haoqian Meng; Yilun Luo; Yafei Zhao; Wenyuan Liu; Peng Zhang; Xindian Ma.
- Source: [primary source](https://aclanthology.org/2026.acl-long.388/).
- Publication: ACL2026, pp.8609–8623; DOI10.18653/v1/2026.acl-long.388.
- Reviewed: 2026-11-24. Status: **primary abstract and publication metadata only**.

## Findings and relevance

Adds quantized residual activation channels to the reduction dimension while
retaining a unified NVFP4 format and standard GEMM execution. Residual recovery
inside a single expanded matrix product therefore has prior art; the absence
of a separate kernel does not mean no additional multiply/accumulate work.

## Limits

The abstract reports LLM quality and GPU deployment. It does not establish
calibration independence, a source-before-im2col scheme, a no-extra-MAC design
or benefits on this project's target array. These details require full-method
comparison before transferring the mechanism. No reported result was reproduced.
