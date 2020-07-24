import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import random

imagen='abejita.png'
Imagen=Image.open(imagen).convert('L')
ArregloImagen=np.array(Imagen).astype(int)
ancho,alto =ArregloImagen.shape


px=[]
for x in range(ancho):
    for y in range(alto):
        px.append(ArregloImagen[x,y])

lista_ordenada=sorted(px)        
largo_lista_ordenada=len(lista_ordenada)

if largo_lista_ordenada%2==0:
    corte=int(largo_lista_ordenada/2)
else:
    corte=int((1+largo_lista_ordenada)/2)   
   
px_corte=lista_ordenada[corte-1]    

parte_inferior = lista_ordenada[:corte] 
cantidad_de_cortes_parte_inferior=parte_inferior.count(px_corte)
parte_superior=lista_ordenada[corte:]
cantidad_de_cortes_parte_superior=parte_superior.count(px_corte)

NuevaImagen=np.zeros((ancho,alto))

u=0
l=0

for x in range(ancho):
    for y in range(alto):
        if ArregloImagen[x,y]<px_corte:
            NuevaImagen[x,y]=0
       
        elif ArregloImagen[x,y]>px_corte:
            NuevaImagen[x,y]=1

        elif ArregloImagen[x,y]==px_corte:
            if u<cantidad_de_cortes_parte_superior and l<cantidad_de_cortes_parte_inferior:
                if random.randint(0,1)==0:
                    NuevaImagen[x,y]=1
                    u+=1
                else:
                    NuevaImagen[x,y]=0
                    l+=1
            elif l<cantidad_de_cortes_parte_inferior:
                NuevaImagen[x,y]=0
                l+=1
            elif u<cantidad_de_cortes_parte_superior:
                NuevaImagen[x,y]=1
                u=+1
                                   

plt.figure(figsize=(10,10), constrained_layout=False)
plt.subplot(1,2,1)
plt.title('original')
plt.imshow(ArregloImagen,cmap='gray')
plt.subplot(1,2,2)
plt.title('segmentacion')
plt.imshow(NuevaImagen,cmap='gray')                       
plt.imsave('segmentacion_50-50.jpg',NuevaImagen,cmap="gray")                