import csv
import pandas as pd
import numpy as np
import scipy as sp
from datetime import datetime

from parsers import base
import os

in_dir ="F:"+os.path.sep+"z_dados"+os.path.sep+"Restaurants"+os.path.sep
file = "yelp_data.csv"
data = base.readData(in_dir+file, sep=",")
base.writeData(data.apply(lambda x: x.astype(str).str.replace(';','')),in_dir+'dumas_yelp.csv',index=True,dumasConvert=False)

import sys
sys.exit()


states = ['AK', 'AL', 'AR', 'AS', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'GU', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MP', 'MS', 'MT', 'NA', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'PR', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VI', 'VT', 'WA', 'WI', 'WV', 'WY']

tc = ['Restaurants','Pizza','Mexican','Food','Diners','Bakeries','Sandwiches','Breakfast','Coffee','Pizza','Ice Cream','Drinks','Yogurt']
cat =[]
for e in tc:
    cat.append(e.upper())


file="F:\\temp\\sac\\scratch\\yelp_academic_dataset_business.csv"
data = pd.read_csv(file, sep=",",dtype={'is_open': object}).replace(np.nan, '', regex=True)

drop_list = []

for i in range(0,len(data)): 
    if data['state'][i] not in states:
        drop_list.append(i)
    else:
        eflag = False
        for e in cat:
            if e in data['categories'][i].upper():
                eflag = True
                break
            
        if not eflag:
            drop_list.append(i)
            

us = data.drop(data.index[drop_list])

for c in us.columns:
    us[c] = us[c].astype(str)

for i in us.index:
    for j,header in enumerate(us.columns):
        val = us[header][i].upper()
    
        if header == 'hours':
            val = val.replace('[', '').replace(']', '').replace('\'', '')
        elif header == 'is_open':
            if val == 1:
                val = 'TRUE'
            else:
                val = 'FALSE'
        elif header == 'attributes':
            val = val.replace('[', '').replace(']', '').replace('\'', '')
        elif header == 'categories':
            val = val.replace('[', '').replace(']', '').replace('\'', '')
        #verificar o rating
            
        us.set_value(i,header,val)

us.to_csv('F:\\temp\\sac\\yelp_data.csv',index=False,encoding='utf-8',quoting=csv.QUOTE_ALL)
