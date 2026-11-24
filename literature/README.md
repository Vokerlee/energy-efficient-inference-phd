# Literature reviews

Current reviews connect published evidence to energy-efficient inference
research, centered on systolic hardware and portable numerical experiments.

## Topic reviews

| Topic | Status | Synthesis |
|---|---|---|
| 01 — Energy of compute-bound versus memory-bound inference | Reviewed 2026-11-08; expanded 2026-11-22 | [Review](topics/01-inference-energy.md) |
| 02 — Systolic arrays and alternative matrix multipliers | Reviewed 2026-11-08; expanded 2026-11-23 | [Review](topics/02-matrix-multiplier-architectures.md) |
| 03 — Efficient hardware im2col and convolution mapping | Reviewed 2026-11-08; expanded 2026-11-23 | [Review](topics/03-im2col-and-convolution-mapping.md) |
| 04 — Hardware-driven dynamic activation quantization | Reviewed 2026-11-08; expanded 2026-11-23 | [Review](topics/04-dynamic-activation-quantization.md) |
| 05 — Outliers and selective precision | Reviewed 2026-11-08; expanded 2026-11-15 | [Review](topics/05-outliers-and-selective-precision.md) |
| 06 — Range prediction and tracking | Reviewed 2026-11-08; expanded 2026-11-22 | [Review](topics/06-range-prediction-and-tracking.md) |
| 07 — Quantization and structured sparsity | Reviewed 2026-11-08; expanded 2026-11-22 | [Review](topics/07-quantization-and-structured-sparsity.md) |
| 08 — Accumulation and block-scale arithmetic | Reviewed 2026-11-08; expanded 2026-11-23 | [Review](topics/08-accumulation-and-block-scaling.md) |
| 09 — Adaptive low-rank computation | Reviewed 2026-11-08; expanded 2026-11-15 | [Review](topics/09-adaptive-low-rank-computation.md) |
| 10 — Fast matrix multiplication | Reviewed 2026-11-08; screened 2026-11-22 | [Review](topics/10-fast-matrix-multiplication.md) |
| 11 — Operator fusion and streaming inference | Reviewed 2026-11-08; expanded 2026-11-22 | [Review](topics/11-operator-fusion-and-streaming.md) |
| 12 — Hardware control for adaptive execution | Reviewed 2026-11-08; expanded 2026-11-23 | [Review](topics/12-adaptive-execution-control.md) |
| 13 — End-to-end quality under runtime approximation | Reviewed 2026-11-09; expanded 2026-11-23 | [Review](topics/13-end-to-end-quality.md) |
| 14 — Portable experiments and credible hardware evaluation | Reviewed 2026-11-09; expanded 2026-11-23 | [Review](topics/14-experimental-and-hardware-evaluation.md) |
| 15 — Modern accelerator memory hierarchies and matrix/vector execution | Reviewed 2026-11-14; expanded 2026-11-22 | [Review](topics/15-accelerator-memory-and-execution.md) |

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
Official technical documentation is indexed alongside papers, with its version
or access date and a distinct documentation-reading status.

| Key / review | Topic | Contribution to the review |
|---|---|---|
| [`zhang2019qpytorch`](papers/2019-zhang-qpytorch.md) | 13, 14 | QPyTorch methodology comparator; reading scope and limits in canonical note. |
| [`moreau2017qappa`](papers/2017-moreau-qappa.md) | 13, 14 | QAPPA methodology comparator; reading scope and limits in canonical note. |
| [`inci2022qappa`](papers/2022-inci-qappa.md) | 13, 14 | QAPPA methodology comparator; reading scope and limits in canonical note. |
| [`nair2023intfpqsim`](papers/2023-nair-int-fp-qsim.md) | 13, 14 | INT-FP-QSim methodology comparator; reading scope and limits in canonical note. |
| [`jiang2023arbitor`](papers/2023-jiang-arbitor.md) | 13, 14 | Arbitor methodology comparator; reading scope and limits in canonical note. |
| [`liu2023nnsmith`](papers/2023-liu-nnsmith.md) | 13, 14 | NNSmith methodology comparator; reading scope and limits in canonical note. |
| [`yahmed2022diverget`](papers/2022-yahmed-diverget.md) | 13, 14 | DiverGet methodology comparator; reading scope and limits in canonical note. |
| [`colbert2021upsampling`](papers/2021-colbert-upsampling.md) | 03, 11, 14 | Established nearest-neighbor coefficient folding and explicitly modeled time/energy. |
| [`sestito2021flexibleconv`](papers/2021-sestito-flexible-convolution.md) | 02, 03, 11 | Online zero-insertion remapping and reconfigurable FPGA convolution; separate from duplicate-input folding. |
| [`tsubone2024noiseshaping`](papers/2024-tsubone-training-data-noise-shaping.md) | 04, 06, 13 | Abstract-only: training-data-dependent weight error redistribution; adaptive noise shaping has existing neural precedents. |
| [`zhu2025passionsr`](papers/2025-zhu-passionsr.md) | 04, 13 | Calibrated UNet-and-VAE quantization; decoder precision is already studied. |
| [`deng2026latentquant`](papers/2026-deng-latentquant.md) | 13 | Abstract-only: reconstruction and frozen-policy compatibility can diverge during VAE QAT. |
| [`chen2025dcae`](papers/2025-chen-dc-ae.md) | 01, 03, 13, 14 | Compression/decoder tradeoffs; complete generation scope and explicit profiling assumptions. |
| [`gemmateam2024gemma2`](papers/2024-gemma-team-gemma2.md) | 01, 14, 15 | Prompt-encoder matrix work versus autoregressive decode; embedding storage versus executed operations. |
| [`karlin1994competitive`](papers/1994-karlin-competitive-randomized.md) | 12 | Established online state-change/caching theory; comparator assumptions must be explicit. |
| [`zhao2024atom`](papers/2024-zhao-atom.md) | 04, 05, 11, 12 | Online activation movement with calibrated channel identities; mixed-precision regularity and fusion. |
| [`zhang2026tilequant`](papers/2026-zhang-tilequant.md) | 04, 08, 12, 14 | Static weight-tile precision maps, compact layout and shape-adaptive execution. |
| [`wang2026ofgq`](papers/2026-wang-ofgq.md) | 02, 04, 12 | Adaptive-format and variable-cycle systolic synchronization; indexed abstract/introduction only. |
| [`huang2024tfmq`](papers/2024-huang-tfmq.md) | 04, 13 | Temporal conditioning sensitivity, isolated reconstruction and finite-timestep calibration. |
| [`huang2025temporalfeatures`](papers/2025-huang-temporal-features.md) | 11, 13 | Cached temporal features and explicitly offline strategy selection. |
| [`lee2025qlip`](papers/2025-lee-qlip.md) | 04, 12, 13 | Input-prompt-dependent layer/timestep precision using trained control and prepared quantizers. |
| [`simeoni2025dinov3`](papers/2025-simeoni-dinov3.md) | 01, 13, 14 | Modern vision backbone with distinct global/dense feature and downstream evaluation contracts. |
| [`chen2025sanasprint`](papers/2025-chen-sana-sprint.md) | 01, 03, 13 | Few-step diffusion with SANA-derived channel mixing and linear attention; denoiser scope must be explicit. |
| [`woo2023convnextv2`](papers/2023-woo-convnext-v2.md) | 03, 13, 14 | Depthwise/channel-mixing/normalization control; masked-pretraining sparsity is not inference sparsity. |
| [`guo2026dynacore`](papers/2026-guo-dynacore.md) | 02, 12, 15 | Precision-dependent reduction capacity with invariant output count and explicitly scheduled partial-sum reduction. |
| [`deepseek2026v4`](papers/2026-deepseek-v4-scale-widening.md) | 04, 08 | Direct prior art for losslessly absorbing fine source scales into a wider matrix operand format. |
| [`makhov2025prefilt`](papers/2025-makhov-prefilt.md) | 04, 13 | Noise spectrum, downstream filtering and a reconstruction bypass in fully quantized image restoration. |
| [`minami2020noiseshaping`](papers/2020-minami-noise-shaping.md) | 04, 13 | Existing diffusion-filter design for weight quantization; abstract-only comparison boundary is explicit. |
| [`yu2024dbfs`](papers/2024-yu-dbfs.md) | 02, 08, 12 | Width-dependent frequency, shift-add SIMD and explicit repacking costs; runtime configurability is established. |
| [`lu2025flexibleriscv`](papers/2025-lu-flexible-riscv-inference.md) | 03, 04, 12 | ISA-guided packing and local convolution lowering combined with configurable arithmetic; live-value selection remains a separate comparison. |
| [`chang2024bfpcim`](papers/2024-chang-bfp-cim.md) | 04, 07, 08, 12 | Direct hardware prior art for runtime quantization together with sparsity and exponent grouping. |
| [`zhang2025integerfpaccum`](papers/2025-zhang-integer-fp-accumulation.md) | 02, 08, 12 | Integer intermediates with floating outputs and a dynamically enabled normalizer are already described in hardware prior art. |
| [`khodamoradi2024ed`](papers/2024-khodamoradi-error-diffusion.md) | 04, 08, 13 | A concrete comparator for distinguishing local quantization error from error propagated through a model DAG. |
| [`ando2019dithernn`](papers/2019-ando-dither-nn.md) | 03, 04, 07, 13 | Spatial activation error feedback with a hardware implementation is established work, not an unexplored alternative to ordinary rounding. |
| [`facq2026microqonv`](papers/2026-facq-microqonv.md) | 03, 04, 08 | A direct baseline for combining quantization with convolution lowering; quantize-once-before-expansion is already established. |
| [`zhao2021overq`](papers/2021-zhao-overq.md) | 05, 07, 12 | Using spare zero slots for outliers, including hardware routing, is existing work. Compare against it before proposing an im2col-tail variant. |
| [`zhou2021implicitconv`](papers/2021-zhou-implicit-convolution.md) | 02, 03 | A strong implicit-lowering baseline; small spatial kernels do not inherently require issuing one short input-channel window at a time. |
| [`zhang2019compact`](papers/2019-zhang-compact.md) | 03, 07, 15 | Prior work already combines activation representation, convolution scheduling and local-memory energy. |
| [`li2025lmai2c`](papers/2025-li-lmai2c.md) | 03, 15 | A concrete reference for combining feeder reuse with alignment/padding and local-memory costs. |
| [`wu2025reusedim2col`](papers/2025-wu-data-reused-im2col.md) | 03 | A close hardware comparator for reducing feeder buffers and aligning repeated data in time. |
| [`chen2026sleepdynamic`](papers/2026-chen-sleep-dynamic-quantization.md) | 03, 04, 12, 15 | Hardware reuse plus dynamic quantization already exists; identify which layers, parameters and runtime choices actually adapt. |
| [`wong2026miao`](papers/2026-wong-miao.md) | 02, 08, 14 | Direct hardware/software precedent for changing intermediate precision with operand quantization. Compare its optimized datapath before claiming savings against uniform accumulation. |
| [`fasolino2026overflowdps`](papers/2026-fasolino-overflow-dps.md) | 08, 12 | Existing autonomous per-accumulation control rules out novelty of merely moving an overflow detector into hardware. |
| [`he2026bfpboundary`](papers/2026-he-bfp-accumulation-boundary.md) | 08, 14 | Close baseline for reducing accumulator precision and choosing chunk structure rather than only lowering operand width. |
| [`lo2023bucketgetter`](papers/2023-lo-bucket-getter.md) | 02, 08 | Direct hardware precedent for exponent grouping and deferred floating-point accumulation; these primitives cannot be presented as new. |
| [`andrulis2023raella`](papers/2023-andrulis-raella.md) | 04, 08, 12 | Demonstrates that data-dependent recovery can save energy without saving execution cycles. Useful for separating conversion, array activity and numerical fidelity. |
| [`zhang2021fast`](papers/2021-zhang-fast.md) | 02, 08, 12 | Established live precision decisions coupled to a native arithmetic implementation, with explicit conversion and multi-pass work. |
| [`kabaha2025compaqt`](papers/2025-kabaha-compaqt.md) | 12, 13 | Online refinement and claimed classification consistency already have formal-method precedents; this is not an offline-only algorithm. |
| [`veit2026kernelcontracts`](papers/2026-veit-kernel-contracts.md) | 13, 14 | Methodological comparator for separating an intended arithmetic change from an implementation failure in numerical experiments. |
| [`hu2025mant`](papers/2025-hu-m-ant.md) | 04, 06, 12, 15 | Streaming statistics and dedicated quantization hardware; preparation separated. |
| [`geng2026adana`](papers/2026-geng-adana.md) | 04, 12 | Counter-based online subtype selection and dedicated engine; focused paper review. |
| [`hsieh2025fpgasparsequantized`](papers/2025-hsieh-fpga-sparse-quantized.md) | 02, 07, 14 | Offline weight preparation and floating-point FPGA zero gating. |
| [`williams2009roofline`](papers/2009-williams-roofline.md) | 01 | Performance bottlenecks and operational intensity. |
| [`horowitz2014energy`](papers/2014-horowitz-computing-energy.md) | 01 | Historical component-energy and locality foundations. |
| [`chen2016eyeriss`](papers/2016-chen-eyeriss.md) | 01 | Matched-resource dataflow energy comparison. |
| [`jouppi2017tpu`](papers/2017-jouppi-tpu.md) | 01, 02, 15 | Systolic inference rooflines and utilization measurements. |
| [`ghane2018energyroofline`](papers/2018-ghane-energy-roofline.md) | 01 | Energy/power extension of roofline reasoning. |
| [`parashar2019timeloop`](papers/2019-parashar-timeloop.md) | 01, 02, 14 | Mapping-dependent activity and cost modeling. |
| [`wu2019accelergy`](papers/2019-wu-accelergy.md) | 01, 14 | Action-specific component-energy estimation. |
| [`jouppi2021tpuv4i`](papers/2021-jouppi-tpuv4i.md) | 01, 02, 15 | Production inference design and unequal energy scaling. |
| [`liu2022s2ta`](papers/2022-liu-s2ta.md) | 01, 02, 03, 07 | INT8 array buffering costs and sparsity overhead. |
| [`patel2024splitwise`](papers/2024-patel-splitwise.md) | 01 | Different inference phases and power sensitivities. |
| [`yang2024parttime`](papers/2024-yang-power-measurements.md) | 01, 14 | Validation limits of software-visible GPU power sensors. |
| [`gregersen2024inputpower`](papers/2024-gregersen-input-dependent-power.md) | 01 | Operand patterns affect GEMM power. |
| [`zhao2025viditq`](papers/2025-zhao-vidit-q.md) | 01, 04, 13 | Diffusion precision, conversion, latency, and quality. |
| [`chung2025mlenergy`](papers/2025-chung-ml-energy-benchmark.md) | 01, 14 | Generative-inference energy measurement and accounting. |
| [`chung2026joules`](papers/2026-chung-where-joules-go.md) | 01, 04 | Recent batch/precision energy trade-offs. |
| [`cai2026mobilenpu`](papers/2026-cai-mobile-npu-efficiency.md) | 01 | NPU phase behavior and host/control energy. |
| [`bonazzi2026tinyml`](papers/2026-bonazzi-tinyml-memory-wall.md) | 01 | Edge traffic bottlenecks and measurement-boundary caveats. |
| [`kung1982systolic`](papers/1982-kung-systolic-architectures.md) | 02 | Foundations of systolic reuse, regularity, and I/O balance. |
| [`chen2014diannao`](papers/2014-chen-diannao.md) | 02 | Reduction-oriented neural datapath and specialized buffering. |
| [`kwon2018maeri`](papers/2018-kwon-maeri.md) | 02 | Flexible interconnect as an alternative to rigid mappings. |
| [`chen2019eyerissv2`](papers/2019-chen-eyeriss-v2.md) | 02 | Flexible operand delivery, sparse execution, and utilization analysis. |
| [`qin2020sigma`](papers/2020-qin-sigma.md) | 02 | Flexible dot-product/reduction architecture for irregular matrices. |
| [`genc2021gemmini`](papers/2021-genc-gemmini.md) | 02, 03, 15 | Full-stack matrix accelerator, DMA, memory, and software integration. |
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
| [`song2020drq`](papers/2020-song-drq.md) | 04, 12 | Live regional precision with prepared thresholds; focused full text reviewed. |
| [`liu2024drift`](papers/2024-liu-drift.md) | 04, 12 | Distribution-based adaptation competitor; full text pending. |
| [`dettmers2022llmint8`](papers/2022-dettmers-llm-int8.md) | 05 | Activation outliers routed to a higher-precision feature path. |
| [`guo2023olive`](papers/2023-guo-olive.md) | 05 | Locally aligned outlier encoding with lossy victims. |
| [`ramachandran2025microscopiq`](papers/2025-ramachandran-microscopiq.md) | 05 | Weight-outlier representation and reconstruction hardware. |
| [`li2025svdquant`](papers/2025-li-svdquant.md) | 05, 09, 11, 13 | Diffusion outlier handling through a fused low-rank branch. |
| [`meng2026sharq`](papers/2026-meng-sharq.md) | 05, 07 | Online sparse–dense FP4 activation decomposition. |
| [`koster2017flexpoint`](papers/2017-koster-flexpoint.md) | 06 | Bounded-history exponent prediction and initialization. |
| [`dunning2019tdigest`](papers/2019-dunning-t-digest.md) | 06 | Streaming quantile reference; hardware cost remains open. |
| [`micikevicius2022fp8`](papers/2022-micikevicius-fp8-formats.md) | 06 | FP8 representation and the separate scale-selection problem. |
| [`li2026scalepredictor`](papers/2026-li-scale-predictor.md) | 06, 12 | Instance-aware prediction of deeper quantization scales. |
| [`chen2024mixq`](papers/2024-chen-mixq.md) | 06, 12 | Online outlier-prediction competitor; full text pending. |
| [`parashar2017scnn`](papers/2017-parashar-scnn.md) | 07 | Compressed sparse operands and specialized accumulation. |
| [`shomron2021sparq`](papers/2021-shomron-sparsity-aware-quantization.md) | 07, 12 | Runtime bit-window and zero-aware activation quantization. |
| [`wu2022sparseloop`](papers/2022-wu-sparseloop.md) | 07, 14 | Sparse action modeling with format and skipping overhead. |
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
| [`heusel2017fid`](papers/2017-heusel-frechet-inception-distance.md) | 13 | Distributional image quality, distinct from reference-output similarity. |
| [`li2023qdiffusion`](papers/2023-li-q-diffusion.md) | 13 | Full-trajectory calibration and diffusion activation structure. |
| [`he2023ptqd`](papers/2023-he-ptqd.md) | 13 | Quantization noise and trajectory-level correction. |
| [`huang2024vbench`](papers/2024-huang-vbench.md) | 13 | Multidimensional video quality and temporal consistency. |
| [`ryu2026qdrift`](papers/2026-ryu-q-drift.md) | 13 | Sampler-side correction and task-quality versus trajectory similarity. |
| [`chen2018tvm`](papers/2018-chen-tvm.md) | 14 | Portable computation, schedules, and extensible tensor primitives. |
| [`reddi2020mlperf`](papers/2020-reddi-mlperf-inference.md) | 14 | Scenario-defined performance and task-quality evaluation. |
| [`tschand2025mlperfpower`](papers/2025-tschand-mlperf-power.md) | 14 | Measured energy, instrumentation, and workload boundaries. |
| [`raj2025scalesimv3`](papers/2025-raj-scale-sim-v3.md) | 14 | Systolic timing, memory effects, and bounded validation evidence. |
| [`zhang2025spargeattn`](papers/2025-zhang-spargeattention.md) | 07, 11 | Online sparse/quantized attention and distinct QK/PV skipping decisions. |
| [`zhang2025sta`](papers/2025-zhang-sliding-tile-attention.md) | 07, 11 | Tile-aligned video attention with dense computation inside retained blocks. |
| [`yuan2025nsa`](papers/2025-yuan-native-sparse-attention.md) | 07, 11 | Natively trained hierarchical block selection; distinct from post-training replacement. |
| [`dai2026gsrs`](papers/2026-dai-growing-sparsity-reduced-search.md) | 07, 11 | Temporal sparse-mask adaptation with charged search and normalization timing. |
| [`hong2022cadyq`](papers/2022-hong-cadyq.md) | 04, 06, 12 | Learned patch/layer activation-precision selection. |
| [`venieris2023nawqsr`](papers/2023-venieris-nawq-sr.md) | 04, 06, 12 | Offline precision schedule versus live range estimation on an NPU. |
| [`abati2023resq`](papers/2023-abati-resq.md) | 04, 06, 12 | Error-bound-based dynamic residual activation quantization. |
| [`moitra2024pivot`](papers/2024-moitra-pivot.md) | 12 | Input-dependent execution path with charged second-pass fallback. |
| [`kim2025ditto`](papers/2025-kim-ditto.md) | 05, 06, 07, 12 | Hardware temporal-difference width selection and zero skipping. |
| [`heo2025exion`](papers/2025-heo-exion.md) | 05, 06, 07, 12 | Temporal FFN reuse and compacted output-sparse execution. |
| [`fan2025sqdm`](papers/2025-fan-sq-dm.md) | 05, 06, 07, 12 | Prepared low precision plus live sparse/dense channel routing. |
| [`kong2024cambricond`](papers/2024-kong-cambricon-d.md) | 05, 06, 07, 12 | Differential-execution competitor; full text still pending. |
| [`ni2021wrapnet`](papers/2021-ni-wrapnet.md) | 08 | Training-assisted narrow wrap-around accumulation. |
| [`sakr2019accumulation`](papers/2019-sakr-accumulation-width.md) | 08 | Statistical precision analysis with explicit distributional assumptions. |
| [`islamoglu2025mxdotp`](papers/2025-islamoglu-mxdotp.md) | 08 | Native scaled dot-product semantics and wide internal accumulation. |
| [`cuyckens2025mxrobot`](papers/2025-cuyckens-mx-robotics.md) | 08 | Implementation-specific MX accumulation and grouping costs. |
| [`kung2019packing`](papers/2019-kung-column-combining.md) | 02, 07 | Training-assisted filter packing and physical systolic utilization. |
| [`wang2021dualside`](papers/2021-wang-dual-side-sparse-tensor-core.md) | 02, 03, 07 | Bitmap im2col co-designed with dual-side sparse outer products. |
| [`rhu2018cdma`](papers/2018-rhu-compressing-dma.md) | 02, 07 | Transfer-boundary activation compression with explicit upstream bandwidth. |
| [`peltekis2023bic`](papers/2023-peltekis-systolic-bus-invert.md) | 01, 02 | BF16 systolic switching reduction, distinct from cycle skipping. |
| [`bamberg2023nnstats`](papers/2023-bamberg-neural-statistics-coding.md) | 01, 02 | Data-dependent memory/interconnect coding with explicit scope limits. |
| [`jouppi2023tpuv4`](papers/2023-jouppi-tpu-v4.md) | 15 | TensorCore memory hierarchy and measured CMEM effects. |
| [`google2026tpuarchitecture`](papers/2026-google-tpu-architecture.md) | 15 | Current TPU matrix/vector units, generation differences, and memory scopes. |
| [`jax2026tpupipelining`](papers/2026-jax-tpu-pipelining.md) | 15 | Explicit memory spaces, asynchronous transfers, and pipeline storage. |
| [`aws2026trainium2architecture`](papers/2026-aws-trainium2-architecture.md) | 15 | Operand/partial-sum buffers and precision-dependent logical tiles. |
| [`nvidia2026blackwelltmem`](papers/2026-nvidia-blackwell-tensor-memory.md) | 15 | Accumulator transport and matrix/vector epilogue resource competition. |
| [`hooper2025fgmp`](papers/2025-hooper-fgmp.md) | 04, 12 | Calibrated sensitivity with live activation-block precision selection and hardware support. |
| [`li2023aquant`](papers/2023-li-aquant.md) | 04 | Activation-dependent rounding borders targeting output error. |
| [`peters2023qbitopt`](papers/2023-peters-qbitopt.md) | 12 | Sensitivity-based training-time allocation and its activation extension. |
| [`moon2024igqvit`](papers/2024-moon-igq-vit.md) | 04, 12 | Live channel/token assignment to prepared quantizer groups. |
| [`zhao2025specquant`](papers/2025-zhao-specquant.md) | 05, 09 | Fourier-derived weight/residual decomposition; runtime interpretation requires care. |
| [`petersen2012matrixcookbook`](papers/2012-petersen-matrix-cookbook.md) | 13 | Linear covariance transport, quadratic-form expectations, and matrix norms. |
| [`jcgm2008gum`](papers/2008-jcgm-uncertainty-propagation.md) | 13 | First-order uncertainty propagation with explicit input correlations. |
| [`higham2019probabilistic`](papers/2019-higham-mary-probabilistic-rounding.md) | 08, 13 | Conditional probabilistic rounding bounds, distinct from additive-error RMS identities. |
| [`tramer2019slalom`](papers/2019-tramer-slalom.md) | 12, 14 | Projected verification of neural linear operators and preprocessing costs. |
| [`hardt2012adaptivesketches`](papers/2012-hardt-adaptive-sketches.md) | 12, 13 | Failure of fixed-input sketch guarantees under adaptive queries. |
| [`meyer2021hutchplusplus`](papers/2021-meyer-hutchplusplus.md) | 13 | Established stochastic trace identities and variance reduction. |
| [`santini2025probabilistic`](papers/2025-santini-probabilistic-quantization.md) | 04, 06, 12 | Live output-range prediction with calibrated interval parameters. |
| [`chen2026hutchsharp`](papers/2026-chen-hutchsharp.md) | 13 | Recent two-sided implicit norm estimation and dependency qualifications. |
| [`napolean2026sprobe`](papers/2026-napolean-sprobe.md) | 12, 14 | Quantized-GEMM fault verification and observation traffic. |
| [`nvidia2026cutlasskernels`](papers/2026-nvidia-cutlass-kernels.md) | 02, 03, 14 | Customizable CUDA kernel primitives and implicit convolution lowering. |
| [`pytorch2026customcuda`](papers/2026-pytorch-custom-cuda-operators.md) | 11, 14 | C++/CUDA operator integration and explicit graph coverage. |
| [`nvidia2026cublaslt`](papers/2026-nvidia-cublaslt-reference.md) | 14 | Configurable library comparator for custom GPU matrix kernels. |
| [`nvidia2026cudaredistributables`](papers/2026-nvidia-cuda-redistributables.md) | 14 | Versioned component archives and checksums for native CUDA toolchains. |
| [`xie2025mmasim`](papers/2025-xie-mma-sim.md) | 02 | Bit-accurate GPU matrix-unit modeling; abstract/metadata check, pinned to v1. |
| [`khattak2025tensorcoremodels`](papers/2025-khattak-tensor-core-models.md) | 02 | Instruction-arithmetic model scope; abstract/metadata check, pinned to v1. |
| [`jiang2023mistral7b`](papers/2023-jiang-mistral-7b.md) | 14 | Versioned architecture dimensions, GQA/window rules and output-head sizing. |
| [`dubey2024llama3`](papers/2024-dubey-llama-3.md) | 13, 14 | Architecture scaling references and dynamic FP8 quality-evaluation limits. |
| [`nag2025llvit`](papers/2025-nag-ll-vit.md) | 01, 02 | Estimated encoder-block energy split on an INT8 systolic FPGA baseline. |
| [`iyengar2026diffusionenergy`](papers/2026-iyengar-diffusion-energy-scaling.md) | 01, 14 | Whole-GPU diffusion energy fits and denoising FLOP attribution limits. |
| [`jain2026clear`](papers/2026-jain-clear-transformer-energy.md) | 01, 14 | Component replay for energy attribution and measurement-context limits. |
| [`zhang2026dstar`](papers/2026-zhang-dstar.md) | 04, 07, 12 | Live differential precision, prepared scales/masks and physical bit-slice mapping. |
| [`yoo2026apt`](papers/2026-yoo-apt.md) | 04, 07, 12 | Attention-guided skipping/precision with offline-profiled thresholds. |
| [`fu2026phantom`](papers/2026-fu-phantom.md) | 07, 12, 15 | Temporal token selection, dense compaction and explicit cache traffic. |
| [`walczak2026shatterquant`](papers/2026-walczak-shatterquant.md) | 02, 04, 08 | Prepared weight-block precision; activation width remains fixed. |
| [`calver2026runtimecertified`](papers/2026-calver-runtime-certified-attention.md) | 04, 12, 13 | Local attention certificates and tiered precision/fallback costs. |
| [`wei2026witcert`](papers/2026-wei-witcert.md) | 12, 13 | Runtime risk gates with explicitly different adaptive-query guarantees. |
| [`yang2026activationconcentration`](papers/2026-yang-activation-concentration.md) | 07, 14, 15 | Scalar-versus-column sparsity, threshold quality and mapping-specific costs. |
| [`yoon2026disc`](papers/2026-yoon-disc.md) | 07, 12, 15 | Token reuse and sparse attention co-designed with bank distribution. |
| [`jangda2026subcuber`](papers/2026-jangda-subcuber.md) | 10 | A direct implementation comparator for shape-dependent Strassen scheduling. Compiler generation and memory fusion are existing mechanisms. |
| [`chiu2025strassenquant`](papers/2025-chiu-strassen-dynamic-quantization.md) | 10 | The specific combination of Strassen, block quantization and ViT acceleration already has a prior description. |
| [`xie2026fp8fastmatmul`](papers/2026-xie-fp8-fast-matmul.md) | 10 | Coefficient choice and low-precision fast multiplication are an existing research intersection. |
| [`federici2025dip`](papers/2025-federici-dip.md) | 07, 12, 15 | Already couples approximation decisions with memory state; cache-aware sparsity alone is not an unoccupied problem. |
| [`silveria2025chipmunk`](papers/2025-silveria-chipmunk.md) | 07, 12, 15 | Grouped masks, compaction and temporal reuse already occur together. The extra prediction product must be charged even though it is smaller than the full operation. |
| [`cong2026rtlynx`](papers/2026-cong-rt-lynx.md) | 07, 11, 13 | A direct diffusion activation-sparsity comparator; fusion and norm compensation are already described. |
| [`chen2026wisparse`](papers/2026-chen-wisparse.md) | 07, 12, 13 | Weight-aware activation scoring and mixed sparsity allocation already have explicit prior art. |
| [`liu2026prox`](papers/2026-liu-prox.md) | 07, 12, 13 | An important example of sparsity plus quantization and of paying extra computation to avoid more expensive work. |
| [`aliev2026recache`](papers/2026-aliev-recache.md) | 12, 13 | Budget-aware caching is established; specifying a compute budget alone is not a new contribution. |
| [`lei2026budcache`](papers/2026-lei-budcache.md) | 12, 13 | Distinguishes prepared budgeted scheduling from per-input runtime decisions. |
| [`sao2026productrounding`](papers/2026-sao-product-aware-rounding.md) | 04, 08, 13 | Output-aware rounding and coordinated errors are explicit prior art, beyond activation-domain MSE. |
| [`tschannen2025siglip2`](papers/2025-tschannen-siglip2.md) | 14 | A frozen model family with final-task metrics for testing changes to vision activations. |
| [`xie2024sana`](papers/2024-xie-sana.md) | 14 | An architectural contrast for checking whether a matrix optimization remains relevant after attention complexity changes. |
| [`chen2024pixartsigma`](papers/2024-chen-pixart-sigma.md) | 14 | A reproducible diffusion family with explicit attention, projection and conditioning boundaries. |
| [`wu2025qwenimage`](papers/2025-wu-qwen-image.md) | 14 | A larger generator contrast with task requirements extending beyond paired latent similarity, including text rendering. |
| [`khaki2026vrsparsequant`](papers/2026-khaki-vr-sparsequant.md) | 04, 07, 11 | Direct prior art for quantizer-dependent gain selection, sparse residual correction and fused execution. |
| [`song2026roshift`](papers/2026-song-roshift.md) | 07, 09, 12 | Receiving-weight geometry and shared-projection Gram objectives already appear in activation-sparsity research. |
| [`zimmer2025sparseswaps`](papers/2025-zimmer-sparseswaps.md) | 07, 13 | A clear comparator against claiming that Gram-based mask optimization or pairwise interactions are new mathematical ideas. |
| [`wang2025was`](papers/2025-wang-was.md) | 07, 12, 13 | Weight-aware live masks, prepared allocation and kernel-level costs. |
| [`oconnor2016sigmadelta`](papers/2016-oconnor-sigma-delta.md) | 06, 07, 12 | Stateful quantized temporal updates and numerical equivalence scope. |
| [`kung2018adaptivetiling`](papers/2018-kung-adaptive-tiling.md) | 02, 07, 15 | Prepared sparse-weight tiling and fixed-array call reduction. |
| [`nvidia2026delayedscaling`](papers/2026-nvidia-delayed-scaling.md) | 06, 11 | Documented historical scaling, clipping and two-pass comparison boundary. |
| [`goubault2013unstabletests`](papers/2013-goubault-fluctuat-unstable-tests.md) | 13, 14 | Numerical decision stability and existing analysis of divergent execution paths. |
| [`titolo2018unstabletests`](papers/2018-titolo-eliminating-unstable-tests.md) | 13, 14 | Numerical decision stability and existing analysis of divergent execution paths. |
| [`titolo2020teststable`](papers/2020-titolo-test-stable-code.md) | 13, 14 | Numerical decision stability and existing analysis of divergent execution paths. |
| [`vaverka2020tfapprox`](papers/2020-vaverka-tfapprox.md) | 08, 14 | Accurate emulation, rounding acceptance or explicit compiler precision semantics. |
| [`brower2026emulationguarantees`](papers/2026-brower-emulation-guarantees.md) | 08, 14 | Accurate emulation, rounding acceptance or explicit compiler precision semantics. |
| [`ozaki2025fma`](papers/2025-ozaki-fma-matmul.md) | 08, 14 | Accurate emulation, rounding acceptance or explicit compiler precision semantics. |
| [`ozaki2026fma`](papers/2026-ozaki-fma-gemm.md) | 08, 14 | Accurate emulation, rounding acceptance or explicit compiler precision semantics. |
| [`dinechin2013ziv`](papers/2013-dinechin-ziv-test.md) | 08, 14 | Accurate emulation, rounding acceptance or explicit compiler precision semantics. |
| [`pytorch2026precisioncasts`](papers/2026-pytorch-inductor-precision-casts.md) | 08, 14 | Accurate emulation, rounding acceptance or explicit compiler precision semantics. |
| [`luo2026hap`](papers/2026-luo-hap.md) | 04, 08, 12 | Dynamic zero-point narrowing, bounded precision matching and an explicitly executed correction path. |
| [`meng2026arcquant`](papers/2026-meng-arcquant.md) | 04, 05, 08 | Abstract-only comparator: quantized residual channels expand the GEMM reduction dimension. |
| [`dewage2026componentsensitivity`](papers/2026-dewage-attention-component-sensitivity.md) | 04, 07, 13 | Attention roles and end-task sensitivity; intervention/transfer limits explicit. |
| [`parvathy2026sparqle`](papers/2026-parvathy-sparqle.md) | 04, 07, 13 | Dense low/sparse high activation bits, bitmap costs and selective clipping. |
| [`pan2025groupwinograd`](papers/2025-pan-group-quantized-winograd.md) | 04, 08, 10, 11 | Quantized Winograd and transform-scale preparation/runtime distinctions. |
| [`chen2023paw`](papers/2023-chen-paw-winograd.md) | 04, 08, 10, 11 | Quantized Winograd and transform-scale preparation/runtime distinctions. |
| [`krizhevsky2009cifar`](papers/2009-krizhevsky-cifar.md) | 14 | Dataset splits and archive identity for frozen-feature task evaluation. |
| [`andri2022tapwise`](papers/2022-andri-tap-wise-winograd.md) | 03, 04, 10, 11, 15 | Quantized Winograd hardware and producer/consumer rate matching. |
| [`hattink2020winograd`](papers/2020-hattink-winograd-memories.md) | 10, 11, 15 | Existing spatial partial-output retention and inverse/sum ordering. |
| [`nvidia2026nvdla`](papers/2026-nvidia-nvdla-winograd.md) | 02, 03, 15 | Official convolution pipeline, buffer and atomic-work documentation. |
| [`chikin2022balancing`](papers/2022-chikin-winograd-balancing.md) | 04, 10, 13 | Prepared transforms/coefficients and live decision boundaries. |
| [`protsenko2024winograd`](papers/2024-protsenko-quantization-friendly-winograd.md) | 04, 10, 13 | Prepared transforms/coefficients and live decision boundaries. |
| [`mori2024wino`](papers/2024-mori-wino-vidi-vici.md) | 04, 10, 13 | Prepared transforms/coefficients and live decision boundaries. |
| [`federici2026alignment`](papers/2026-federici-concentration-alignment.md) | 04, 10, 13 | Prepared transforms/coefficients and live decision boundaries. |
| [`guo2025winogradcim`](papers/2025-guo-winograd-hybrid-cim.md) | 01, 10, 15 | Design-specific transform/postprocessing power and hybrid CIM architecture. |
| [`ji2021winogradfusion`](papers/2021-ji-winograd-tile-fusion.md) | 03, 10, 11 | Existing layer-shape tile selection; full-paper reading remains pending. |
| [`park2025wins`](papers/2025-park-wins.md) | 03, 07, 10 | Prepared transform-domain structured pruning and sub-GEMM workload balance. |
| [`liu2018sparsewinograd`](papers/2018-liu-sparse-winograd.md) | 03, 07, 10 | Dynamic Winograd activation sparsity through changed ReLU placement and retraining. |
