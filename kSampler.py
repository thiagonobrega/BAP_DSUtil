'''
Created on 17 de out de 2017

@author: Thiago
'''
import argparse
import pandas as pd
import numpy as np
from sampler import base
from sampler import ksampler
from sklearn.cluster import KMeans
import scipy as sp


def extractClusterElements(df,km,cluster):
    index = np.argwhere(km.labels_!=cluster)
    #return index
    return np.delete(df,index)


def nparray2indexlix(array):
    '''
        Converte o array com os index para uma lista de index
    '''
    r = []
    for e in array:
        r.append(e[0])
    return r
    
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Arguments to extract samples',
    )
    
    parser.add_argument('input_file', action="store", help='Input file')

#     parser.add_argument('-dt', action="store",dest="data_type",
#                         default='ncvoters',
#                         help='data format [ncvoters,ncinmates,medicare]')
    
    
    args = parser.parse_args()
    input_file = args.input_file
    knf2 = args.fase2
    input_file="F:\\temp\\sampler\\restaurants\\tripadvisor_clean.csv"
    input_file="F:\\temp\\sampler\\restaurants\\trip5k.csv"
    knf2 = 2
    
    data, df = base.read(input_file, sep=",")
    columns_names = list(data.columns)
    #X = ksampler.vectorize_classic(data,columns_names)
    X = ksampler.vectorize(df)
    import math
    #https://www.quora.com/How-can-we-choose-a-good-K-for-K-means-clustering
    #k = 30
    #k = int(math.sqrt(len(data)/2))
    #km = ksampler.clusterFi(data,X,k)
    #km = ksampler.clusterFi(df,X,k)
    k = 4 
    km = ksampler.clusterFiX(df,X,k)
    
    cluster_elements = []
    
    for cluster in set(km.labels_):
        #extrai os clusters
        temp_df = extractClusterElements(df,km,cluster)
        xt = ksampler.vectorize(temp_df)
        temp_km = ksampler.clusterFiX(temp_df,xt,knf2)
        
        #v = temp_km.cluster_centers_[0] - temp_km.cluster_centers_[0]
        #x_prime = scale(xt.dot(v) / (v.dot(v)))
        #sp.stats.anderson(x_prime)
        
        #marca os labels
        for ilabel in set(temp_km.labels_):
            index = np.argwhere(temp_km.labels_==ilabel)
            cluster_elements.append(index)
    
    # extract cluster elements    
    #z = data.loc[nparray2indexlix(cluster_elements[1])]

    #for i in range(len(cluster_elements)):
    #    print("Cluster %s : %s" % (i,len(cluster_elements[i])) )
    #    s += len(cluster_elements[i])
    
    index = np.argwhere(km.cluster_centers_[29]==0)
    sp.stats.anderson(np.delete(km.cluster_centers_[29],index))
    z[0]*(1+4/len(z[0])+25/(len(z[0])*len(z[0]))
    
    z[0]*(1+4/329+25/(329*329)