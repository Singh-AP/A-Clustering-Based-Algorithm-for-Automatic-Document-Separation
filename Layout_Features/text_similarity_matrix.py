import text_similarity
import cv2
import os
import Image
location=''

i=0

for filename in  os.listdir(folder):
    img=cv2.imread(os.path.join(folder,filename))
    if img is not None:
        i+=1

similarity_matrix=np.zeros((i,i))
i=0
j=0
for filename in  os.listdir(folder):
    img=Image.open(os.path.join(folder,filename))
    if img is not None:
        for filename2 in  os.listdir(folder):
            img2=Image.open(os.path.join(folder,filename2))
            if img2 is not None:
                similarity_matrix[i][j]=text_similarity(img,img2)
                j+=1
                
    i+=1
 
print(similarity_matrix)

