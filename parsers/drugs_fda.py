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

#outdir =os.path.sep+"home/thiago/dados"+os.path.sep+"drugs"+os.path.sep
outdir ="F:"+os.path.sep+"z_dados"+os.path.sep+"drugs"+os.path.sep
indir=outdir+"fda"+os.path.sep

##
## Acessory data read
##
print(":::: Reading Original files")

file = "DEMO17Q2.txt"
print("> File %s" %file)
data_demo = readFile(indir,file)

file = "DRUG17Q2.txt"
print("> File %s" %file)
data_drug = readFile(indir,file)

file = "REAC17Q2.txt"
print("> File %s" %file)
data_react = readFile(indir,file)

#nao utilizado
file = "OUTC17Q2.txt"
print("> File %s" %file)
data_outcome = readFile(indir,file)

#nao utilizado
file = "RPSR17Q2.txt"
print("> File %s" %file)
data_reports = readFile(indir,file)

#nao utilizado
file = "INDI17Q2.txt"
print("> File %s" %file)
data_ind = readFile(indir,file)

file = "THER17Q2.txt"
print("> File %s" %file)
data_therapy= readFile(indir,file)
del file

print(":::: Assembling")
data_drug['drugname'] = data_drug['drugname'].astype(str)

data = data_demo.merge(data_drug,how='inner',on="primaryid", suffixes=('', 'FR_'))
data = data.merge(data_react,how='inner',on="primaryid", suffixes=('', 'FR_'))
#data = data.join(data_therapy,how='left',on="caseid",rsuffix="FR_")


delete_columns = ["primaryid","caseid","prodai","dur","dur_cod","end_dt",
                  "drug_rec_act","caseversion","i_f_code","mfr_dt","init_fda_dt",
                  "fda_dt",'rept_cod','mfr_num','rept_dt','to_mfr',
                  'reporter_country','drug_seq','val_vbm','cum_dose_chr',
                  'cum_dose_unit','dechal','rechal','exp_dt','nda_num','dose_amt',
                  'dose_freq','dsg_drug_seq','end_dt','lit_ref'] + 

for d in list(data.columns):
    if "FR_" in d:
        delete_columns.append(d)

data = data[list(set(data.columns)-set(delete_columns))]

#del d,delete_columns,data_ind,data_outcomet

###
#data['occp_cod'].unique()
data['occp_cod'] = data['occp_cod'].str.replace("MD","Physician".upper())
data['occp_cod'] = data['occp_cod'].str.replace("PH","Pharmacist".upper())
data['occp_cod'] = data['occp_cod'].str.replace("OT","Other health-professional".upper())
data['occp_cod'] = data['occp_cod'].str.replace("LW","Lawyer".upper())
data['occp_cod'] = data['occp_cod'].str.replace("CN","Consumer".upper())

#event_dt

#data['event_dt'].astype(str) = pd.to_numeric(data['event_dt'], downcast='signed').asty
#datetime.strptime(str(data['event_dt'][1000]), '%Y%m%d')

cut = lambda x: x[:x.find('.')]
data['event_dt'] = data['event_dt'].astype(str).apply(cut)

#datetime.strptime(str(data['event_dt'][1000]), '%Y%m%d')
#lambda d: datetime.strptime(str(d,'%Y') if len(d)==4 else datetime.strptime(str(d,'%Y%m') if len(d)==6 else datetime.strptime(str(d,'%Y%m%d') if len(d)==8
#fix_time = lambda d: datetime.strptime(str(d,'%Y') if len(d)==4 else datetime.strptime(str(d,'%Y%m') if len(d)==6 else datetime.strptime(str(d,'%Y%m%d') if len(d)==8


#df['name'].apply(capitalizer)
#fix_date(data['event_dt'][1000])
#x = data['event_dt'].astype(str).str.replace("nan","")
#data['OUTCOME_EN'] = data['OUTCOME_EN'].astype(str).str.replace("NAN","")
#datetime.strptime(str(data['event_dt'][1000]), '%Y%m%d')
#data['drugname']

data['event_dt'] = data['event_dt'].apply(fix_date)
data = data.apply(lambda x: x.astype(str).str.upper())

print(":: Saving data ...")
print("Dumas")
base.writeData(data.apply(lambda x: x.astype(str).str.replace(';','')),outdir+'dumas_drugs_fda.csv',index=True,dumasConvert=False)
print("BAP")
base.writeData(data,outdir+'drugs_fda.csv')

