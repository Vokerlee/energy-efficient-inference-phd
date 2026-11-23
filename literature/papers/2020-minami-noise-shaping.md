# Design of Noise Shaping Quantizers for Data Compaction of Neural Networks

- Citation key: `minami2020noiseshaping`.
- Authors: Yuki Minami; Tomohiro Ikeda; Masato Ishikawa.
- Publication: Transactions of the Society of Instrument and Control Engineers, volume 56, issue 9, pages 425–431, 2020; DOI `10.9746/sicetr.56.425`.
- Source: [publisher](https://www.jstage.jst.go.jp/article/sicetr/56/9/56_425/_article/-char/en).
- Reviewed: 2026-11-23. Status: **publisher abstract and bibliographic record only**.
- Reading focus: quantized object, information used to design the diffusion filter, and scope of the optimization.

## What it establishes

Studies neural-network weight quantization with noise-shaping filters. The
abstract describes selecting error-diffusion filters from learning-data
characteristics using a traveling-salesman-style optimization.

## Relevance to our goals

Filter design for neural quantization already has a dedicated literature.
Noise shaping and selecting a diffusion filter are not new principles.

## Limits and transfer conditions

The reviewed record concerns weights and learning-data-based preparation.
Complete recurrence, numerical assumptions and hardware costs were not checked.
Do not infer either coverage or absence of a calibration-free activation
controller from this abstract; full-text comparison remains open.
