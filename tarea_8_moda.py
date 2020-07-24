import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import collections

imagen='amapolas.jpg'
Imagen=Image.open(imagen).convert('L')
ArregloImagen=np.array(Imagen).astype(int)
ancho,alto =ArregloImagen.shape


px=[]
for x in range(ancho):
    for y in range(alto):
        px.append(ArregloImagen[x,y])

a,b =collections.Counter(px).most_common(2)
moda1=a[0]
moda2=b[0]

if moda1<moda2:
    moda_oscura=moda2
    moda_clara=moda1
else:
    moda_oscura=moda1
    moda_clara=moda2
    
NuevaImagen=np.zeros((ancho,alto))


for x in range(ancho):
    for y in range(alto):
        if abs(ArregloImagen[x,y]-moda_clara) < abs(ArregloImagen[x,y]-moda_oscura):
            NuevaImagen[x,y]=0
        else:
            NuevaImagen[x,y]=1
        
plt.figure(figsize=(10,10), constrained_layout=False)
plt.subplot(1,2,1)
plt.title('original')
plt.imshow(ArregloImagen,cmap='gray')
plt.subplot(1,2,2)
plt.title('segmentacion')
plt.imshow(NuevaImagen,cmap='gray')                       
plt.imsave('segmentacion_moda.jpg',NuevaImagen,cmap="gray")  