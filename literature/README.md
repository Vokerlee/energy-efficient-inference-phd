# Literature reviews

Current reviews connect published evidence to energy-efficient inference
research, centered on systolic hardware and portable numerical experiments.

## Topic reviews

| Topic | Status | Synthesis |
|---|---|---|
| 01 — Energy of compute-bound versus memory-bound inference | Reviewed 2026-11-08; 17 papers | [Review](topics/01-inference-energy.md) |

Other agreed topics are added when their reviews are performed.

## Reading the evidence

Paper files are canonical: reuse them across topics instead of copying reviews.
Each records its source/version, reading status, findings, relevance, and limits.
**Full-text focused reading** means the full text was accessed and the stated
sections were examined; it does not claim every section was exhaustively reviewed.

Separate physical measurements, implementation-based estimates, analytical
deductions, and proposals. A targeted search does not establish exhaustive
coverage or novelty. Search scope and outstanding questions live in each topic.

The shared [bibliography](references.bib) uses the citation keys recorded below.
Links point to original papers; original annotations here are our own writing.

## Paper index

All entries below received full-text focused reading on 2026-11-08.

| Key / review | Topic | Contribution to the review |
|---|---|---|
| [`williams2009roofline`](papers/2009-williams-roofline.md) | 01 | Performance bottlenecks and operational intensity. |
| [`horowitz2014energy`](papers/2014-horowitz-computing-energy.md) | 01 | Historical component-energy and locality foundations. |
| [`chen2016eyeriss`](papers/2016-chen-eyeriss.md) | 01 | Matched-resource dataflow energy comparison. |
| [`jouppi2017tpu`](papers/2017-jouppi-tpu.md) | 01 | Systolic inference rooflines and utilization measurements. |
| [`ghane2018energyroofline`](papers/2018-ghane-energy-roofline.md) | 01 | Energy/power extension of roofline reasoning. |
| [`parashar2019timeloop`](papers/2019-parashar-timeloop.md) | 01 | Mapping-dependent activity and cost modeling. |
| [`wu2019accelergy`](papers/2019-wu-accelergy.md) | 01 | Action-specific component-energy estimation. |
| [`jouppi2021tpuv4i`](papers/2021-jouppi-tpuv4i.md) | 01 | Production inference design and unequal energy scaling. |
| [`liu2022s2ta`](papers/2022-liu-s2ta.md) | 01 | INT8 array buffering costs and sparsity overhead. |
| [`patel2024splitwise`](papers/2024-patel-splitwise.md) | 01 | Different inference phases and power sensitivities. |
| [`yang2024parttime`](papers/2024-yang-power-measurements.md) | 01 | Validation limits of software-visible GPU power sensors. |
| [`gregersen2024inputpower`](papers/2024-gregersen-input-dependent-power.md) | 01 | Operand patterns affect GEMM power. |
| [`zhao2025viditq`](papers/2025-zhao-vidit-q.md) | 01 | Diffusion precision, conversion, latency, and quality. |
| [`chung2025mlenergy`](papers/2025-chung-ml-energy-benchmark.md) | 01 | Generative-inference energy measurement and accounting. |
| [`chung2026joules`](papers/2026-chung-where-joules-go.md) | 01 | Recent batch/precision energy trade-offs. |
| [`cai2026mobilenpu`](papers/2026-cai-mobile-npu-efficiency.md) | 01 | NPU phase behavior and host/control energy. |
| [`bonazzi2026tinyml`](papers/2026-bonazzi-tinyml-memory-wall.md) | 01 | Edge traffic bottlenecks and measurement-boundary caveats. |
