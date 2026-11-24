# Channel Balancing for Accurate Quantization of Winograd Convolutions

- Citation key: `chikin2022balancing`.
- Authors: Vladimir Chikin; Vladimir Kryzhanovskiy.
- Publication: CVPR 2022.
- Source: [primary source](https://openaccess.thecvf.com/content/CVPR2022/html/Chikin_Channel_Balancing_for_Accurate_Quantization_of_Winograd_Convolutions_CVPR_2022_paper.html).
- Reviewed: 2026-11-24. Status: **Full-text focused reading**, §§3–6. Direct browser fetch returned HTTP403; the publisher PDF was retrieved separately and text extracted locally.

## Contribution and relevance

Balances input/filter channels in the Winograd domain. Input scaling runs during inference while filter balancing is prepared offline. Coefficients can be calibrated with a few examples without additional training, then optionally trained further.

## Comparison boundary

No-training does not imply calibration-free current-block adaptation. Compare prepared channel balancing against any live rounding rule; applying coefficients during a forward pass is already established.

## Focused follow-up

Equation4 already computes a live maximum and scale for each transformed input
sample/tap; static scales are a separate calibrated alternative. Prepared
channel balancing therefore must not be confused with an entirely offline
activation quantizer. Section6 distinguishes static coefficient fusion from
extra elementwise work in the dynamic case. A new comparison must separate
current-range scale selection, prepared balancing, and the runtime rounding
rule; “dynamic Winograd activation quantization” alone is not a distinction.
