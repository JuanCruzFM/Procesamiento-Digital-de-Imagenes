import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import math

Imagen=Image.open('amapolas.jpg').convert('L')
ArregloImagen=np.array(Imagen).astype(int)

ancho,alto =ArregloImagen.shape


N=4
M=4 #factores de escala

nuevo_ancho=math.floor(ancho/N)
nuevo_alto=math.floor(alto/M)

Resampleo=np.zeros((nuevo_ancho,nuevo_alto))

#downsampling constante
def downsampling_cte(nuevo_ancho,nuevo_alto,N,M,Resampleo):
    for x in range(nuevo_ancho):
        for y in range(nuevo_alto):
            Resampleo[x,y]=ArregloImagen[int(N*x),int(M*y)]
    return Resampleo


#downsampling bilineal 
def downsampling_bilineal(nuevo_ancho,nuevo_alto,N,M,Resampleo):   
    for x in range(nuevo_ancho):
        for y in range(nuevo_alto):
            Resampleo[x,y]= 0.25*(ArregloImagen[int(N*x),int(M*y)] + ArregloImagen[int(N*x + 1),int(M*y)] + ArregloImagen[int(N*x),int(M*y + 1)] + ArregloImagen[int(N*x + 1),int(M*y + 1)] )
    return Resampleo

#downsample bicubico

def kernel_bicubico(x,a):    
    if abs(x)<=1:
        return (a+2)*abs(x)**3 -(a+3)*abs(x)**2 + 1
    if abs(x)>1 and abs(x)<2:
        return a*abs(x)**3 - 5*a*abs(x)**2 +8*a*abs(x) - 4*a
    else:
        return 0

def downsampling_bicubico(nuevo_ancho,nuevo_alto,N,M,Resampleo):        
    for x in range(nuevo_ancho):
        for y in range(nuevo_alto):
    
                    px=0
                    for n in range(-1,3):
                        for m in range(-1,3):
                            if n+N*x<0 or n+N*x >= ancho:
                                X=N*x
                            else:
                                X=n+N*x
                            if m+M*y < 0 or m+M*y >= alto:
                                Y=M*y
                            else:
                                Y=m+M*y 
                            px+=kernel_bicubico(((N-1)/N)-n ,-0.5)*kernel_bicubico(((M-1)/M)-m,-0.5)*ArregloImagen[X,Y]
                            
                    Resampleo[x,y]=px         
    return Resampleo

def switch():
    opcion=int(input("Ingrese downsampling deseado:\n \n1: Constante \n2: Bilineal \n3: Bicubico \n\n " ))
    switcher = {
        1: downsampling_cte,
        2: downsampling_bilineal,
        3: downsampling_bicubico,
          }
    function = switcher.get(opcion, 0)
    return function

function=switch()
ImagenUp=function(nuevo_ancho,nuevo_alto,N,M,Resampleo)

plt.figure(figsize=(10,10), constrained_layout=False)
plt.subplot(1,2,1)
plt.title('original')
plt.imshow(ArregloImagen,cmap='gray')
plt.subplot(1,2,2)
plt.title('downsampling')
plt.imshow(ImagenUp,cmap='gray')                       
plt.imsave('downsampling.jpg',ImagenUp,cmap="gray")  



 

 