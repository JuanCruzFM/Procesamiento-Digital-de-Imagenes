# Multifractal Spectrum Analysis of Satellite Images from the Bahía Blanca Estuary

This project computes the **multifractal spectrum** of grayscale satellite images from the **Bahía Blanca Estuary (Ría de Bahía Blanca, Argentina)** using Hölder exponents and box-counting methods.

The objective is to characterize spatial heterogeneity and texture patterns in satellite imagery through multifractal analysis.

---

# Overview

The workflow implemented in this project consists of:

1. Loading and preprocessing grayscale satellite images.
2. Computing the local Hölder exponent ($\alpha$-image).
3. Quantizing the $\alpha$-image into equivalence classes.
4. Estimating the Hausdorff dimension using box-counting.
5. Constructing the multifractal spectrum $f(\alpha)$.
6. Segmenting images using the $f(\alpha)$-image and Otsu thresholding.

Different local measures are implemented:

* **Sum measure**
* **Maximum measure**
* **Absolute difference measure**

Each measure produces a different multifractal spectrum.

---

# Mathematical Background

For a local measure $\mu(B(x,r))$ defined on a neighborhood centered at point $x$ with radius $r$, the Hölder exponent is defined as:

$$
\alpha(x)=\lim_{r\to0}\frac{\log\mu(B(x,r))}{\log r}
$$

Numerically, the exponent is obtained through a linear regression between:

$$
\log \mu(B(x,r))
\quad \text{vs} \quad
\log r
$$

The multifractal spectrum $f(\alpha)$ is estimated using a box-counting approach.


# Notes on Performance

The current implementation prioritizes clarity over speed.

Some parts of the algorithm, particularly:

* neighborhood scanning,
* repeated box-counting,
* nested loops,

can become computationally expensive for large images.

Possible future improvements include:

* vectorization,
* parallelization,
* FFT/integral-image acceleration,
* GPU implementations,
* replacing explicit loops with optimized NumPy operations.

---




