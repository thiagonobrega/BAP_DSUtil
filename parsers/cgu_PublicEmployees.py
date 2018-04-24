# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 09:59:34 2018

699023 registros 43 atributos

@author: Thiago
"""

import pandas as pd
import numpy as np
from parsers import base
import os
from datetime import datetime


def readFile(in_dir,file):
    return base.readData(in_dir+file, sep="\t", encoding="iso-8859-1")

indir ="F:"+os.path.sep+"z_dados"+os.path.sep+"PublicEmployees"+os.path.sep
indir =os.path.sep+"home/thiago/dados"+os.path.sep+"PublicEmployees"+os.path.sep

ds = "cgu" + os.path.sep
file = "20171017_expulsoes.csv"

data = readFile(indir+ds,file)

print("Dumas")
base.writeData(data.apply(lambda x: x.astype(str).str.replace(';','')),indir+'dumas_cgu.csv',index=True,dumasConvert=False)
print("BAP")
base.writeData(data,indir+'cgu.csv')


#file = "20160630_CadastroMilitares.csv"
#militar = readFile(indir+ds,file)