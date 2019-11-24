from text_similarity_function import text_similarity
from PIL import Image
import os
import numpy as np
from LayoutFeaturesFunction import LayoutFeatures
def cluster_no(img_test,k):
    i=0
    # folder='b/'  # test images folder
    #lss=[]
    dist=[]
    labels=[]
    features1=LayoutFeatures(img_test) # Layout features of query image to be done
    with open('train_labels_and_url.txt','r') as files:
        count=0
        for line in files:
            count+=1
            print("line ",count)
            FileDir=line.split()[0]
            label=line.split()[1]
    # for foldername in  os.listdir(folder):
    #     for filename in os.listdir(str(folder+'/'+foldername+'/')):
            img=Image.open(FileDir)
            labels.append(label)      #extract labels from function for current image
            dist1=1-text_similarity(img,img_test)
            dist2=np.sum((features1-LayoutFeatures(img))**2) #spacing function  used here 
            dist.append(dist1**2+dist2)
            if count>100:
                break

    index=np.argsort(dist)
    maxx=np.zeros((17,1))
    for i in range(0,k):
        maxx[labels[index[i]]]+=1
    maxxx=-1
    maxxx=np.max(maxx)
    return maxxx 
    

             
print(cluster_no(Image.open('novel.png'),17))