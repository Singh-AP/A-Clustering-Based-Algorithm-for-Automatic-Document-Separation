# A-Clustering-Based-Algorithm-for-Automatic-Document-Separation
[![Generic badge](https://img.shields.io/badge/image-processing-green)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Python-3.7-blue)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/built-with_love-red)](https://shields.io/)

Semester Project, Digital Image Processing, Monsoon 2019.<br>
Contributors: [Amrit Preet Singh](https://github.com/TheIndianCoder), [Mehtaab Singh Hazra] (https://github.com/mehtabhazra1998)
## BRIEF Description

A model to estimate inter page similarity in order to separate pages into ordered collections of document images . The features obtained from the query image is used to assign the cluter number to the image.

## APPLICATIONS

- Managing Document image collections
- Search results for queries on document image collections
- Detection for indexing and other purposes 

## Installation

To install the required libraries (tested on Ubuntu 17.11) run:

          python3 -m venv venv
          source venv/bin/activate
          pip install -r requirements.txt

## Dataset:

          The model has been tested on the RVL-CDIP dataset, which is available at: http://www.cs.cmu.edu/~aharley/rvl-cdip/

## RUNNING THE CODE

-Inference on Image:

           ./run_pythonscript.sh <query image path>
   
 ## Files
 
 -text_similarity.py:
 
           Cosine similarity of the bag of words in the image's OCR output
  
  -LayoutFeaturesFuntion.py:
  
            Retreives layout features like:
                  - Average Word length
                  - Average line spacing
                  - Average Character height
                  - Average Word spacing
     
   - knn_cluster.py:
   
            Returns the majority vote of k nearest neighbors of a given image
               
   - train_labels_and_url.txt:
   
            File conataining the path of images and the respective labels.
            
[![Generic badge](https://img.shields.io/badge/Contributions-welcome-green)](https://shields.io/)

