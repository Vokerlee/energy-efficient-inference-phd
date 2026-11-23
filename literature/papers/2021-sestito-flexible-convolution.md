# Design of Flexible Hardware Accelerators for Image Convolutions and Transposed Convolutions

- Citation key: `sestito2021flexibleconv`.
- Authors: Sestito, Cristian; Spagnolo, Fanny; Perri, Stefania.
- Publication: Journal of Imaging7(10),210,2021.
- Source: [publisher full text](https://www.mdpi.com/2313-433X/7/10/210); DOI10.3390/jimaging7100210.
- Reviewed: 2026-11-23. Status: **full-text focused reading**.
- Focus: Sections2–3: transposed-convolution subfilters, input remapping and zero insertion.

## Findings, relevance and limits

Surveys transposed-convolution decomposition and introduces online input remapping that avoids physically expanding the input with zeros. A runtime-reconfigurable FPGA architecture supports different convolution modes/kernel sizes. Thus avoiding zero multiplications and implementing convolution/transposed-convolution hardware are existing contributions.

The paper mentions nearest-neighbor insertion in its background, but Section3's described numerical equivalence is specifically to zero-insertion transposed convolution. Do not conflate it with aggregating coefficients for duplicated nearest-neighbor samples. Hardware mode reconfiguration is distinct from selecting quantization rules from current activation statistics.

Output ordering, subfilter balance and buffers are explicit comparison issues. Reported FPGA resource/energy results do not transfer to another systolic geometry or establish a calibration-free precision controller. Results were not reproduced here.
