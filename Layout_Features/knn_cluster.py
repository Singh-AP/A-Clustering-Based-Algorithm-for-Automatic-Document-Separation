from text_similarity_function import text_similarity
from PIL import Image
import os
import numpy as np
def cluster_no(img_test,test_folder,k):
    i=0
    folder='b/'
    #lss=[]
    dist=[]
    features1=[] 
    for foldername in  os.listdir(folder):
        for filename in os.listdir(str(folder+'/'+foldername+'/')):
            img=Image.open(os.path.join(folder,foldername,filename))
            #labels.append(img.label()) 
            dist1=1-text_similarity(img,img_test)
            dist2=np.sum((features1-features(img))**2) 
            dist.append(dist1**2+dist2)

    index=dist[np.argsort(a[dist])]
    maxx=np.zeros((17,1))
    for i in range(0,k):
        maxx[index[i]]+=1
    maxxx=-1
    for i in range(17):
        if(maxxx<maxx[i]):
            maxxx=index[i]

    return maxxx 
    

             
