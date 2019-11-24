from text_similarity_function import text_similarity
import cv2
import os
import numpy as np
from PIL import Image
location=''

i=0
folder='a/'

for foldername in  os.listdir(folder):
    for filename in os.listdir(str(folder+'/'+foldername+'/')):
        img=cv2.imread(os.path.join(folder,foldername,filename))
        if img is not None:
            i+=1

similarity_matrix=np.zeros((i,i))
i=0
j=0
for foldername in  os.listdir(folder):
    for filename in os.listdir(str(folder+'/'+foldername+'/')):    
        img=Image.open(os.path.join(folder,foldername,filename))
        if img is not None:
            for filename2 in  os.listdir(folder):
                img2=Image.open(os.path.join(folder,filename2))
                if img2 is not None:
                    similarity_matrix[i][j]=text_similarity(img,img2)
                    j+=1
                    
        i+=1
    
print(similarity_matrix)

