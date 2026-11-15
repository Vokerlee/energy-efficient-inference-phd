# CUDA component archives and reproducible native builds

- Citation key: `nvidia2026cudaredistributables`.
- Author: NVIDIA.
- Publication: CUDA 12.8 Linux installation documentation and CUDA 12.8.1 manifest.
- Source: [installation guide, §§9–9.2](https://docs.nvidia.com/cuda/archive/12.8.0/cuda-installation-guide-linux/index.html#tarball-and-zip-archive-deliverables), [12.8.1 manifest](https://developer.download.nvidia.com/compute/cuda/redist/redistrib_12.8.1.json).
- Reviewed: 2026-11-15. Status: **documentation focused reading**.
- Reading focus: component archives, manifest fields, checksum verification and CMake integration; Linux x86-64 compiler/runtime/header entries.

## Findings and relevance

NVIDIA publishes component archives with versioned URLs and checksums. The
manifest separates the toolkit release label from component versions: CUDA
12.8.1 includes NVCC 12.8.93 and cudart/CCCL 12.8.90. Section 9.1 describes
downloading, verifying, extracting and combining these archives; §9.2 discusses
FindCUDAToolkit integration.

This supports a repository-local compiler environment whose identity can be
recorded separately from Python package pins and the installed driver. Record
component checksums, compiler versions and generated GPU architectures when
comparing custom kernels.

## Limits

Archives are components, not a complete installer or a driver. A local toolkit
does not establish GPU availability, host compatibility or numerical fidelity.
Pinned sources support rebuilding; they do not guarantee identical binaries or
timings across hosts. This is build documentation, not energy or novelty evidence.
