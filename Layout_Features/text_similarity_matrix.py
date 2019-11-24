from text_similarity_function import text_similarity
import cv2
import os
import numpy as np
from PIL import Image
location=''

i=0
folder='b/'
lss=[]
for foldername in  os.listdir(folder):
    for filename in os.listdir(str(folder+'/'+foldername+'/')):
        lss.append(os.path.join(folder,foldername,filename))
        #img=Image.open(os.path.join(folder,foldername,filename))
        #if img is not None:
        i+=1

similarity_matrix=np.zeros((i,i))
i=0
j=0


for x in lss:
    img = Image.open(x)
    j=0

    for y in lss :
        img2=Image.open(y)
        if(i>=j):
            similarity_matrix[i][j]=text_similarity(img,img2)
            j+=1
    i+=1
print(similarity_matrix)

