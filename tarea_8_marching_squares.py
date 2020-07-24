import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import collections
import cv2

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

def m0(k):
    m=np.array([[0,0],
                [0,0]])
    m=np.rot90(m,k)
    return m

def m1(k):
    m=np.array([[0,1],
                [1,1]])
    m=np.rot90(m,k)
    return m

def m2(k):
    m=np.array([[1,0],
                [0,0]])
    m=np.rot90(m,k)
    return m    

def m3(k):
    m=np.array([[1,1],
                [1,1]])
    m=np.rot90(m,k)
    return m  

def m5(k):
    m=np.array([[1,0],
                [0,1]])
    m=np.rot90(m,k)
    return m  

def m4(k):
    m=np.array([[1,1],
                [0,0]])
    m=np.rot90(m,k)
    return m      
f=2
Marching=np.zeros((f*ancho,f*alto,3))

for x in range(ancho):
    for y in range(alto):
        for X in range(f):
            for Y in range(f):
                Marching[f*x+X,f*y+Y]=[255*NuevaImagen[x,y],255*NuevaImagen[x,y],255*NuevaImagen[x,y]]


for x in range(ancho-1):
    for y in range(alto-1):

        aux=np.array([[ NuevaImagen[x,y] , NuevaImagen[x+1,y] ],
                      [NuevaImagen[x,y+1] , NuevaImagen[x+1,y+1]]])

        if np.all(aux==m1(0)):
            cv2.line(Marching,(int(f*(y+0.5)),int(f*(x))),(int(f*(y)),int(f*(x+0.5))),(0,255,0),thickness=2)
            
        elif np.all(aux==m1(1)):
            cv2.line(Marching,(int(f*(y+0.5)),int(f*(x))),(int(f*(y+1)),int(f*(x+0.5))),(0,255,0),thickness=2)          

        elif np.all(aux==m1(2)):
            cv2.line(Marching,(int(f*(y+1)),int(f*(x+0.5))),(int(f*(y+0.5)),int(f*(x+1))),(0,255,0),thickness=2)

        elif np.all(aux==m1(3)):
            cv2.line(Marching,(int(f*(y)),int(f*(x+0.5))),(int(f*(y+0.5)),int(f*(x+1))),(0,255,0),thickness=2)            
            
        elif np.all(aux==m2(0)):
            cv2.line(Marching,(int(f*(y+0.5)),int(f*(x))),(int(f*(y)),int(f*(x+0.5))),(0,255,0),thickness=2)  
                      
        elif np.all(aux==m2(1)):
            cv2.line(Marching,(int(f*(y+0.5)),int(f*(x))),(int(f*(y+1)),int(f*(x+0.5))),(0,255,0),thickness=2)
            
        elif np.all(aux==m2(2)):
            cv2.line(Marching,(int(f*(y+1)),int(f*(x+0.5))),(int(f*(y+00.5)),int(f*(x+1))),(0,255,0),thickness=2)

        elif np.all(aux==m2(3)):
            cv2.line(Marching,(int(f*(y)),int(f*(x+0.5))),(int(f*(y+0.5)),int(f*(x+1))),(0,255,0),thickness=2)
            
        elif np.all(aux==m4(0)):
            cv2.line(Marching,(int(f*(y+0.5)),int(f*(x))),(int(f*(y+0.5)),int(f*(x+1))),(0,255,0),thickness=2)            

        elif np.all(aux==m4(1)):
            cv2.line(Marching,(int(f*(y)),int(f*(x+0.5))),(int(f*(y+1)),int(f*(x+0.5))),(0,255,0),thickness=2)
            
        elif np.all(aux==m4(2)):
            cv2.line(Marching,(int(f*(y+0.5)),int(f*(x))),(int(f*(y+0.5)),int(f*(x+1))),(0,255,0),thickness=2)       
        
        elif np.all(aux==m4(3)):
            cv2.line(Marching,(int(f*(y)),int(f*(x+0.5))),(int(f*(y+1)),int(f*(x+0.5))),(0,255,0),thickness=2)
            
        elif np.all(aux==m5(0)):
            cv2.line(Marching,(int(f*(y)),int(f*(x+0.5))),(int(f*(y+0.5)),int(f*(x+1))),(0,255,0),thickness=2)
            cv2.line(Marching,(int(f*(y+0.5)),int(f*(x))),(int(f*(y+1)),int(f*(x+0.5))),(0,255,0),thickness=2)
            
        elif np.all(aux==m5(1)):
            cv2.line(Marching,(int(f*(y)),int(f*(x+0.5))),(int(f*(y+0.5)),int(f*(x))),(0,255,0),thickness=2)
            cv2.line(Marching,(int(f*(y+0.5)),int(f*(x+1))),(int(f*(y+1)),int(f*(x+0.5))),(0,255,0),thickness=2)
            
Marching=Marching/255
            
plt.figure(figsize=(10,10), constrained_layout=False)
plt.subplot(1,2,1)
plt.title('original')
plt.imshow(ArregloImagen,cmap='gray')
plt.subplot(1,2,2)
plt.title('segmentacion')
plt.imshow(Marching)                       
plt.imsave('marching'+imagen,Marching)               