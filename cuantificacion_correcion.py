import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

im='amapolas.jpg'
Imagen=Image.open(im).convert('L')
ImageArray=np.array(Imagen).astype(int)
width,heigth =ImageArray.shape

def cuantizacion_uniforme(width,heigth,ImageArray,N=None):
    if N==None:
        N=int(input('Numero de particiones deseado: '))
    Cuantizacion_uniforme=np.zeros((width,heigth))
    
    for x in range(width):
        for y in range(heigth):
            Cuantizacion_uniforme[x,y]=(np.floor(ImageArray[x,y]*(N/256))*(255/(N-1))).astype(int)
    return Cuantizacion_uniforme


#dithering
def dithering(width,heigth,ImageArray):
    num_bins=int(input('Numero de particiones deseado: '))    
    Dithering=np.zeros((width,heigth))
    noise=(np.random.rand(width,heigth)-0.5)*255/num_bins
    Image_noise=np.clip(ImageArray+noise,0,255)
    Dithering=cuantizacion_uniforme(width,heigth,Image_noise,num_bins)
    return Dithering

def difusion_error(width,heigth,ImageArray):
    num_bins=int(input('Numero de particiones deseado: ')) 
    salida=np.zeros((width,heigth))
    for x in range(width):
        error=0
        for y in range(heigth):
            salida[x,y]=(np.floor((ImageArray[x,y]+error)*(num_bins/256))*(255/(num_bins-1))).astype(int)
            salida[x,y]=np.clip(salida[x,y],0,255)
            error+= ImageArray[x,y] - salida[x,y] 
            
    return salida






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


ImagenUp=function(width,heigth,ImageArray)

plt.figure(figsize=(10,10), constrained_layout=False)
plt.subplot(1,2,1)
plt.title('original')
plt.imshow(ImageArray,cmap='gray')
plt.subplot(1,2,2)
plt.title('procesamiento')
plt.imshow(ImagenUp,cmap='gray')                       
plt.imsave('procesamiento '+im,ImagenUp,cmap="gray") 