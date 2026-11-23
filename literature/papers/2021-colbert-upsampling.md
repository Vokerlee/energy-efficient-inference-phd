# An Energy-Efficient Edge Computing Paradigm for Convolution-based Image Upsampling

- Citation key: `colbert2021upsampling`.
- Authors: Colbert, Ian; Kreutz-Delgado, Ken; Das, Srinjoy.
- Publication: arXiv2107.07647,2021; focused versionv1.
- Sources: [versioned full text](https://arxiv.org/html/2107.07647v1); [version history](https://arxiv.org/abs/2107.07647).
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Focus: Sections2.2,4.2,5.1; nearest-neighbor kernel folding and cost assumptions.

## Findings, relevance and limits

Transforms trained resize/subpixel convolutions into equivalent transposed convolutions. Section4.2 aggregates filter coefficients acting on duplicated nearest-neighbor inputs. For2x upsampling followed by3x3 convolution, the transformed arithmetic uses4/9 of the original dense MAC count. This is established algebra, not a new optimization merely because it is applied to a diffusion decoder.

The transformation is a one-time weight preparation. Section5.1 uses an optimistic compute/communication overlap model; energy includes compute, memory and constant-power terms. These modeled benefits are not measured energy for a different fixed-array/memory architecture.

Quantized coefficient sums, rounding, boundary handling, output phase layout and array packing require separate validation. Real-arithmetic equivalence does not imply bit-identical BF16 execution or establish live activation feedback/control. No implementation or reported result was reproduced for this review.
