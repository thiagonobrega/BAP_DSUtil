'''
Created on 17 de out de 2017

@author: Thiago
'''
import argparse
import pandas as pd
import numpy as np
from sampler import base
from sklearn.cluster import KMeans
import scipy as sp
from scipy.stats import bernoulli
import os
import time

def sample(data,p):
    brs = bernoulli.random_state
    elementos = []
    for i in range(2,len(data)):
        if brs.binomial(1,p) == 1:
            elementos.append(i)
    return elementos
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Arguments to extract samples',
    )
    
    parser.add_argument('--infile', action="store", dest="input_file",
                        help='Input file')
    
    parser.add_argument('--outdir', action="store", dest="out_dir",
                        help='Outputdir --outdir ./saida/ (the final / is importante)')
    
    parser.add_argument('--p_size', nargs='+', type=float, dest='list_sample_size',
                        help="recebe a lista p (de bernulli) para amostragem --p_size 0.1 0.2 )")
    
    parser.add_argument('--nsamples', action="store", dest="n_samples", type=int,
                        help='number of sample')

#     parser.add_argument('-dt', action="store",dest="data_type",
#                         default='ncvoters',
#                         help='data format [ncvoters,ncinmates,medicare]')
    
    
    args = parser.parse_args()
    
    
    input_file = args.input_file
    n_samples = int(args.n_samples)
    list_p = args.list_sample_size
    out_dir = args.out_dir
    
    
    if args.out_dir == None:
        out_dir = ""
    
    #import sys
    #sys.exit()
    
    #input_file="F:\\temp\\sampler\\restaurants\\tripadvisor_clean.csv"
    #input_file="F:\\temp\\sampler\\restaurants\\trip5k.csv"
    #out_dir = "apagar\\saida1\\"
    #n_samples = 5
    #list_p = [ 0.1, 0.4]
    now = time.ctime()
    print("Reading data [ %s ]..." % now)
    data = base.readData(input_file, sep=",")
    now = time.ctime()
    print("Data read [ %s ] " % now)
    
        
    import string
    sl = list(string.ascii_lowercase)
    
    for p in list_p:
        for s in range(n_samples):
            fin = os.path.split(input_file)[1]
            fout = fin.split(".")[0]+"-"+sl[s] + "_bernouli_selected_p" + str(p).replace(".","") + ".csv"
            z = sample(data,p)
            base.sample_writer(base.get_sample(data,z),out_dir,fout)
            print("Sample (%s) saved !" % fout)
    
    now = time.ctime()
    print("Done !")
    print(now)
    print("=="*20)
    print("=="*20)