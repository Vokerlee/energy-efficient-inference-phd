# CIFAR-10 and CIFAR-100 datasets

- Citation key: `krizhevsky2009cifar`.
- Authors: Alex Krizhevsky; Vinod Nair; Geoffrey Hinton.
- Source: [primary source](https://www.cs.toronto.edu/~kriz/cifar.html).
- Publication: official dataset documentation; linked technical report by Alex Krizhevsky, 2009.
- Reviewed: 2026-11-24. Status: **primary dataset documentation reviewed; linked report not read**.

## Dataset and evaluation role

CIFAR100 has100 fine classes, with500 training and100 test images per class.
Official Python archive MD5 is `eb9058c3a382ffc7106e4002c42a8d85`. The page links
the collection-method report and defines label/split conventions.

## Relevance and limits

Provides a fixed recognition task for frozen-feature quantization evaluation.
A labeled reference gallery is an evaluator component; it must not become
activation calibration or policy selection data. Report exact selections,
preprocessing, gallery size, neighbor/vote rules and query allocation. Accuracy
in this constructed frozen-feature task is not official ImageNet accuracy or
a hardware energy measurement.
