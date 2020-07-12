import colorsys as cs
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

Imagen1=Image.open('amapolas.jpg')
Imagen1=Imagen1.convert('RGB')
ArregloImagen1=np.array(Imagen1)
ArregloImagen1=ArregloImagen1.astype(int)

Imagen2=Image.open('montaje.png')
Imagen2 = Imagen2.convert('RGB')
ArregloImagen2=np.array(Imagen2)
ArregloImagen2=ArregloImagen2.astype(int)

ancho1,alto1,dim1=ArregloImagen1.shape

ancho2,alto2,dim2=ArregloImagen2.shape

if (ancho1,alto1) != (ancho2,alto2):
    print("Aviso: Las imágenes no son de igual tamaño, la imagen final sera recortada")

if ancho1 < ancho2:
    ancho=ancho1
else:
    ancho=ancho2
    
if alto1 < alto2:
    alto=alto1
else:
    alto=alto2

RGBnormalizado1=ArregloImagen1/255

RGBnormalizado2=ArregloImagen2/255

RGBnuevo=np.zeros((ancho,alto,3))

YIQ=np.zeros((ancho,alto,3))

YIQ_1=np.zeros((ancho,alto,3))

YIQ_2=np.zeros((ancho,alto,3))


def suma_clampeada_rgb(ArregloImagen1,ArregloImagen2,ancho,alto,RGBnuevo,RGBnormalizado1,RGBnormalizado2,YIQ_1,YIQ_2,YIQ):
    for x in range(ancho):
        for y in range(alto):
            for i in range(3):
                RGBnuevo[x,y,i] = ArregloImagen1[x,y,i] + ArregloImagen2[x,y,i]
                if RGBnuevo[x,y,i] > 255:
                   RGBnuevo[x,y,i] = 255
    RGBnuevo=RGBnuevo.astype('uint8')
    plt.imshow(RGBnuevo)
    plt.imsave('sumaclampeadaRGB.jpg',RGBnuevo)                                                                                                    

           
def suma_promediada_rgb(ArregloImagen1,ArregloImagen2,ancho,alto,RGBnuevo,RGBnormalizado1,RGBnormalizado2,YIQ_1,YIQ_2,YIQ):  
    for x in range(ancho):
        for y in range(alto):
            for i in range(3):
                RGBnuevo[x,y,i] = (ArregloImagen1[x,y,i] + ArregloImagen2[x,y,i])/2
                if RGBnuevo[x,y,i] > 255:
                   RGBnuevo[x,y,i] = 255
    RGBnuevo=RGBnuevo.astype('uint8')
    plt.imshow(RGBnuevo)
    plt.imsave('suma_promediada_RGB.jpg',RGBnuevo)            


def cuasiresta_clampeada_rgb(ArregloImagen1,ArregloImagen2,ancho,alto,RGBnuevo,RGBnormalizado1,RGBnormalizado2,YIQ_1,YIQ_2,YIQ):
    for x in range(ancho):
        for y in range(alto):
            for i in range(3):
                RGBnuevo[x,y,i] = ArregloImagen1[x,y,i] - ArregloImagen2[x,y,i]
                if RGBnuevo[x,y,i] < 0:
                   RGBnuevo[x,y,i] = 0
                
    RGBnuevo=RGBnuevo.astype('uint8')
    plt.imshow(RGBnuevo)
    plt.imsave('cuasiresta_clampeada_RGB.jpg',RGBnuevo)             
           

def cuasiresta_promediada_rgb(ArregloImagen1,ArregloImagen2,ancho,alto,RGBnuevo,RGBnormalizado1,RGBnormalizado2,YIQ_1,YIQ_2,YIQ):
    for x in range(ancho):
        for y in range(alto):
            for i in range(3):
                RGBnuevo[x,y,i] = (ArregloImagen1[x,y,i] - ArregloImagen2[x,y,i])/2 + 255/2
                if RGBnuevo[x,y,i] > 255:
                   RGBnuevo[x,y,i] = 255                
                if RGBnuevo[x,y,i] < 0:
                   RGBnuevo[x,y,i] =0
    RGBnuevo=RGBnuevo.astype('uint8')
    plt.imshow(RGBnuevo)
    plt.imsave('cuasiresta_promediada_rgb.jpg',RGBnuevo)   


def interpolacion_yiq(ArregloImagen1,ArregloImagen2,ancho,alto,RGBnuevo,RGBnormalizado1,RGBnormalizado2,YIQ_1,YIQ_2,YIQ):
    for x in range(ancho):
        for y in range(alto):           
            
            YIQ_1[x,y,:]=cs.rgb_to_yiq(RGBnormalizado1[x,y,0],RGBnormalizado1[x,y,1],RGBnormalizado1[x,y,2])               
            YIQ_2[x,y,:]=cs.rgb_to_yiq(RGBnormalizado2[x,y,0],RGBnormalizado2[x,y,1],RGBnormalizado2[x,y,2])
                        
            if  YIQ_1[x,y,0]+YIQ_2[x,y,0] != 0:
                YIQ[x,y,0]=(YIQ_1[x,y,0]+YIQ_2[x,y,0])/2
                YIQ[x,y,1]=(YIQ_1[x,y,0]*YIQ_1[x,y,1]+YIQ_2[x,y,0]*YIQ_2[x,y,1])/(YIQ_1[x,y,0]+YIQ_2[x,y,0])
                YIQ[x,y,2]=(YIQ_1[x,y,0]*YIQ_1[x,y,2]+YIQ_2[x,y,0]*YIQ_2[x,y,2])/(YIQ_1[x,y,0]+YIQ_2[x,y,0])             
            else:
                YIQ[x,y,0]=0
                YIQ[x,y,1]=0
                YIQ[x,y,2]=0
            
            RGBnuevo[x,y]=cs.yiq_to_rgb(YIQ[x,y,0],YIQ[x,y,1],YIQ[x,y,2])
    plt.imshow(RGBnuevo)
    plt.imsave('interpolacion_yiq.jpg',RGBnuevo)                
          

def if_brighter(ArregloImagen1,ArregloImagen2,ancho,alto,RGBnuevo,RGBnormalizado1,RGBnormalizado2,YIQ_1,YIQ_2,YIQ):
    for x in range(ancho):
        for y in range(alto):
            YIQ_1[x,y,:]=cs.rgb_to_yiq(RGBnormalizado1[x,y,0],RGBnormalizado1[x,y,1],RGBnormalizado1[x,y,2])               
            YIQ_2[x,y,:]=cs.rgb_to_yiq(RGBnormalizado2[x,y,0],RGBnormalizado2[x,y,1],RGBnormalizado2[x,y,2])
                        
            if YIQ_1[x,y,0]>=YIQ_2[x,y,0]:
                YIQ=YIQ_1
            else:
                YIQ=YIQ_2
                        
            RGBnuevo[x,y]=cs.yiq_to_rgb(YIQ[x,y,0],YIQ[x,y,1],YIQ[x,y,2])
    plt.imshow(RGBnuevo)
    plt.imsave('if_brighter.jpg',RGBnuevo)          

def if_darker(ArregloImagen1,ArregloImagen2,ancho,alto,RGBnuevo,RGBnormalizado1,RGBnormalizado2,YIQ_1,YIQ_2,YIQ):
    for x in range(ancho):
        for y in range(alto):
            YIQ_1[x,y,:]=cs.rgb_to_yiq(RGBnormalizado1[x,y,0],RGBnormalizado1[x,y,1],RGBnormalizado1[x,y,2])               
            YIQ_2[x,y,:]=cs.rgb_to_yiq(RGBnormalizado2[x,y,0],RGBnormalizado2[x,y,1],RGBnormalizado2[x,y,2])
                        
            if YIQ_1[x,y,0]<=YIQ_2[x,y,0]:
                YIQ=YIQ_1
            else:
                YIQ=YIQ_2
                        
            RGBnuevo[x,y]=cs.yiq_to_rgb(YIQ[x,y,0],YIQ[x,y,1],YIQ[x,y,2])
    plt.imshow(RGBnuevo)
    plt.imsave('if_darker.jpg',RGBnuevo)   
 
def default(ArregloImagen1,ArregloImagen2,ancho,alto,RGBnuevo,RGBnormalizado1,RGBnormalizado2,YIQ_1,YIQ_2,YIQ):
   return print("\n Opción Invalida")

def switch_demo(b,ArregloImagen1,ArregloImagen2,ancho,alto,RGBnuevo,RGBnormalizado1,RGBnormalizado2,YIQ_1,YIQ_2,YIQ):
    switcher = {
        1: suma_clampeada_rgb,
        2: suma_promediada_rgb,
        3: cuasiresta_clampeada_rgb,
        4: cuasiresta_promediada_rgb,
        5: interpolacion_yiq,
        6: if_brighter,
        7: if_darker ,
        }
    
    func=switcher.get(b, default )    
    func(ArregloImagen1,ArregloImagen2,ancho,alto,RGBnuevo,RGBnormalizado1,RGBnormalizado2,YIQ_1,YIQ_2,YIQ)

b=int(input('\n 1: suma_clampeada_rgb \n 2: suma_promediada_rgb \n 3: cuasiresta_clampeada_rgb \n 4: cuasiresta_promediada_rgb \n 5: interpolacion_yiq \n 6: if_brighter \n 7: if_darker \n Ingrese número entre 1 y 7: '))    

switch_demo(b,ArregloImagen1,ArregloImagen2,ancho,alto,RGBnuevo,RGBnormalizado1,RGBnormalizado2,YIQ_1,YIQ_2,YIQ)
    