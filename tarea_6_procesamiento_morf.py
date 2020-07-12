import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

imagen='amapolas.jpg'
Imagen=Image.open(imagen).convert('L')
ArregloImagen=np.array(Imagen).astype(int)

ancho,alto =ArregloImagen.shape


N=3  #tamaño kernel

def base(ancho,alto,N,opcion,Im):
    NuevaImagen=np.zeros((ancho,alto))
    for x in range(ancho):
        for y in range(alto):
            px=[]
            for i in range(N):
                for j in range(N):
                    dx=x+i-int((N-1)/2)
                    dy=y+j-int((N-1)/2)
    
                    if dx < 0: dx=int(0)
                    if dx >= ancho: dx=int(ancho-1)
                    if dy < 0: dy=int(0)
                    if dy >= alto: dy=int(alto-1)

                    px.append(Im[dx,dy])

            if opcion==1: NuevaImagen[x,y]=np.amin(px)
            if opcion==2: NuevaImagen[x,y]=np.amax(px)
            if opcion==3: NuevaImagen[x,y]=np.amedian(px)

    return NuevaImagen

def procesamiento_morfologico(opc):
    if opc==1: ImagenProsc=base(ancho,alto,N,1,ArregloImagen) #erosion
    if opc==2: ImagenProsc=base(ancho,alto,N,2,ArregloImagen) #dilatacion
    if opc==3: ImagenProsc=base(ancho,alto,N,3,ArregloImagen) #mediana
    if opc==4: #apertura
        IP=base(ancho,alto,N,1,ArregloImagen)
        ImagenProsc=base(ancho,alto,N,2,IP)
    if opc==5:    #cierre
        IP=base(ancho,alto,N,2,ArregloImagen)
        ImagenProsc=base(ancho,alto,N,1,IP)
    if opc==6: #borde exterior
        ImagenProsc=base(ancho,alto,N,2,ArregloImagen)-ArregloImagen
    if opc==7:   ImagenProsc=ArregloImagen-base(ancho,alto,N,1,ArregloImagen)  #borde interior 
    if opc==8: #top-hat
         IP=base(ancho,alto,N,1,ArregloImagen)
         ImagenProsc=ArregloImagen-base(ancho,alto,N,2,IP)       
    return ImagenProsc    
        
opc=int(input('Ingrese caso: \n1: Erosion\n2: Dilatacion\n3: Mediana\n4: Apertura\n5: Cierre \n6: Borde exterior \n7: Borde interior \n8: Top-Hat\n\n  '))
NImagen=procesamiento_morfologico(opc)

plt.figure(figsize=(10, 10), constrained_layout=False)
plt.subplot(1,2,1)
plt.title('Original')
plt.imshow(ArregloImagen,cmap='gray')
plt.subplot(1,2,2)
plt.title('Procesamiento morfologico')
plt.imshow(NImagen,cmap='gray')                       
plt.imsave('procesamiento-morfologico '+imagen,NImagen,cmap="gray")  

                