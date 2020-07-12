from matplotlib import pyplot as plt
from PIL import Image
import colorsys as cs
import numpy as np

Imagen=Image.open('original.png')
Imagen=Imagen.convert('RGB')
ArregloImagen=np.array(Imagen)
ArregloImagen=ArregloImagen.astype(int)
RGBnormalizado=ArregloImagen/255

Numero_contadores=int(input('Inserte el número de contadores deseado: '))

ancho,alto,dim=ArregloImagen.shape
YIQ=np.zeros((ancho,alto,dim))
Valores=[]

for x in range(ancho):
    for y in range(alto):
        YIQ[x,y,:]=cs.rgb_to_yiq(RGBnormalizado[x,y,0],RGBnormalizado[x,y,1],RGBnormalizado[x,y,2])
        Valores.append(YIQ[x,y,0])
    

peso=np.ones_like(Valores)/len(Valores)

plt.subplot(2,1,1)
plt.hist(Valores,bins=Numero_contadores, weights=peso ,range=[0,1])
plt.title('Imagen Original')
plt.xlabel('Luminancia')
plt.ylabel('Frecuencia relativa')
plt.xticks(np.linspace(0, 1, Numero_contadores+1))
plt.xlim(0,1)
plt.subplots_adjust(hspace=0.75)

YIQmodificado=np.zeros((ancho,alto,dim))
YIQmodificado[:,:,0]=np.sqrt(YIQ[:,:,0])
YIQmodificado[:,:,1]=YIQ[:,:,1]
YIQmodificado[:,:,2]=YIQ[:,:,2]

yiqn=np.ravel(YIQmodificado[:,:,0])
peso_n=np.ones_like(yiqn)/len(yiqn)

plt.subplot(2,1,2)
plt.hist(yiqn,bins=Numero_contadores,weights=peso_n,range=[0,1])
plt.title('Imagen Modificada')
plt.xlabel('Luminancia')
plt.ylabel('Frecuencia relativa')
plt.xticks(np.linspace(0, 1, Numero_contadores+1))
plt.xlim(0,1)

RGBnuevo=np.zeros((ancho,alto,dim))

for x in range(ancho):
    for y in range(alto):
        RGBnuevo[x,y,:]=cs.yiq_to_rgb(YIQmodificado[x,y,0],YIQmodificado[x,y,1],YIQmodificado[x,y,2])

plt.imsave('correcion_por_histograma.png',RGBnuevo)        




