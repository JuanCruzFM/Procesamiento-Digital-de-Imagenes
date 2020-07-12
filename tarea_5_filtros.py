import colorsys as cs
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

imagen123='amapolas.jpg'
img = Image.open(imagen123)


arrayimagen = np.array(img).astype(int)

ancho,alto,dim =arrayimagen.shape
 
YIQ=np.zeros((ancho,alto,dim)).astype(float)

RGBnormalizado=arrayimagen/255
 
for x in range(ancho):
    for y in range(alto):
        YIQ[x,y,:]=cs.rgb_to_yiq(RGBnormalizado[x,y,0],RGBnormalizado[x,y,1],RGBnormalizado[x,y,2])    

plt.subplot(1,2,1)
plt.imshow(YIQ[:,:,0],'gray')         
plt.imsave('original_gris.jpg',YIQ[:,:,0],cmap="gray")

def yiq_to_rgb(YIQ):
    RGBn=np.zeros((ancho,alto,dim))
    for x in range(ancho):
        for y in range(alto):
            RGBn[x,y,:]=cs.yiq_to_rgb(YIQ[x,y,0],YIQ[x,y,1],YIQ[x,y,2])
    return RGBn        

def Plano_3x3():
    A=np.ones((3,3))/9
    return A

def Plano_5x5():
    A=np.ones((5,5))/25
    return A

def Plano_7x7():
    A=np.ones((7,7))/49
    return A


def Bartlett_3x3():
    A=np.array([[1,2,1],
                [2,4,2],
                [1,2,1]])/16
    return A

def Bartlett_5x5():
    A=np.outer([1,2,3,2,1],[1,2,3,2,1])/81
    return A

def Bartlett_7x7():
    A=np.outer([1,2,3,4,3,2,1],[1,2,3,4,3,2,1])/256
    return A
           
def Gauss_3x3():
    A=np.array([[1,2,1],
                [2,4,2],
                [1,2,1]])/16
    return A

def Gauss_5x5():
    A=np.outer([1,4,6,4,1],[1,4,6,4,1])/256
    return A

def Gauss_7x7():
    A=np.outer([1,6,15,20,15,6,1],[1,6,15,20,15,6,1])/4096
    return A

def Laplaciano_v4():
    A=  np.array([[ 0,-1, 0],
                 [-1, 4,-1],
                 [ 0,-1, 0]])
    return A

def Laplaciano_v8():
    A=np.array([[-1,-1,-1],
                [-1, 8,-1],
                [-1,-1,-1]])
    return A
    
def Sobel():
    c=int(input("N: 0\nE: 1\nS: 2\nW: 3\nNE: 4\nSE: 5\nSW: 6\nNW: 7\n\nType your entry: "))
    if c < 3 and c >= 0: plano=0
    elif c < 8 and c >= 3: plano=1
    else: c=0
    
    N_NE= np.array([[[1,0],[2,1],[1,2]],
                 [[0,-1],[0,0],[0,1]],
                 [[-1,-2],[-2,-1],[-1,0]]])
    
    A=np.rot90(N_NE, -c, axes=(0,1))[:,:,plano]
    return A

def default():
   return print("\n Opción Invalida")

def switch_demo(b):
    switcher = {
        1: Plano_3x3,
        2: Plano_5x5,
        3: Plano_7x7,
        4: Bartlett_3x3,
        5: Bartlett_5x5,
        6: Bartlett_7x7,
        7: Gauss_3x3 ,
        8: Gauss_5x5 ,
        9: Gauss_7x7,
        10: Laplaciano_v4,
        11: Laplaciano_v8,
        12: Sobel
        }
    
    func=switcher.get(b, default )    
    return func()

b=int(input('1: Plano_3x3 \n 2: Plano_5x5 \n 3: Plano_7x7 \n 4: Bartlett_3x3 \n 5: Bartlett_5x5 \n 6: Bartlett_7x7 \n 7: Gauss_3x3 \n 8: Gauss_5x5 \n 9: Gauss_7x7 \n 10: Laplaciano_v4 \n 11: Laplaciano_v8 \n 12: Sobel \n Elija una opcion: '))

Kernel=switch_demo(b)

anchokernel,altokernel=np.shape(Kernel)

#for x in range(ancho):
#    for y in range(alto):
#        pixelnuevo=0
#        for i in range(anchokernel):
#            for j in range(altokernel):
#                ax= int(x-(anchokernel-1)/2 + i)
#                ay= int(y-(altokernel-1)/2 + j)
#                if ax < 0:
#                    ax=int(0)
#                if ay < 0:
#                    ay=int(0)
#                if ax >= ancho:
#                    ax=int(ancho-1)
#                if ay >= alto:
#                    ay=int(alto-1)         
#                pixelnuevo= pixelnuevo + YIQ[ax,ay,0]*Kernel[i,j]
#        if pixelnuevo > 1:
#            pixelnuevo=1
#        if pixelnuevo < 0:
#            pixelnuevo=0                  
#        YIQ[x,y,0]= pixelnuevo     

def convolucionar(Original, Kernel, ancho,alto):
    wIm=ancho
    hIm=alto
    K=Kernel
    wK, hK = np.shape(Kernel)
    for xIm in range(wIm):
        for yIm in range(hIm):
            px=0
            for xK in range(wK):
                for yK in range(hK):
                    ax = int(xIm-(wK-1)/2+xK)
                    ay = int(yIm-(hK-1)/2+yK)
                    
                    if ax < 0: ax=int(0)
                    if ax >= wIm: ax=int(wIm-1)
                    if ay < 0: ay=int(0)
                    if ay >= hIm: ay=int(hIm-1)
                    
                    if Original.ndim ==3: px = px + Original[ax,ay,0]*K[xK,yK]
                    if Original.ndim ==2: px = px + Original[ax,ay]*K[xK,yK]
                    if px < 0: px=0
                    if px > 1: px=1
            if Original.ndim ==3: Original[xIm,yIm,0]=px
            if Original.ndim ==2: Original[xIm,yIm]=px
    return Original




YIQnuevo=convolucionar(YIQ,Kernel,ancho,alto)

R=yiq_to_rgb(YIQnuevo)

gris=np.dot(R[...,:3], [0.299, 0.587, 0.114])

#
#RGBnuevo=np.zeros((ancho,alto,dim))
#
#for x in range(ancho):
#    for y in range(alto):
#        RGBnuevo[x,y,:]=cs.yiq_to_rgb(YIQ[x,y,0],YIQ[x,y,1],YIQ[x,y,2])
#
#gray = np.dot(RGBnuevo[...,:3], [0.299, 0.587, 0.114])

plt.subplot(1,2,2)
plt.imshow(gris,cmap='gray')        
plt.imsave('filtrada '+imagen123,gris,cmap="gray")

#RGBnuevo=RGBn.astype(int)            

#NImagen=Image.fromarray(RGBnuevo,'RGB')
#NuevaImagen=NImagen.convert('L')
#NuevaImagen.save('NuevaImagen.jpg')
#NuevaImagen.show()

        
        