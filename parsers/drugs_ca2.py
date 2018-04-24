# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 10:07:57 2017

499139 registros
13 atributos

@author: Thiago
"""
import pandas as pd
import numpy as np
from parsers import base
import os
from datetime import datetime


def fix_date(din):
    d = str(din)
    dt = datetime.strptime(str(d),'%d-%b-%y')
    newdate = str(dt.day) + "/" + str(dt.month) + "/" + str(dt.year)
    return newdate


def readFile(in_dir,file,columns_name):
    data = base.readData(in_dir+file, sep="$" , headers = None)
    data.columns = columns_name
    
    delete_columns = []
    for d in cols:
        if "_FR" in d:
            delete_columns.append(d)
            
    return data[list(set(columns_name)-set(delete_columns))]

outdir =os.path.sep+"home/thiago/dados"+os.path.sep+"drugs"+os.path.sep
#outdir ="F:"+os.path.sep+"z_dados"+os.path.sep+"drugs"+os.path.sep
indir=outdir+"cvponline_extract_20170331"+os.path.sep

##
## Acessory data read
##



##
## Acessorie data
##

#  Purpose: This table provides the information about the active ingredients associated with all drugs. 
# talves usar em outra combincao
file = "drug_product_ingredients.txt"
cols = ['DRUG_PRODUCT_INGREDIENT_ID','DRUG_PRODUCT_ID','DRUGNAME','ACTIVE_INGREDIENT_ID','ACTIVE_INGREDIENT_NAME']
print("Read data : %s" % file)
drug_product_ingredients_data = readFile(indir,file,cols)
del file ,cols

# Report_Drug
# Purpose: This table provides the information about drugs associated with specific reports. 
file = "report_drug.txt"
cols = ['REPORT_DRUG_ID','REPORT_ID','DRUG_PRODUCT_ID','DRUGNAME','DRUGINVOLV_ENG','DRUGINVOLV_FR',
        'ROUTEADMIN_ENG', 'ROUTEADMIN_FR' , 'UNIT_DOSE_QTY', 'DOSE_UNIT_ENG' , 'DOSE_UNIT_FR',
        'FREQUENCY', 'FREQ_TIME' , 'FREQUENCY_TIME_ENG' , 'FREQUENCY_TIME_FR' , 'FREQ_TIME_UNIT_ENG' , 'FREQ_TIME_UNIT_FR',
        'THERAPY_DURATION','THERAPY_DURATION_UNIT_ENG','THERAPY_DURATION_UNIT_FR','DOSAGEFORM_ENG','DOSAGEFORM_FR']
print("Read data : %s" % file)
report_drug_data = readFile(indir,file,cols)

for i in report_drug_data.columns:    
    try:
        report_drug_data = report_drug_data[report_drug_data[i]!='']
    except TypeError:
        pass
            
    
del file ,cols,


## reactio + report

import pandas as pd
data = report_drug_data.merge(drug_product_ingredients_data,how='inner',on="DRUG_PRODUCT_ID", suffixes=('', 'FR_'))

delete_columns = ['REPORT_DRUG_ID','DRUG_PRODUCT_INGREDIENT_ID','DRUG_PRODUCT_ID','ACTIVE_INGREDIENT_ID','REPORT_ID']

for d in list(data.columns):
    if "FR_" in d:
        delete_columns.append(d)
            
data = data[list(set(data.columns)-set(delete_columns))]




#for i in data.columns:    
#    zz.replace({i: {'': np.nan}}).dropna(subset=[i])
#    x = data['].value_counts()


##STANDARD FORMAT
#upercase
print("Converting to Standart Format...")
print("::: Upper")
data = data.apply(lambda x: x.astype(str).str.upper())

#datetime.strptime(str(data['DATINTRECEIVED'][10]),'%d-%b-%y')
#data.columns

print("Saving data ...")
print("Dumas")
#base.writeData(data.apply(lambda x: x.astype(str).str.replace(';','')),outdir+'dumas_drugs_ca.csv',index=True,dumasConvert=False)
print("BAP")
base.writeData(data,outdir+'drugs_ca.csv')

###
#delete_columns = []
#for d in list(reactions_data.columns):
#    if "_CODE" in d:
#        delete_columns.append(d)
            
#z = reactions_data[list(set(reactions_data.columns)-set(delete_columns))]


#for d in list(z.columns):
#    x = z[d].unique()
#    if len(x) < 10:
#        print(" %s : %s " % (d,x))