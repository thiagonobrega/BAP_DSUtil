# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 10:09:30 2017

@author: Thiago
"""

import pandas as pd
import numpy as np
import csv

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

def readData(file,sep=",", encoding = "utf8", headers = 'infer'):
    """
        Read the data and return as a panda dataframe
    """
    data = pd.read_csv(file,sep=sep,encoding = encoding , header = headers).replace(np.nan, '', regex=True)
    return data


def writeData(data,file,encoding = "utf8",index=False):
    """
        save the data (pandas) to a file
    """
    if index:
        data.index.names = ['ID']
        data.to_csv(file,index=index,encoding=encoding ,quoting=csv.QUOTE_NONNUMERIC)
    else:
        data.to_csv(file,index=index,encoding=encoding ,quoting=csv.QUOTE_ALL)