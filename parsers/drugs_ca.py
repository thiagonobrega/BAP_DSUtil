# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 10:07:57 2017

1.942.165 registros
18 atributos

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

#outdir =os.path.sep+"home/thiago/dados"+os.path.sep+"drugs"+os.path.sep
outdir ="F:"+os.path.sep+"z_dados"+os.path.sep+"drugs"+os.path.sep
indir=outdir+"cvponline_extract_20170331"+os.path.sep

##
## Acessory data read
##

file = "gender_lx.txt"
cols = ['GENDER_LX_ID','GENDER_CODE','GENDER_EN','GENDER_FR']
print("Read data : %s" % file)
gender_data = readFile(indir,file,cols)
del file ,cols


file = "outcome_lx.txt"
cols = ['OUTCOME_LX_ID','OUTCOME_CODE','OUTCOME_EN','OUTCOME_FR']
print("Read data : %s" % file)
outcome_data = readFile(indir,file,cols)
del file ,cols

file = "report_type_lx.txt"
cols = ['REPORT_TYPE_LX_ID','REPORT_TYPE_CODE','REPORT_TYPE_EN','REPORT_TYPE_FR']
print("Read data : %s" % file)
report_type_data = readFile(indir,file,cols)
del file ,cols

file = "source_lx.txt"
cols = ['SOURCE_LX_ID','SOURCE_CODE','SOURCE_EN','SOURCE_FR']
print("Read data : %s" % file)
source_data = readFile(indir,file,cols)
del file ,cols

file = "seriousness_lx.txt"
cols = ['SERIOUSNESS_LX_ID','SERIOUSNESS_CODE','SERIOUSNESS_EN','SERIOUSNESS_FR']
print("Read data : %s" % file)
seriosness_data = readFile(indir,file,cols)
del file ,cols

##
## Linkding data
##

# Purpose: This table provides the information about the linked/duplicate reports presentation text associated with the code. 
file = "report_links.txt"
cols = ['REPORT_LINK_ID','REPORT_ID','RECORD_TYPE_ENG','RECORD_TYPE_FR','REPORT_LINK_NO']
print("Read data : %s" % file)
report_links_data = readFile(indir,file,cols)
del file ,cols


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

# talves usar em outra combincao
file = "drug_products.txt"
cols = ['DRUG_PRODUCT_ID','DRUGNAME']
print("Read data : %s" % file)
drug_products_data = readFile(indir,file,cols)
del file ,cols


# Purpose: This table provides the information about indications associated with specific reports. 
#nao e muilto util
file = "report_drug_indication.txt"
cols = ['REPORT_DRUG_ID','REPORT_ID','DRUG_PRODUCT_ID','DRUGNAME','INDICATION_NAME_ENG',
        'INDICATION_NAME_FR']
print("Read data : %s" % file)
report_drug_indication_data = readFile(indir,file,cols)
del file ,cols

###
### Data
###

# Report_Drug
# Purpose: This table provides the information about drugs associated with specific reports. 
file = "report_drug.txt"
cols = ['REPORT_DRUG_ID','REPORT_ID','DRUG_PRODUCT_ID','DRUGNAME','DRUGINVOLV_ENG','DRUGINVOLV_FR',
        'ROUTEADMIN_ENG', 'ROUTEADMIN_FR' , 'UNIT_DOSE_QTY', 'DOSE_UNIT_ENG' , 'DOSE_UNIT_FR',
        'FREQUENCY', 'FREQ_TIME' , 'FREQUENCY_TIME_ENG' , 'FREQUENCY_TIME_FR' , 'FREQ_TIME_UNIT_ENG' , 'FREQ_TIME_UNIT_FR',
        'THERAPY_DURATION','THERAPY_DURATION_UNIT_ENG','THERAPY_DURATION_UNIT_FR','DOSAGEFORM_ENG','DOSAGEFORM_FR']
print("Read data : %s" % file)
report_drug_data = readFile(indir,file,cols)
del file ,cols

#reports
#  Purpose: This table provides the information about reports and patients. 
file = "reports.txt"
cols = ['REPORT_ID','REPORT_NO','VERSION_NO','DATRECEIVED','DATINTRECEIVED','MAH_NO',
        'REPORT_TYPE_CODE','REPORT_TYPE_ENG','REPORT_TYPE_FR','GENDER_CODE','GENDER_ENG','GENDER_FR',
        'AGE','AGE_Y','AGE_UNIT_ENG','AGE_UNIT_FR','OUTCOME_CODE','OUTCOME_ENG','OUTCOME_FR',
        'WEIGHT','WEIGHT_UNIT_ENG','WEIGHT_UNIT_FR','HEIGHT','HEIGHT_UNIT_ENG','HEIGHT_UNIT_FR',
        'SERIOUSNESS_CODE','SERIOUSNESS_ENG','SERIOUSNESS_FR','DEATH','DISABILITY','CONGENITAL_ANOMALY',
        'LIFE_THREATENING','HOSP_REQUIRED','OTHER_MEDICALLY_IMP_COND','REPORTER_TYPE_ENG','REPORTER_TYPE_FR',
        'SOURCE_CODE','SOURCE_ENG','SOURCE_FR']
print("Read data : %s" % file)
reports_data = readFile(indir,file,cols)
del file ,cols



## reaction
# Purpose: This table provides the information about the reaction terms associated with report. 
# remove MEDDRA_VERSION
file = "reactions.txt"
cols = ['REACTION_ID','REPORT_ID','DURATION','DURATION_UNIT_ENG','DURATION_UNIT_FR',
        'PT_NAME_ENG','PT_NAME_FR','SOC_NAME_ENG','SOC_NAME_FR','MEDDRA_VERSION']
print("Read data : %s" % file)
reactions_data = readFile(indir,file,cols)
del file ,cols



## reactio + report

import pandas as pd
#data = reports_data.join(report_drug_data,how='left',on="REPORT_ID",rsuffix="FR_")
#data = data.join(drug_products_data,how='inner',rsuffix="FR_")
#data = data.join(outcome_data,how='left',rsuffix="FR_")
##z = z.join(outcome_data,how='inner',rsuffix="FR_")
##data = data.join(seriosness_data,how='left',rsuffix="FR_")

data = reports_data.merge(report_drug_data,how='inner',on="REPORT_ID", suffixes=('', 'FR_'))
data = data.join(drug_products_data,on='DRUG_PRODUCT_ID',how='inner',rsuffix="FR_")
data = data.join(outcome_data,on='OUTCOME_CODE',how='left',rsuffix="FR_")

#delete_columns = []
delete_columns = [ 'DRUG_PRODUCT_ID','SERIOUSNESS_CODE', 
                  'THERAPY_DURATION_UNIT_ENG','OUTCOME_CODE','GENDER_CODE',
                  'AGE_UNIT_ENG', 'VERSION_NO' , 'AGE', 'FREQUENCY',
                  'FREQ_TIME_UNIT_ENG','SERIOUSNESS_LX_ID', 'REPORT_TYPE_CODE',
                  'REPORT_DRUG_ID', 'REPORT_NO', 'OTHER_MEDICALLY_IMP_COND',
                  'THERAPY_DURATION','LIFE_THREATENING', 'FREQ_TIME',
                  'OUTCOME_LX_ID','SOURCE_CODE','SERIOUSNESS_ENG','MAH_NO',
                  'FREQUENCY_TIME_ENG','REPORT_ID','CONGENITAL_ANOMALY',
                  'DEATH','HOSP_REQUIRED','DISABILITY','SERIOUSNESS_EN',
                  'OUTCOME_EN' ] + ['UNIT_DOSE_QTY', 'DOSE_UNIT_ENG' , 'DATRECEIVED'
                  'REPORTER_TYPE_ENG', 'SOURCE_ENG', 'REPORT_TYPE_ENG']


for d in list(data.columns):
    if "FR_" in d:
        delete_columns.append(d)
            
data = data[list(set(data.columns)-set(delete_columns))]

del delete_columns, drug_product_ingredients_data, drug_products_data, 
del gender_data, outcome_data, reactions_data, report_drug_data, 
del report_drug_indication_data, report_links_data, report_type_data, 
del reports_data, seriosness_data , source_data

##STANDARD FORMAT
#upercase
print("Converting to Standart Format...")
print("::: Upper")
data = data.apply(lambda x: x.astype(str).str.upper())
print("::: AGE ")
data['AGE_Y'] = pd.to_numeric(data['AGE_Y'], downcast='signed')
data['AGE_Y'] = data['AGE_Y'].fillna(-1).astype(int).astype(str).str.replace("-1","")
#data['OUTCOME_EN'] = data['OUTCOME_EN'].astype(str).str.replace("NAN","")
data['GENDER_ENG'] = data['GENDER_ENG'].str.replace("FEMALE","F")
data['GENDER_ENG'] = data['GENDER_ENG'].str.replace("MALE","M")
data['GENDER_ENG'] = data['GENDER_ENG'].str.replace("UNKNOWN","UNK")
#data['GENDER_ENG'].unique()
#HEIGHT,WEIGHT

data['DATINTRECEIVED'] = data['DATINTRECEIVED'].apply(fix_date)

data = data.apply(lambda x: x.astype(str).str.upper())

#datetime.strptime(str(data['DATINTRECEIVED'][10]),'%d-%b-%y')
#data.columns

print("Saving data ...")
print("Dumas")
base.writeData(data.apply(lambda x: x.astype(str).str.replace(';','')),outdir+'dumas_drugs_ca.csv',index=True,dumasConvert=False)
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