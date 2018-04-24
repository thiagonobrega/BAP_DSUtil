# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 11:32:36 2017

@author: Thiago
"""
import argparse
import pandas as pd
import numpy as np
from sampler import base
import scipy as sp
import os
import time

def sample(data,sample_size):
    z = np.random.choice(int(len(data)) ,int(sample_size),replace=False)
    return np.delete(z,np.where(z==0))
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Arguments to extract samples',
    )
    
    parser.add_argument('--infile', action="store", dest="input_file",
                        help='Input file')
    
    parser.add_argument('--outdir', action="store", dest="out_dir",
                        help='Outputdir --outdir ./saida/ (the final / is importante)')
    
    parser.add_argument('--sample_size', nargs='+', type=float, dest='list_sample_size',
                        help="recebe a lista p (de bernulli) para amostragem --p_size 0.1 0.2 )")
    
    parser.add_argument('--nsamples', action="store", dest="n_samples", type=int,
                        help='number of sample')
    
    parser.add_argument('--use-percent', dest='percent', action='store_true')
    
    
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
    #out_dir = ""
    #n_samples = 5
    #list_sample_size = [ 0.1, 0.4]
    #list_sample_size = [ 100, 500]
    #p_flag = False
    now = time.ctime()
    print("Reading data [ %s ]..." % now)
    data = base.readData(input_file, sep=",")
    now = time.ctime()
    print("Data read [ %s ] " % now)
    
        
    import string
    sl = list(string.ascii_lowercase)
    
    for sample_size in list_sample_size:
        for s in range(n_samples):
            
            if (p_flag):
                actual_sample_size = int(len(data)* sample_size)
                file_id = "_random_percent_"
                file_ss =  "p" +str(sample_size).replace(".","")
                print("\t Using sample size : [ %s ] => %s " % (sample_size,actual_sample_size))
            else:
                file_id = "_random_selected_"
                actual_sample_size = sample_size
                file_ss =  str(actual_sample_size) 

            fin = os.path.split(input_file)[1]
            fout = fin.split(".")[0]+"-"+sl[s] + file_id + file_ss + ".csv"
            z = sample(data,actual_sample_size)
            base.sample_writer(base.get_sample(data,z),out_dir,fout)
            print("Sample (%s) saved !" % fout)
    
    now = time.ctime()
    print("Done !")
    print(now)
    print("=="*20)
    print("=="*20)
