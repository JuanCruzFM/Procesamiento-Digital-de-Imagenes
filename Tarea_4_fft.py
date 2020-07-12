import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

imagen='untitled.png'
Imagen=Image.open(imagen).convert('L')
ArregloImagen=np.array(Imagen).astype(int)

fft=np.fft.fft2(ArregloImagen)

fshift=np.fft.fftshift(fft)

magnitud=np.log(1+np.abs(fshift))


plt.figure(figsize=(10,10), constrained_layout=False)
plt.subplot(1,2,1)
plt.title('original')
plt.imshow(ArregloImagen,cmap='gray')
plt.subplot(1,2,2)
plt.title('fft')
plt.imshow(magnitud,cmap='gray')
plt.imsave('modulo_fft ' +imagen,magnitud,cmap='gray')

   