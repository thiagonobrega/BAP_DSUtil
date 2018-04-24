# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 10:50:11 2018

21 atributos
@author: Thiago
"""

import pandas as pd
import numpy as np
from parsers import base
import os
from datetime import datetime


def readFile(in_dir,file):
    return base.readData(in_dir+file, sep="$")

def fix_date(din):
    newdate = ''
    d=str(din)
    if len(d)==4:
        dt = datetime.strptime(str(d),'%Y')
        newdate = str(dt.year) 
    if len(d)==6:
        dt = datetime.strptime(str(d),'%Y%m')
        newdate = str(dt.month) + "/" + str(dt.year) 
    if len(d)==8:
        dt = datetime.strptime(str(d),'%Y%m%d')
        newdate = str(dt.day) + "/" + str(dt.month) + "/" + str(dt.year) 
    return newdate

outdir =os.path.sep+"home/thiago/dados"+os.path.sep+"drugs"+os.path.sep
#outdir ="F:"+os.path.sep+"z_dados"+os.path.sep+"drugs"+os.path.sep
indir=outdir+"fda"+os.path.sep

##
## Acessory data read
##
print(":::: Reading Original files")


file = "DRUG17Q2.txt"
print("> File %s" %file)
data = readFile(indir,file)

print(":::: Assembling")
data['drugname'] = data['drugname'].astype(str)


delete_columns = ["primaryid","dur",'role_cod','lot_num', 'exp_dt','nda_num','dechal','rechal','val_vbm','drug_seq','caseid']

fix_dfeq = [("1X","Once or one time"),("BID","Twice a day"),("BIW","Twice a week"),("HS","At bedtime"),("PRN","As needed"),("Q12H","Every 12 hours"),("Q2H","Every 2 hours"),("Q3H","Every 3 hours"),("Q3W","Every 3 weeks"),("Q4H","Every 4 hours"),("Q5H","Every 5 hours"),("Q6H","Every 6 hours"),("Q8H","Every 8 hours"),("QD","Daily"),("QH","Every hour"),("QID","4 times a day"),("QM","Monthly"),("QOD","Every other day"),("QOW","Every other week"),("QW","Every week"),("TID","3 times a day"),("TIW","3 times a week"),("UNK","Unknown")]
for i in fix_dfeq:
    print("::: Fixing %s"%i[0])
    data['dose_freq'] = data['dose_freq'].str.replace(i[0],i[1].upper())

for d in list(data.columns):
    if "FR_" in d:
        delete_columns.append(d)

data = data[list(set(data.columns)-set(delete_columns))]

for i in data.columns:    
    try:
        data = data[data[i]!='']
    except TypeError:
        pass
    

data = data.apply(lambda x: x.astype(str).str.upper())

print(":: Saving data ...")
print("Dumas")
#base.writeData(data_fda.apply(lambda x: x.astype(str).str.replace(';','')),outdir+'dumas_drugs_fda.csv',index=True,dumasConvert=False)
print("BAP")
base.writeData(data,outdir+'drugsfda.csv')

