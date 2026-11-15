# PyTorch custom CUDA operators and operator-graph coverage

- Citation key: `pytorch2026customcuda`.
- Author: PyTorch contributors.
- Publication: Living official documentation, accessed 2026-11-15; versioned source checked at v2.11.0.
- Source: [custom operators tutorial](https://docs.pytorch.org/tutorials/advanced/cpp_custom_ops.html), [export tutorial](https://docs.pytorch.org/tutorials/intermediate/torch_export_tutorial.html), [v2.11.0 registration source](https://github.com/pytorch/pytorch/blob/v2.11.0/torch/library.py), [release compatibility](https://pytorch.org/get-started/previous-versions/).
- Reviewed: 2026-11-15. Status: **documentation/source focused reading**.
- Reading focus: Registration, mutation contracts, numerical checks versus `opcheck`, and exported ATen graphs/decomposition.

## Findings and relevance

Custom operator registration provides a framework boundary for C++/CUDA code.
Exported operator graphs and decompositions support coverage inspection beyond
module hooks. Numerical comparison and registration checks serve different
purposes. The official release table pairs Torch 2.11.0 with torchvision 0.26.0.

## Limits

Current tutorials describe a moving documentation build; check exact APIs in
the chosen release. Export coverage, fused attention, shapes and mutation need
explicit tests. Registration alone does not replace hidden matrix products or
prove numerical equivalence. No custom operator was built in this review.
