# Exploring Efficient Acceleration Architecture for Winograd-Transformed Transposed Convolution of GANs on FPGAs

- Citation key: `di2020winotransconv`.
- Authors: Xinkai Di; Hai-Gang Yang; Yiping Jia; Zhihong Huang; Ning Mao.
- Publication: Electronics2020,9(2),286; DOI10.3390/electronics9020286.
- Source: [publisher full text](https://www.mdpi.com/2079-9292/9/2/286).
- Reviewed:2026-11-24. Status: **full-text focused reading**, §2.3 and the stated architecture contributions.

## Contribution and relevance

Decomposes zero-insertion transposed convolution into smaller ordinary
convolutions, then applies Winograd with rearrangement, buffering and a custom
FPGA dataflow. Eliminating structural zeros together with convolution transforms
already has a hardware implementation.

## Comparison boundary

Zero insertion differs from nearest-neighbor repetition. This paper establishes
the broader transform/sparsity co-design comparator; the inspected passages do
not settle every duplication-specific support mask or live rounding rule.
Its implementation-specific performance figures do not establish another
array's energy or input/output scheduling cost.
