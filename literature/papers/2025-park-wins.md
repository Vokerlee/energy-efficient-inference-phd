# WINS: Winograd Structured Pruning for Fast Winograd Convolution

- Citation key: `park2025wins`.
- Authors: Cheonjun Park; Hyun Jae Oh; Mincheol Park; Hyunchan Moon; Minsik Kim; Suhyun Kim; Myung Kuk Yoon; Won Woo Ro.
- Publication: ICCV2025, pp.22477–22487.
- Source: [publisher PDF](https://openaccess.thecvf.com/content/ICCV2025/papers/Park_WINS_Winograd_Structured_Pruning_for_Fast_Winograd_Convolution_ICCV_2025_paper.pdf).
- Reviewed:2026-11-24. Status: **full-text focused reading**, §§2.2,4–5; PDF retrieved separately after browser HTTP403.

## Contribution and relevance

Prunes transformed weight matrices in row/column units compatible with batched
GEMM. Balanced pruning addresses unequal sub-GEMM workloads; the adaptive
variant selects a layer strategy using estimated accuracy and speedup. The
paper evaluates fine-tuned models. Its GPU speedups do not measure array energy.

## Comparison boundary

Transform-domain structure and hardware utilization are established design
criteria. This is prepared weight pruning, not a demonstrated live activation
plane-skipping rule on an unchanged model. Compare workload balance and actual
matrix dimensions, rather than treating every transformed zero as equal work
saved. Broadly combining Winograd and structured sparsity is already covered.
