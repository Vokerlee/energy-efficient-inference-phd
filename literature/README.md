# Literature reviews

Current reviews connect published evidence to energy-efficient inference
research, centered on systolic hardware and portable numerical experiments.

## Topic reviews

| Topic | Status | Synthesis |
|---|---|---|
| 01 — Energy of compute-bound versus memory-bound inference | Reviewed 2026-11-08; 17 papers | [Review](topics/01-inference-energy.md) |
| 02 — Systolic arrays and alternative matrix multipliers | Reviewed 2026-11-08 | [Review](topics/02-matrix-multiplier-architectures.md) |
| 03 — Efficient hardware im2col and convolution mapping | Reviewed 2026-11-08 | [Review](topics/03-im2col-and-convolution-mapping.md) |
| 04 — Hardware-driven dynamic activation quantization | Reviewed 2026-11-08 | [Review](topics/04-dynamic-activation-quantization.md) |
| 05 — Outliers and selective precision | Reviewed 2026-11-08 | [Review](topics/05-outliers-and-selective-precision.md) |
| 06 — Range prediction and tracking | Reviewed 2026-11-08 | [Review](topics/06-range-prediction-and-tracking.md) |
| 07 — Quantization and structured sparsity | Reviewed 2026-11-08 | [Review](topics/07-quantization-and-structured-sparsity.md) |
| 08 — Accumulation and block-scale arithmetic | Reviewed 2026-11-08 | [Review](topics/08-accumulation-and-block-scaling.md) |
| 09 — Adaptive low-rank computation | Reviewed 2026-11-08 | [Review](topics/09-adaptive-low-rank-computation.md) |
| 10 — Fast matrix multiplication | Reviewed 2026-11-08 | [Review](topics/10-fast-matrix-multiplication.md) |
| 11 — Operator fusion and streaming inference | Reviewed 2026-11-08 | [Review](topics/11-operator-fusion-and-streaming.md) |
| 12 — Hardware control for adaptive execution | Reviewed 2026-11-08 | [Review](topics/12-adaptive-execution-control.md) |

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

Reading status, source version, and review date are recorded in each paper note.
Records awaiting full-text review are explicitly marked.

| Key / review | Topic | Contribution to the review |
|---|---|---|
| [`williams2009roofline`](papers/2009-williams-roofline.md) | 01 | Performance bottlenecks and operational intensity. |
| [`horowitz2014energy`](papers/2014-horowitz-computing-energy.md) | 01 | Historical component-energy and locality foundations. |
| [`chen2016eyeriss`](papers/2016-chen-eyeriss.md) | 01 | Matched-resource dataflow energy comparison. |
| [`jouppi2017tpu`](papers/2017-jouppi-tpu.md) | 01, 02 | Systolic inference rooflines and utilization measurements. |
| [`ghane2018energyroofline`](papers/2018-ghane-energy-roofline.md) | 01 | Energy/power extension of roofline reasoning. |
| [`parashar2019timeloop`](papers/2019-parashar-timeloop.md) | 01, 02 | Mapping-dependent activity and cost modeling. |
| [`wu2019accelergy`](papers/2019-wu-accelergy.md) | 01 | Action-specific component-energy estimation. |
| [`jouppi2021tpuv4i`](papers/2021-jouppi-tpuv4i.md) | 01, 02 | Production inference design and unequal energy scaling. |
| [`liu2022s2ta`](papers/2022-liu-s2ta.md) | 01, 02, 03, 07 | INT8 array buffering costs and sparsity overhead. |
| [`patel2024splitwise`](papers/2024-patel-splitwise.md) | 01 | Different inference phases and power sensitivities. |
| [`yang2024parttime`](papers/2024-yang-power-measurements.md) | 01 | Validation limits of software-visible GPU power sensors. |
| [`gregersen2024inputpower`](papers/2024-gregersen-input-dependent-power.md) | 01 | Operand patterns affect GEMM power. |
| [`zhao2025viditq`](papers/2025-zhao-vidit-q.md) | 01, 04 | Diffusion precision, conversion, latency, and quality. |
| [`chung2025mlenergy`](papers/2025-chung-ml-energy-benchmark.md) | 01 | Generative-inference energy measurement and accounting. |
| [`chung2026joules`](papers/2026-chung-where-joules-go.md) | 01, 04 | Recent batch/precision energy trade-offs. |
| [`cai2026mobilenpu`](papers/2026-cai-mobile-npu-efficiency.md) | 01 | NPU phase behavior and host/control energy. |
| [`bonazzi2026tinyml`](papers/2026-bonazzi-tinyml-memory-wall.md) | 01 | Edge traffic bottlenecks and measurement-boundary caveats. |
| [`kung1982systolic`](papers/1982-kung-systolic-architectures.md) | 02 | Foundations of systolic reuse, regularity, and I/O balance. |
| [`chen2014diannao`](papers/2014-chen-diannao.md) | 02 | Reduction-oriented neural datapath and specialized buffering. |
| [`kwon2018maeri`](papers/2018-kwon-maeri.md) | 02 | Flexible interconnect as an alternative to rigid mappings. |
| [`chen2019eyerissv2`](papers/2019-chen-eyeriss-v2.md) | 02 | Flexible operand delivery, sparse execution, and utilization analysis. |
| [`qin2020sigma`](papers/2020-qin-sigma.md) | 02 | Flexible dot-product/reduction architecture for irregular matrices. |
| [`genc2021gemmini`](papers/2021-genc-gemmini.md) | 02, 03 | Full-stack matrix accelerator, DMA, memory, and software integration. |
| [`munoz2023flexagon`](papers/2023-munoz-martinez-flexagon.md) | 02, 07 | Sparse dataflow flexibility and merging/reduction costs. |
| [`cho2017mec`](papers/2017-cho-mec.md) | 03 | Compact lowering with multiple smaller matrix multiplications. |
| [`dukhan2019indirect`](papers/2019-dukhan-indirect-convolution.md) | 03 | Pointer-based convolution without expanded activation copies. |
| [`liu2020ssta`](papers/2020-liu-sparse-systolic-tensor-array.md) | 03, 07 | Late hardware lowering reduces local-SRAM delivery demand. |
| [`selvam2021fuseconv`](papers/2021-selvam-fuseconv.md) | 03 | Depthwise utilization and the boundary between mapping and operator changes. |
| [`soltaniyeh2022spots`](papers/2022-soltaniyeh-spots.md) | 03, 07 | Pipelined hardware im2col, overlap reuse, and zero-block skipping. |
| [`fornt2023im2col`](papers/2023-fornt-on-the-fly-im2col.md) | 03, 11 | On-the-fly feeder with stride/dilation and explicit overhead accounting. |
| [`dai2021vsquant`](papers/2021-dai-vs-quant.md) | 04, 08 | Vector scales and their numerical/hardware trade-off. |
| [`keller2022vsqchip`](papers/2022-keller-vector-scaled-accelerator.md) | 04 | Prototype evidence for low-bit vector-scaled inference. |
| [`yao2022zeroquant`](papers/2022-yao-zeroquant.md) | 04 | Software runtime quantization and conversion-overhead baseline. |
| [`rouhani2023mx`](papers/2023-rouhani-microscaling.md) | 04, 08 | Microscaling representation and conversion foundations. |
| [`abdelmaksoud2026adip`](papers/2026-abdelmaksoud-adip.md) | 04 | Precision-scalable systolic execution; controller distinction. |
| [`fasoli2026microscaling`](papers/2026-fasoli-microscaling-limits.md) | 04 | Scale quantization can defeat finer grouping. |
| [`song2020drq`](papers/2020-song-drq.md) | 04, 12 | Priority dynamic-quantization competitor; full text pending. |
| [`liu2024drift`](papers/2024-liu-drift.md) | 04, 12 | Distribution-based adaptation competitor; full text pending. |
| [`dettmers2022llmint8`](papers/2022-dettmers-llm-int8.md) | 05 | Activation outliers routed to a higher-precision feature path. |
| [`guo2023olive`](papers/2023-guo-olive.md) | 05 | Locally aligned outlier encoding with lossy victims. |
| [`ramachandran2025microscopiq`](papers/2025-ramachandran-microscopiq.md) | 05 | Weight-outlier representation and reconstruction hardware. |
| [`li2025svdquant`](papers/2025-li-svdquant.md) | 05, 09, 11 | Diffusion outlier handling through a fused low-rank branch. |
| [`meng2026sharq`](papers/2026-meng-sharq.md) | 05, 07 | Online sparse–dense FP4 activation decomposition. |
| [`koster2017flexpoint`](papers/2017-koster-flexpoint.md) | 06 | Bounded-history exponent prediction and initialization. |
| [`dunning2019tdigest`](papers/2019-dunning-t-digest.md) | 06 | Streaming quantile reference; hardware cost remains open. |
| [`micikevicius2022fp8`](papers/2022-micikevicius-fp8-formats.md) | 06 | FP8 representation and the separate scale-selection problem. |
| [`li2026scalepredictor`](papers/2026-li-scale-predictor.md) | 06, 12 | Instance-aware prediction of deeper quantization scales. |
| [`chen2024mixq`](papers/2024-chen-mixq.md) | 06, 12 | Online outlier-prediction competitor; full text pending. |
| [`parashar2017scnn`](papers/2017-parashar-scnn.md) | 07 | Compressed sparse operands and specialized accumulation. |
| [`shomron2021sparq`](papers/2021-shomron-sparsity-aware-quantization.md) | 07, 12 | Runtime bit-window and zero-aware activation quantization. |
| [`wu2022sparseloop`](papers/2022-wu-sparseloop.md) | 07 | Sparse action modeling with format and skipping overhead. |
| [`kam2025panacea`](papers/2025-kam-panacea.md) | 07 | Asymmetric quantization and structured bit-slice opportunities. |
| [`blanchard2020blockfma`](papers/2020-blanchard-block-fma.md) | 08 | Numerical semantics of mixed-precision block accumulation. |
| [`colbert2023a2q`](papers/2023-colbert-a2q.md) | 08 | Overflow bounds and training-constrained accumulation. |
| [`colbert2024a2qplus`](papers/2024-colbert-a2q-plus.md) | 08 | Tighter accumulator constraints and initialization trade-offs. |
| [`cuyckens2025mxreduction`](papers/2025-cuyckens-mx-reduction.md) | 08 | Microscaling reduction-tree cost and NPU integration. |
| [`halko2011randomized`](papers/2011-halko-randomized-decompositions.md) | 09 | Cost and accuracy of randomized subspace discovery. |
| [`garcia2025rana`](papers/2025-garcia-rana.md) | 09 | Input-dependent rank allocation with learned adapters. |
| [`wang2025nalr`](papers/2025-wang-noise-adaptive-low-rank.md) | 09 | Noise-conditioned rank schedules for diffusion. |
| [`chang2025palu`](papers/2025-chang-palu.md) | 09 | Projection/reconstruction trade-offs in a memory-focused workload. |
| [`demmel2007stable`](papers/2007-demmel-fast-linear-algebra.md) | 10 | Stability assumptions for fast numerical algorithms. |
| [`huang2016strassen`](papers/2016-huang-strassen-reloaded.md) | 10 | Practical Strassen fusion and workspace costs. |
| [`lavin2016fastconv`](papers/2016-lavin-fast-convolution.md) | 10 | Small-filter convolution with transform overhead. |
| [`barabasz2019winograd`](papers/2019-barabasz-winograd-error.md) | 10 | Numerical cost of larger/faster convolution transforms. |
| [`fawzi2022alphatensor`](papers/2022-fawzi-alphatensor.md) | 10 | Algorithm search with domain and hardware constraints. |
| [`alwani2016fused`](papers/2016-alwani-fused-layer-cnn.md) | 11 | Hardware inter-layer fusion and local intermediate storage. |
| [`dao2022flashattention`](papers/2022-dao-flashattention.md) | 11 | Tiled attention with bounded intermediate storage. |
| [`nayak2024fusemax`](papers/2024-nayak-fusemax.md) | 11 | Attention mapping across matrix and reduction stages. |
| [`shah2024flashattention3`](papers/2024-shah-flashattention-3.md) | 11 | Low-precision attention with asynchronous execution. |
| [`zadouri2026flashattention4`](papers/2026-zadouri-flashattention-4.md) | 11 | Pipeline redesign when matrix and nonlinear throughput scale differently. |
| [`albericio2016pragmatic`](papers/2016-albericio-bit-pragmatic.md) | 12 | Data-dependent hardware work and synchronization costs. |
| [`wang2019haq`](papers/2019-wang-haq.md) | 12 | Offline hardware-aware mixed-precision search. |
| [`yu2021anyprecision`](papers/2021-yu-any-precision.md) | 12 | Model preparation for selectable runtime precision. |
