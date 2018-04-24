'''
Created on 17 de out de 2017

@author:  Thiago Nobrega
@mail: thiagonobrega@gmail.com
'''

import pandas as pd
import numpy as np

def get_sample(data,sample_index):
    return data.iloc[sample_index]

def sample_writer(sample,outdir,fout):
    """
        write the sample in a csv file
    """
    import csv
    import os
    os.makedirs(outdir,exist_ok=True)
    file_out = outdir+fout
    sample.to_csv(file_out,quoting=csv.QUOTE_NONNUMERIC,index=False)

def read(file,sep=",", encoding = "utf8"):
    """
        Read the data and return:
            1 - Panda dataframe (with row and attributes)
            2 - Panda dataframe with all attributes as in a unique attribute. Return all attributes values in one row
    """
    data = pd.read_csv(file,sep=sep,encoding = encoding).replace(np.nan, '', regex=True)
    #data['new'] = data[cols].values.sum(axis=1)
    #data['concat'] = pd.Series(data[columns].fillna('').values.tolist()).str.join('')
    #df = data.apply(lambda row: ','.join(map(str, row)), axis=1)
    return data, np.asarray(data.apply(lambda row: ' '.join(map(str, row)), axis=1))

def readData(file,sep=",", encoding = "utf8"):
    """
        Read the data and return as a panda dataframe
    """
    data = pd.read_csv(file,sep=sep,encoding = encoding).replace(np.nan, '', regex=True)
    return data


