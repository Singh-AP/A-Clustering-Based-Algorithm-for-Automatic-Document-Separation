from text_similarity_function import text_similarity



def cluster_no(img_test,test_folder,k):
    i=0
    folder='b/'
    #lss=[]
    dist=[]
    features1=[] # features of query image to be done
    for foldername in  os.listdir(folder):
        for filename in os.listdir(str(folder+'/'+foldername+'/')):
            img=Image.open(os.path.join(folder,foldername,filename))
            labels.append(img.label())      #extract labels from function for current image
            dist1=1-text_similarity(img,img_test)
            dist2=np.sum((features1-features(img))**2) #spacing function to be used here 
            dist.append(dist1**2+dist2)

    index=np.argsort(dist)
    maxx=np.zeros((17,1))
    for i in range(0,k):
        maxx[index[i]]+=1
    maxxx=-1
    for i in range(17):
        if(maxxx<maxx[i]):
            maxxx=index[i]

    return maxxx
    

             
