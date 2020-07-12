import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math
import random

Imagen=Image.open('montaje.png').convert('L')
ArregloImagen=np.array(Imagen).astype(int)


ancho,alto =ArregloImagen.shape


#cuantizacion uniforme
def cuantizacion_uniforme(ancho,alto,ArregloImagen):
    N=int(input('Numero de particiones deseado: '))
    Cuantizacion_uniforme=np.zeros((ancho,alto))
    
    for x in range(ancho):
        for y in range(alto):
            for n in range(N):
                if ArregloImagen[x,y]>=255*(n)/N and ArregloImagen[x,y]<255*(n+1)/N:
                    Cuantizacion_uniforme[x,y]=(255*n)/N
    return Cuantizacion_uniforme

#plt.figure(figsize=(10, 10), constrained_layout=False)
#plt.subplot(1,2,1)
#plt.title('original')
#plt.imshow(ArregloImagen,cmap='gray')
#plt.subplot(1,2,2)
#plt.title('Cuantificcion constante')
#plt.imshow(Cuantizacion_uniforme,cmap='gray')                       
#plt.imsave('cuantificacion-uniforme.jpg',Cuantizacion_uniforme,cmap="gray")            


#dithering
def dithering(ancho,alto,ArregloImagen):    
    Dithering=np.zeros((ancho,alto))
    for x in range(ancho):
        for y in range(alto):
            if ArregloImagen[x,y] <= random.randint(0,255):
                Dithering[x,y]=0
            else:
                Dithering[x,y]=255
    return Dithering

#plt.figure(figsize=(10, 10), constrained_layout=False)
#plt.subplot(1,2,1)
#plt.title('original')
#plt.imshow(ArregloImagen,cmap='gray')
#plt.subplot(1,2,2)
#plt.title('Dithering')
#plt.imshow(Dithering,cmap='gray')                       
#plt.imsave('Dithering.jpg',Dithering,cmap="gray")         



#difusion de error
def difusion_error(ancho,alto,ArregloImagen):
    salida=np.zeros((ancho,alto))
    for x in range(ancho):
        error=0
        for y in range(alto):
            if ArregloImagen[x,y]+error <= 127: salida[x,y]=0
            else: salida[x,y]=255
            error+= ArregloImagen[x,y] - salida[x,y] 
    return salida
#        
#                
#plt.figure(figsize=(5,5), constrained_layout=False)
#plt.subplot(1,2,1)
#plt.title('original')
#plt.imshow(ArregloImagen,cmap='gray')
#plt.subplot(1,2,2)
#plt.title('error diffusion')
#plt.imshow(salida,cmap='gray')                       
#plt.imsave('error-diffusion.jpg',salida,cmap="gray")         

def switch():
    opcion=int(input("Ingrese upsampling deseado:\n \n1: cuantizacion uniforme \n2: dithering \n3: difusion error \n\n " ))
    switcher = {
        1: cuantizacion_uniforme,
        2: dithering,
        3: difusion_error,
          }
    function = switcher.get(opcion, 0)
    return function

function=switch()
ImagenUp=function(ancho,alto,ArregloImagen)

plt.figure(figsize=(10,10), constrained_layout=False)
plt.subplot(1,2,1)
plt.title('original')
plt.imshow(ArregloImagen,cmap='gray')
plt.subplot(1,2,2)
plt.title('procesamiento')
plt.imshow(ImagenUp,cmap='gray')                       
plt.imsave('procesamiento.jpg',ImagenUp,cmap="gray")  
     




