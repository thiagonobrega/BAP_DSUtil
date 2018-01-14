# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 19:11:52 2018

gc log.txt | select -first 10

@author: Thiago
"""
import pandas as pd
import numpy as np
from parsers import base
import os
from datetime import datetime


def readFile(in_dir,file):
    return base.readData(in_dir+file, sep="|", encoding="iso-8859-1")

indir ="F:"+os.path.sep+"z_dados"+os.path.sep+"PublicEmployees"+os.path.sep
ds = "tce" + os.path.sep
file = "TCE-PB-SAGRES-Folha_Pessoal_Esfera_Estadual-062017.txt"

data = readFile(indir+ds,file)

#filter mes 06/2016
data = data.loc[data['dt_mesano'] == 62016]
data = data.apply(lambda x: x.astype(str).str.upper())

print("Dumas")
base.writeData(data.apply(lambda x: x.astype(str).str.replace(';','')),indir+'dumas_tce.csv',index=True,dumasConvert=False)
print("BAP")
base.writeData(data,indir+'tce.csv')

