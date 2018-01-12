# -*- coding: utf-8 -*-

import csv
import pandas as pd
import numpy as np
import scipy as sp
from datetime import datetime
from parsers import base
import os

in_dir ="F:"+os.path.sep+"z_dados"+os.path.sep+"Restaurants"+os.path.sep
file = "tripadvisor_data.csv"
data = base.readData(in_dir+file, sep=",")
base.writeData(data.apply(lambda x: x.astype(str).str.replace(';','')),in_dir+'dumas_trip.csv',index=True,dumasConvert=False)

import sys
sys.exit()


file="F:\\temp\\trip\\AK.csv"


headers = ['restaurant'] 
adress_labels = ['streetAddress', 'addressLocality', 'addressRegion_State', 'postalCode','Country']
review_labels = ['author','ratingValue','datePublished','ratingValue_2','reviewBody','ratingValue_3']
headers = headers + adress_labels + review_labels

data = pd.read_csv(file, sep=",",header=None)
data.columns = headers



#data.__getitem__('restaurant').__setitem__(0, str(data['restaurant'][0]).upper())

for i in range(0,len(data)):
    print(i)
    for j,header in enumerate(headers):
        if (str(data[header][i]).upper() == "NAN"):
            data.set_value(i,header,"")
        else:
            if (header == 'datePublished'):
                dt = datetime.strptime(str(data[header][i]).upper(), '%B %d, %Y')
                newdate = str(dt.day) + "/" + str(dt.month) + "/" + str(dt.year) 
                data.set_value(i,header,newdate)
            else:
                data.set_value(i,header,str(data[header][i]).upper())

        #data.__getitem__(header).__setitem__(i, str(data[header][0]).upper())
        #data[header][i] = str(data[header][i]).upper()
        
del data['ratingValue_2']
del data['ratingValue_3']
data['ratingValue'] = data['ratingValue'].astype(float)

### ohio
file='F:\\temp\\sac\\scratch\\ohio-b_random_selected_10000.csv'
data = pd.read_csv(file, sep=",")
for i in range(0,len(data)):
    for j,header in enumerate(data.columns):
        if (str(data[header][i]) == "nan"):
            data.set_value(i,header,"")
        else:
            if ((header == 'birth_date') or (header == 'register_date')):
                dt = datetime.strptime(str(data[header][i]), '%Y-%m-%d')
                newdate = str(dt.day) + "/" + str(dt.month) + "/" + str(dt.year) 
                data.set_value(i,header,newdate)

## ncvoters
file='F:\\temp\\sac\\scratch\\ncvoter-a_random_selected_10000.csv'
data = pd.read_csv(file, sep=",")
data['mail_zipcode'] = data['mail_zipcode'].map('{:.0f}'.format)

for i in range(0,len(data)):
    for j,header in enumerate(data.columns):
        if (str(data[header][i]) == "nan"):
            data.set_value(i,header,"")
        else:
            if (header == 'registr_dt'):
                dt = datetime.strptime(str(data[header][i]), '%m/%d/%Y')
                newdate = str(dt.day) + "/" + str(dt.month) + "/" + str(dt.year) 
                data.set_value(i,header,newdate)



data.to_csv('F:\\temp\\apagar.csv',index=False,encoding='utf-8',quoting=csv.QUOTE_ALL)
z = pd.read_csv('F:\\temp\\apagar.csv',sep=",").replace(np.nan, '', regex=True)

#I = pd.Index(a.columns_names, name="rows")
    
#ll = 12
#C = pd.Index(headers, name="columns")
#with codecs.open(file, mode='r', encoding='utf8') as f:
#    reader = csv.reader(f,delimiter=",",quotechar='"',quoting=csv.QUOTE_ALL, skipinitialspace=True)
#
#    pread = list(reader)
#    pdata = pd.DataFrame(index=range(0,len(pread)),columns=headers)
#    
#    index = 0
#    for row in pread:
#        if(ll != len(row)):
#            print("lascou")
#        nr = []
#        for i,att_name in enumerate(headers):
#            # date
#            if i == 8:
#                pass
#            else:
#                print("::" + att_name)
#                pdata[att_name][index] = "xXx"
#                #pdata[att_name][index] = row[i].upper()
        
#        nrdata.append(nr)
#        data.append(row)    
#        index += 1
#0 name
#1 address
#6 author
#7 grade
# 8 (date),9 (skip) ,10 (review) 
        
#        nr = []
#        for att in row:
#            att.
#linha = data[0]

from datetime import datetime
datestring = 'August 17, 2016'
dt = datetime.strptime(datestring, '%B %d, %Y')
print(dt.year, dt.month, dt.day)
#data = readQuoted(file,delimiter = ',')



###
### trip_2
### 
file='F:\\temp\\sac\\tripadvisor\\trip_AZ_IL_NC_NV_NY_OH_PA_SC_VT_WI.csv'
data = pd.read_csv(file, sep=",",header=None).replace(np.nan, '', regex=True)


labels = ['name','@type','priceRange','url','streetAddress', 'addressLocality',
          'addressRegion', 'postalCode','country','ratingValue','reviewCount']

states_1 = {
        'AK': 'Alaska', 'AL': 'Alabama', 'AR': 'Arkansas', 'AS': 'American Samoa',
        'AZ': 'Arizona', 'CA': 'California', 'CO': 'Colorado', 'CT': 'Connecticut',
        'DC': 'District of Columbia','DE': 'Delaware','FL': 'Florida','GA': 'Georgia',
        'GU': 'Guam','HI': 'Hawaii','IA': 'Iowa','ID': 'Idaho','IL': 'Illinois',
        'IN': 'Indiana','KS': 'Kansas','KY': 'Kentucky','LA': 'Louisiana','MA': 'Massachusetts','MD': 'Maryland',
        'ME': 'Maine','MI': 'Michigan','MN': 'Minnesota','MO': 'Missouri','MP': 'Northern Mariana Islands',
        'MS': 'Mississippi','MT': 'Montana','NA': 'National','NC': 'North Carolina','ND': 'North Dakota',
        'NE': 'Nebraska','NH': 'New Hampshire','NJ': 'New Jersey','NM': 'New Mexico',
        'NV': 'Nevada','NY': 'New York','OH': 'Ohio','OK': 'Oklahoma','OR': 'Oregon',
        'PA': 'Pennsylvania','PR': 'Puerto Rico','RI': 'Rhode Island','SC': 'South Carolina',
        'SD': 'South Dakota','TN': 'Tennessee','TX': 'Texas','UT': 'Utah','VA': 'Virginia',
        'VI': 'Virgin Islands','VT': 'Vermont','WA': 'Washington','WI': 'Wisconsin',
        'WV': 'West Virginia','WY': 'Wyoming'
}


states = {}
for s in states_1.keys():
    states[states_1[s].upper()] = s

states['LONG ISLAND'] = 'NY'
states['FINGER LAKE'] = 'NY'
states['CATSKILL REGION'] = 'NY'
states['BERKSHIRES'] = 'MA'
states['GREEN MOUNTAINS'] = 'VT'
states['JERSEY SHORE'] = 'NJ '
states['NORTHEAST KINGDOM'] = 'VT'
states['WHITE MOUNTAINS'] = 'NH'
states['UPPER PENINSULA'] = 'MI'
states[''] = 'NY'
states[''] = 'NY'

      
def getState(state):
    try:
        return states[state]
    except KeyError:
        for s in states.keys():
            if s in state:
                return states[s]
#        print(":::::: Error - " + state)
        return state

   
data.columns = labels

#deduplicating the dataset
keys = {}
drop_list = []
data['state'] = 'ZZ'

for i in range(0,len(data)):
    key = str(data['name'][i]) + str(data['addressRegion'][i]) + str(data['addressLocality'][i]) + str(data['streetAddress'][i])
    try:
        keys[key]
        drop_list.append(i)
    except KeyError:
        keys[key] = True
        for j,header in enumerate(data.columns):
            if header == 'priceRange':
                svar = data['priceRange'][i].split('-')
                if len(svar) == 1:
                    val = str(len(svar[0]))
                else:
                    val = str(len(svar[0])) + " - " +str(len(svar[1]))
                
                data.set_value(i,header,val)
            elif header == 'addressRegion':
                v = getState(data['addressRegion'][i])
                if len(v) > 2:
                    print("ERROR :: linha ::" + str(i))
                    #z.append(v)
                    #count +=1
                else:
                    data.set_value(i,'state',v)
                    data.set_value(i,header,str(data[header][i]).upper())
            else:
                data.set_value(i,header,str(data[header][i]).upper())

clean_data = data.drop(data.index[drop_list])

clean_data.to_csv('F:\\temp\\sac\\tripadvisor\\clean_data.csv',index=False,encoding='utf-8',quoting=csv.QUOTE_ALL)


     
                
#concat dataframes
pd.concat([data,clean_data])
                
                
                
dat = pd.read_csv('F:\\temp\\sac\\tripadvisor\\clean_data.csv', sep=",").replace(np.nan, '', regex=True)
#z = []
#count = 0
#for i in range(0,len(dat)):
#    v = getState(dat['addressRegion'][i])
#    if len(v) > 2:
#        z.append(v)
#        count +=1
#    else:
#        dat.set_value(i,'addressRegion',v)
#datc = dat.loc[dat['addressRegion'].isin(set(z))]

#dat.to_csv('F:\\temp\\sac\\tripadvisor\\clean_dat.csv',index=False,encoding='utf-8',quoting=csv.QUOTE_ALL)
