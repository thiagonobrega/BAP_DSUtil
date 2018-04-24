'''
Created on 17 de out de 2017

Run:
    mkdir ksampler_output
    python3 kSampler2.py --infile F:\temp\sampler\restaurants\trip5k.csv --outdir ksampler_output/ --nsample 5 --sample_size 10 100 1000
    
    python3 kSampler2.py --infile restaurants/tripadvisor_clean.csv --outdir ksampler_output/ --nsample 5 --sample_size 100 1000 5000 10000
    python3 kSampler2.py --infile restaurants/yelp_clean.csv --outdir ksampler_output/ --nsample 5 --sample_size 100 1000 5000 10000
    
    python3 kSampler2.py --infile voters/ncvoter.csv --outdir ksampler_output/ --nsample 5 --sample_size 1000 10000 100000 1000000
    python3 kSampler2.py --infile voters/ohio_voters_striped_full.csv --outdir ksampler_output/ --nsample 5 --sample_size 1000 10000 100000 1000000
    

@author: Thiago
'''
import argparse
import pandas as pd
import numpy as np
from sampler import base
from sampler import ksampler
from sklearn.cluster import KMeans
import scipy as sp
import time
import os
from sampler.base import sample_writer
from sampler.base import get_sample

#def sample_writer(sample,fout):
#    import csv
#    sample.to_csv(fout,quoting=csv.QUOTE_NONNUMERIC,index=False)

#def get_sample(data,sample_index):
#    return data.iloc[sample_index]
#    return data.ix[sample_index]
    #data.loc[data['labels_gm'] == label]
    #pass
    
def get_clusters_index(data,labels):
    data['labels_gm'] = labels
    
    clusters = []
    #df.loc[df['column_name'].isin(some_values)]
    for label in set(labels):
        #data.loc[data['labels_gm'] == label]
        clusters.append(list(data.index[data['labels_gm'] == label]))
    del data['labels_gm']
    return clusters

def sample(clusters_list,n_sample):
    sample = []
    cluster_act = 0
    max_cluster = len(clusters)
    
    i = 0
    
    while (i < n_sample):
    #for i in range(n_sample):
        #volta para o zero quando chega ao tamanho maximo
        if cluster_act == max_cluster:
            cluster_act=0
        
        # pega um elemento aleatorio do cluester
        pos_c = np.random.randint(0,len(clusters[cluster_act]))
        try:
            #posso ter o problema de ficar eternamente aqui
            sample.index(clusters[cluster_act][pos_c])
            for pos_c in range(len(clusters[cluster_act])):
                #print(pos_c)
                sample.index(clusters[cluster_act][pos_c])
            #print("SAI : %s" % cluster_act)
            i-=1
        except ValueError:
            sample.append(clusters[cluster_act][pos_c])
        
        cluster_act+=1
        i+=1
    
    return sample
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Arguments to extract samples',
    )
    
    parser.add_argument('--infile', action="store", dest="input_file",
                        help='Input file')
    
    parser.add_argument('--outdir', action="store", dest="out_dir",
                        help='Outputdir --outdir ./saida/ (the final / is importante)')
    
    parser.add_argument('--sample_size', nargs='+', type=float, dest='list_sample_size',
                        help="Recebe a lista de sample size eg. -sample_size 100 1000 )")
    
    parser.add_argument('--nsamples', action="store", dest="n_samples", type=int,
                        help='number of sample')
    
    parser.add_argument('--use-percent', dest='percent', action='store_true')

#     parser.add_argument('-dt', action="store",dest="data_type",
#                         default='ncvoters',
#                         help='data format [ncvoters,ncinmates,medicare]')
    
    
    args = parser.parse_args()
    
    
    input_file = args.input_file
    n_samples = int(args.n_samples)
    list_sample_size = args.list_sample_size
    out_dir = args.out_dir
    if args.out_dir == None:
        out_dir = ""
    
    if (args.percent):
        p_flag = True
    else:
        p_flag = False
    
    #import sys
    #sys.exit()
    
    #input_file="F:\\temp\\sampler\\restaurants\\tripadvisor_clean.csv"
    #input_file="F:\\temp\\sampler\\restaurants\\trip5k.csv"
    #out_dir = "saida\\ks\\"
    #n_samples = 5
    #list_sample_size = [ 0.1 , 0.2 ]
    #list_sample_size = [ 100 , 200]
    now = time.ctime()
    print("Reading data [ %s ]..." % now)
    data, df = base.read(input_file, sep=",")
    from sampler.gmeans import GMeans
    gm = GMeans(random_state=1010)
    now = time.ctime()
    print("Data read [ %s ] " % now)
    
    now = time.ctime()
    print("Clustering [ %s ] ..." % now)
    gm.fit(df)
    now = time.ctime()
    print("Clusterized in [ %s ]" % now)
    
    
    #data['labels_gm'] = gm.labels_
    clusters = get_clusters_index(data,gm.labels_)
    
    import string
    sl = list(string.ascii_lowercase)
    
    for sample_size in list_sample_size:
        for s in range(n_samples):
            
            if (p_flag):
                actual_sample_size = int(len(data)* sample_size)
                file_id = "_ksampler_percent_"
                file_ss =  "p" +str(sample_size).replace(".","")
                print("\t Using sample size : [ %s ] => %s " % (sample_size,actual_sample_size))
            else:
                file_id = "_ksampler_selected_"
                actual_sample_size = int(sample_size)
                file_ss =  str(actual_sample_size) 
                
            fin = os.path.split(input_file)[1]
            fout = fin.split(".")[0]+"-"+sl[s] + file_id + file_ss + ".csv"
            z = sample(clusters,actual_sample_size)
            sample_writer(get_sample(data,z),out_dir,fout)
            print("Sample (%s) saved !" % fout)
    
    now = time.ctime()
    print("Done !")
    print(now)
    print("=="*20)
    print("=="*20)
    #z = sample(clusters,100)
    #a = get_sample(data,z)
    #import csv
    #a.to_csv("z.csv",quoting=csv.QUOTE_NONNUMERIC,index=False)