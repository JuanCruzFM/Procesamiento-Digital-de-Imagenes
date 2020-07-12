from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


Imagen=Image.open('amapolas.jpg')


RGB=np.array(Imagen)

RGBnormalizado=RGB/255

ancho,alto,dim =RGB.shape

YIQ=np.zeros((ancho,alto,dim))

RGBnuevo=np.zeros((ancho,alto,dim))

A=np.array([[0.299,0.587,0.114],
           [0.595716,-0.274453,-0.321263],
           [0.211456,-0.522591,0.311135]])

B=np.array([[1,0.9563,0.6210],
            [1,-0.2721,-0.6474],
            [1,-1.1070,1.7046]])

alpha=float(input('Inserte valor alfa: '))
beta1=float(input('Inserte valor beta1: '))
beta2=float(input('Inserte valor beta2: '))



for x in range(ancho):
    for y in range(alto):
        YIQ[x,y]=np.matmul(A,RGBnormalizado[x,y])
        
        YIQ[x,y,0]=YIQ[x,y,0]*alpha
        YIQ[x,y,1]=YIQ[x,y,1]*beta1
        YIQ[x,y,2]=YIQ[x,y,2]*beta2
        
        if YIQ[x,y,0]>=1:
            YIQ[x,y,0]=1
        if YIQ[x,y,0]<=0:
            YIQ[x,y,0]=0
        if YIQ[x,y,1]>=0.5957:
            YIQ[x,y,1]=0.5957
        if YIQ[x,y,1]<=-0.5957:
            YIQ[x,y,1]=-0.5957
        if YIQ[x,y,2]>=0.5226:
            YIQ[x,y,2]=0.5226
        if YIQ[x,y,2]<=-0.5226:
            YIQ[x,y,2]=-0.5226
            
        RGBnuevo[x,y]=np.matmul(B,YIQ[x,y])
        
        if RGBnuevo[x,y,0] <=0:
            RGBnuevo[x,y,0]=0
        if RGBnuevo[x,y,1] <=0:
            RGBnuevo[x,y,1]=0    
        if RGBnuevo[x,y,2] <=0:
            RGBnuevo[x,y,2]=0
        if RGBnuevo[x,y,0] >=1:
            RGBnuevo[x,y,0]=1
        if RGBnuevo[x,y,1] >=1:
            RGBnuevo[x,y,1]=1    
        if RGBnuevo[x,y,2] >=1:
            RGBnuevo[x,y,2]=1
      



        
plt.subplot(1,2,1)
plt.imshow(RGB)
plt.subplot(1,2,2)
plt.imshow(RGBnuevo)

plt.imsave('nuevo.jpg',RGBnuevo)





