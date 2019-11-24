from PIL import Image
import pytesseract
import argparse
import os
import string 
import re 
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords 
import nltk
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# img1=Image.open('dataset/novel.png')
# img2=Image.open('dataset/novel2.png')


##############################################################################################

def text_similarity(img1,img2):
    text=pytesseract.image_to_string(img1)
#text=text.read().lower()
    text2=pytesseract.image_to_string(img2)
    ls=[]
    ls2=[]
    for sentence in text.split():
        for word in re.findall(r'\b[a-z A-Z]{1,26}\b',sentence):
            ls.append(word.lower())
    
    for sentence in text2.split():
        for word in re.findall(r'\b[a-z A-Z]{1,26}\b',sentence):
            ls2.append(word.lower())


    ls_new=[]
    ls_new2=[]
    #stop_words = set(stopwords.words('english'))
    
    ls_rep=ls
    ls_rep2=ls2

    for word in ls:
        flag=1
        for wrd in ls_new:
            if(word==wrd):
                flag=0
        if(flag==1):
            ls_new.append(word)
    ls_new.sort()
    
    
    for word in ls2:
        flag=1
        for wrd in ls_new2:
            if(word==wrd):
                flag=0
        if(flag==1):
            ls_new2.append(word)
    ls_new2.sort()

        
    
    
    #print(ls_new)
    ls=[]
    for w in ls_new:
        if(w not in stop_words):
            ls.append(w)

    ls2=[]
    for w in ls_new2:
        if(w not in stop_words):
            ls2.append(w)

    #print(ls)

    ls_rep.sort()
    ls_rep2.sort()
    word2count = {}
    word2count2 = {}
    for word in ls_rep:
        if word not in word2count.keys():
            word2count[word] = 1
            word2count2[word]=0
        else:
            word2count[word] += 1

    #print(word2count)
    for word in ls_rep2:
        if word not in word2count.keys():
            pass
        else:
            word2count2[word]+=1
    #print(word2count2)
    vec1=[]
    vec2=[]
    #print(ls_rep)
    for key,value in word2count.items():
        vec1.append(value)
    for key,value in word2count2.items():
        vec2.append(value)


    vec1=np.asarray(vec1)
    vec2=np.asarray(vec2)

    #print(vec1)
    #print(vec2)
    return cosine_similarity([vec1],[vec2])


# aa=text_similarity(img1,img2)
# print(aa)
