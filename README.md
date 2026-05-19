# Multifractal Spectrum Analysis of Satellite Images from the Bahía Blanca Estuary

This project computes the **multifractal spectrum** of grayscale satellite images from the **Bahía Blanca Estuary (Ría de Bahía Blanca, Argentina)** using Hölder exponents and box-counting methods.

The objective is to characterize spatial heterogeneity and texture patterns in satellite imagery through multifractal analysis.

---

# Overview

The workflow implemented in this project consists of:

1. Loading and preprocessing grayscale satellite images.
2. Computing the local Hölder exponent ((\alpha)-image).
3. Quantizing the (\alpha)-image into equivalence classes.
4. Estimating the Hausdorff dimension using box-counting.
5. Constructing the multifractal spectrum (f(\alpha)).
6. Segmenting images using the (f(\alpha))-image and Otsu thresholding.

Different local measures are implemented:

* **Sum measure**
* **Maximum measure**
* **Absolute difference measure**

Each measure produces a different multifractal spectrum.

---

# Mathematical Background

For a local measure (\mu(B(x,r))) defined on a neighborhood centered at point (x) with radius (r), the Hölder exponent is defined as:

[
\alpha(x)=\lim_{r\to0}\frac{\log\mu(B(x,r))}{\log r}
]

Numerically, the exponent is obtained through a linear regression between:

[
\log \mu(B(x,r))
\quad \text{vs} \quad
\log r
]

The multifractal spectrum (f(\alpha)) is estimated using a box-counting approach.

---

# Repository Structure

```text
.
├── images/
│   ├── rec01.bmp
│   ├── rec10.bmp
│   ├── rec18.bmp
│   └── rec22.bmp
│
├── notebook/
│   └── multifractal_analysis.ipynb
│
├── results/
│   ├── alpha_images/
│   ├── f_alpha_images/
│   └── spectra/
│
├── README.md
└── requirements.txt
```

---

# Dependencies

The project uses the following Python libraries:

```python
numpy
Pillow
matplotlib
scikit-image
scipy
```

Install dependencies with:

```bash
pip install -r requirements.txt
```

or manually:

```bash
pip install numpy pillow matplotlib scikit-image scipy
```

---

# Usage

## 1. Load a grayscale image

```python
from PIL import Image
import numpy as np

image = Image.open('rec01.bmp').convert('L')
array_image = np.array(image).astype(int)
```

---

## 2. Compute the (\alpha)-image

Using the sum measure:

```python
alpha_image = Alfa_Imagen_Suma(array_image, 8)
```

Other available measures:

```python
Alfa_Imagen_Max()
Alfa_Imagen_DifAbs()
```

---

## 3. Quantize the (\alpha)-image

```python
VC, PC, C = MaxMin(alpha_image, 20)
```

---

## 4. Compute the multifractal spectrum

```python
fAlpha = f_alfa(alpha_image_quantized, VC, C)
```

---

## 5. Plot the multifractal spectrum

```python
plt.plot(VC, fAlpha, 'bo')
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$f(\alpha)$')
plt.show()
```

---

# Image Segmentation

The project also includes segmentation of the (f(\alpha))-image using Otsu thresholding:

```python
from skimage.filters import threshold_otsu

threshold = threshold_otsu(f_image)
binary = f_image < threshold
```

This allows identifying different regions of the estuary based on multifractal properties.

---

# Example Results

The following analyses were performed on multiple sectors of the Bahía Blanca estuary:

* `rec01.bmp`
* `rec10.bmp`
* `rec18.bmp`
* `rec22.bmp`

For each image, the following were computed:

* (\alpha)-image
* (f(\alpha))-image
* Multifractal spectrum
* Segmented image

---

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

# Potential Applications

* Remote sensing
* Estuarine morphology analysis
* Environmental monitoring
* Texture characterization
* Fractal and multifractal image analysis
* Geophysical image processing

---

# References

Some theoretical concepts used in this project are related to:

* Multifractal analysis
* Hölder exponents
* Hausdorff dimension
* Box-counting methods
* Image segmentation techniques

Suggested references:

1. Feder, J. *Fractals*
2. Falconer, K. *Fractal Geometry*
3. Mandelbrot, B. *The Fractal Geometry of Nature*

---

# Author

Juan Cruz
Physics Student / Computational Physics
Bahía Blanca, Argentina

---

# License

This project is released under the MIT License.

