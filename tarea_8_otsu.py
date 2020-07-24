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

a,b=np.histogram(px,bins=256)

probabilidad=a/(ancho*alto)

def suma_acumulativa(k,probabilidad):
    p=0
    for i in range(k):
        p+=probabilidad[i]
    return p

def medias_acumulativas(k,probabilidad):
    p=0
    for i in range(k):
        p+=i*probabilidad[i]
    return p

media_global=medias_acumulativas(len(a),probabilidad)

def varianza_entre_clases(k,probabilidad):
    p=((media_global*suma_acumulativa(k,probabilidad)-medias_acumulativas(k,probabilidad))**2)/(suma_acumulativa(k,probabilidad)*(1-suma_acumulativa(k,probabilidad)))
    return p

vector=[]
for i in range(1,len(a)+1):
    vector.append(varianza_entre_clases(i,probabilidad))
    
maximo=np.amax(vector)

k_max=np.where(vector==np.amax(vector))
kProm_max=int(np.mean(k_max))

NuevaImagen=np.zeros((ancho,alto))
for x in range(ancho):
    for y in range(alto):
        if ArregloImagen[x,y]<=kProm_max:
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
plt.imsave('segmentacion_otsu.jpg'+imagen,NuevaImagen,cmap="gray")              
            