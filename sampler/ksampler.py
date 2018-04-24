# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 15:08:28 2017

@author: Thiago
"""

from sklearn.feature_extraction.text import HashingVectorizer
from scipy.sparse import hstack
from sklearn.cluster import KMeans

##
## old
## 
def vectorize_calssic(data,columns):
    list_X=[]
    #Vectorize
    for X in columns:
        print(X)
        x_vectorizer = HashingVectorizer()
        Xn = x_vectorizer.fit_transform([str(doc) for doc in data[X]])
        list_X.append(Xn)    
    return hstack(list_X)

def clusterFi_classic(data,vectors,cluster_size):
    km = KMeans(n_clusters=cluster_size)
    zip(data, km.fit_predict(vectors))
    return km

def vectorize(df):
    x_vectorizer = HashingVectorizer()
    X = x_vectorizer.fit_transform([str(doc) for doc in df ])
    return X

def clusterFiX(df,vectors,cluster_size):
    km = KMeans(n_clusters=cluster_size)
    zip(df, km.fit_predict(vectors))
    return km

