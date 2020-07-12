import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


Imagen=Image.open('abejita.png').convert('L')
ArregloImagen=np.array(Imagen).astype(int)

ancho,alto =ArregloImagen.shape

N=5
M=5  #factores de escala

Resampleo=np.zeros((N*ancho,M*alto))


#upsampling constante
def upsampling_cte(ancho,alto,N,M,Resampleo):
    for x in range(ancho):
        for y in range(alto):
            for i in range(N):
                for j in range(M):
                    Resampleo[N*x+i,M*y+j]=ArregloImagen[x,y]
    return Resampleo 
    
#plt.imshow(Resampleo,cmap='gray')                       
#plt.imsave('upsampling-cte.jpg',Resampleo,cmap="gray")                
#               


#upsampling bilineal
def upsampling_bilineal(ancho,alto,N,M,Resampleo):
    for x in range(ancho):
        for y in range(alto):
            for i in range(N):
                for j in range(M):
                    if x+1 < ancho and y+1 < alto:
                        Resampleo[N*x+i,M*y+j]= (1-(i/N))*(1-(j/M))*ArregloImagen[x,y] + (1-(i/N))*(j/M)*ArregloImagen[x,y+1] + (i/N)*(1 - (j/M))*ArregloImagen[x+1,y] + (i/N)*(j/M)*ArregloImagen[x+1,y+1]
                    if x+1==ancho and y+1 < alto:
                        Resampleo[N*x+i,M*y+j]=(1-(j/M))*ArregloImagen[x,y] + (j/M)*ArregloImagen[x,y+1] 
                    if x+1<ancho and y+1==alto:
                         Resampleo[N*x+i,M*y+j]=(1-(i/N))*ArregloImagen[x,y] + (i/N)*ArregloImagen[x+1,y]
                    if x+1==ancho and y+1==alto:
                         Resampleo[N*x+i,M*y+j]=ArregloImagen[x,y]
    return Resampleo                             

#plt.imshow(Resampleo,cmap='gray')         
#plt.imsave('upsampling-bilineal.jpg',Resampleo,cmap="gray")          
 

def kernel_bicubico(x,a):    
    if abs(x)<=1:
        return (a+2)*abs(x)**3 -(a+3)*abs(x)**2 + 1
    if abs(x)>1 and abs(x)<2:
        return a*abs(x)**3 - 5*a*abs(x)**2 +8*a*abs(x) - 4*a
    else:
        return 0
    
def upsampling_bicubico(ancho,alto,N,M,Resampleo):
    for x in range(ancho):
        for y in range(alto):
            for i in range(N):
                for j in range(M):
                    px=0
                    for n in range(-1,3):
                        for m in range(-1,3):
                            if n+x<0 or n+x >= ancho:
                                X=x
                            else:
                                X=n+x
                            if m+y < 0 or m+y >= alto:
                                Y=y
                            else:
                                Y=m+y 
                            px+=kernel_bicubico((i/N)-n ,-0.5)*kernel_bicubico((j/M)-m,-0.5)*ArregloImagen[X,Y]
                            
                    Resampleo[N*x+i,M*y+j]=px                                                                    
    return Resampleo
#plt.imshow(Resampleo,cmap='gray')         
#plt.imsave('upsampling-bicubico.jpg',Resampleo,cmap="gray")          

def switch():
    opcion=int(input("Ingrese upsampling deseado:\n \n1: Constante \n2: Bilineal \n3: Bicubico \n\n " ))
    switcher = {
        1: upsampling_cte,
        2: upsampling_bilineal,
        3: upsampling_bicubico,
          }
    function = switcher.get(opcion, 0)
    return function

function=switch()
ImagenUp=function(ancho,alto,N,M,Resampleo)

plt.figure(figsize=(10,10), constrained_layout=False)
plt.subplot(1,2,1)
plt.title('original')
plt.imshow(ArregloImagen,cmap='gray')
plt.subplot(1,2,2)
plt.title('upsampling')
plt.imshow(ImagenUp,cmap='gray')                       
plt.imsave('upsampling.jpg',ImagenUp,cmap="gray")    