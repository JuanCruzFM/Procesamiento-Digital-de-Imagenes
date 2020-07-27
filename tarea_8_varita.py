import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


im='amapolas.jpg'
image=Image.open(im).convert('L')
ImageArray=np.array(image)
width,heigth=ImageArray.shape

mask=np.zeros((width,heigth))

xSeed=int(input('y: '))
ySeed=int(input('x: '))

threshold=20

NumberSeeds=1
seeds=np.array([[xSeed,ySeed]])
mask[xSeed,ySeed]=1
aSeeds=np.array(ImageArray[xSeed,ySeed])

while NumberSeeds!=0:
     mean_seeds=np.mean(aSeeds)
             
     for n in range(NumberSeeds): 
           x=seeds[n,0]
           y=seeds[n,1]
           aSeeds=np.append(aSeeds, ImageArray[x,y])
           if y-1 >= 0 and mask[x,y-1]!=1:
                if abs(ImageArray[x,y-1]-mean_seeds)<threshold:
                    seeds=np.append(seeds,[[x,y-1]],0)
                    mask[x,y-1]=1
           if y+1 < heigth and mask[x,y+1]!=1:
                if abs(ImageArray[x,y+1]-mean_seeds)<threshold:
                    seeds=np.append(seeds,[[x,y+1]],0)
                    mask[x,y+1]=1
           if x-1 >=0 and mask[x-1,y]!=1:
                if abs(ImageArray[x-1,y]-mean_seeds)<threshold:
                    seeds=np.append(seeds,[[x-1,y]],0)
                    mask[x-1,y]=1
           if x+1 < width and mask[x+1,y]!=1:
                if abs(ImageArray[x+1,y]-mean_seeds)<threshold:
                    seeds=np.append(seeds,[[x+1,y]],0)
                    mask[x+1,y]=1 
                   
     oldseeds=np.arange(NumberSeeds)
     seeds=np.delete(seeds,oldseeds,0)
     NumberSeeds=np.shape(seeds)[0]                    

mean_seedsVal=np.mean(aSeeds)
mask=mask*mean_seeds
NewImage=np.zeros((width,heigth))
for x in range(width):
    for y in range(heigth):
        if mask[x,y]!=0:
            NewImage[x,y]=mask[x,y]
        else: 
            NewImage[x,y]=ImageArray[x,y]
            
NewImage=NewImage/255



  
plt.figure(figsize=(10,10), constrained_layout=False)        
plt.subplot(2,2,1) 
plt.imshow(mask, "gray")
plt.title('mascara')
plt.subplot(2,2,2) 
plt.imshow(NewImage, "gray")
plt.imsave('varita '+im,NewImage,cmap='gray')           