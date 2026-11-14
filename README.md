# Energy-Efficient Inference PhD

Research on energy-efficient neural network inference: literature reviews,
hypotheses, findings, and publications.

## Literature

The [literature index](literature/README.md) links topic syntheses, short paper
reviews, source versions, and the shared bibliography.

## Publications

The [publications directory](publications/README.md) contains manuscript sources
and build instructions.

## Experiments

Reproducible experiment code lives in the
[`tensor-inference-experiments`](https://github.com/Vokerlee/tensor-inference-experiments)
repository, included as a submodule at `code/tensor-inference-experiments`.
Each commit of this repository records the exact experiment-code revision.

Clone the repository with its submodules:

```sh
git clone --recurse-submodules https://github.com/Vokerlee/energy-efficient-inference-phd.git
```

For an existing checkout, or after checking out a historical revision:

```sh
git submodule update --init --recursive
```

## License

Unless otherwise noted, original written content and figures in this repository
are licensed under the [Creative Commons Attribution 4.0 International license
(CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). See [LICENSE](LICENSE)
for the full license text.

Third-party materials retain their own licenses and are excluded from this grant.
