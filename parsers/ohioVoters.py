'''
Created on 24 de fev de 2017

@author: Thiago Nobrega
'''

import zipfile
import io

import csv

#head powershell
#gc log.txt | select -first 10 # head

from datetime import datetime
from parsers import base
import os

from datetime import datetime

def convertData(file,headers= 0,delimiter = '\,', quote=csv.QUOTE_ALL):
    """
        Read data from ziped file
    """
#     import codecs
#     f = codecs.iterdecode(file, "utf-8")
# #     f = codecs.iterdecode(file, "ISO-8859-1")
#     
#     data = []
#     
#     reader = csv.reader(f,delimiter=delimiter,quotechar='"',quoting=quote, skipinitialspace=True)
#     
#     count = 0
    
    
    from util.csvutil import readQuoted
    data = readQuoted(file,delimiter = ',')
    
    dm = []
    
    if(headers != 0):
        dm.append(headers)
        
    count = 0
    for row in data:
        dm.append(filterData(row))
#         count+=1
#         if count % 10000 == 0:
#             print(count)
     
    return dm

def filterData(data):
    row = data
#     fdata = []
    

    ##
    ## Adress Basic Data : data about voter adress
    #
    ### adress
    ### res_addr, res_city, res_state , res_zip 
    ead = [row[11] ,row[13] , row[14] , row[15] ]
    
    ##
    ## Personal Data : data about the voter (name,gender,bith,etc...)
    ##
    ### basic personal data
    ###  lastname , firstname , midlename ,  name_sufix 
    bpd = [ row[3],row[4],row[5],row[6] ]
    
    ### extra personal data
    ### birth_date , register_date
    epd = [ row[7], row[8] ]
    ### party 
    ### party_affiliation
    ext = [ row[10] ]
        
    entity = bpd + epd + ext + ead

    return entity


def listFiles(dir):
    import os
    lf = []
    for file in os.listdir(dir):
        if file.startswith("SWVF"):
            fr = os.path.join(dir, file)
            lf.append(fr)
    return lf

if __name__ == '__main__':
    
    dir = "F:\\etapa_02\\Voters\\Ohio\\"
    files = listFiles(dir)
    
    header = "lastname","firstname","middlename","namesufix","birth_date","register_date","party_affiliation","res_addr", "res_city", "res_state" , "res_zip"
    alldata = convertData(files[0],headers=header)
    print(len(alldata)) 
    for file in files[1:]:
        print(file)
        data = convertData(file)
        alldata += data
    
    print(len(alldata))
    print(alldata[0])
    print(alldata[1])
    
    
    
    
    file = dir + 'ohio_voters_striped_full.csv'
    from util.csvutil import write2csv2
    write2csv2(file,alldata)
    import sys
    sys.exit()
    
    print(file)
    
#     ofile  = open(outfile, "w" ,encoding="UTF-8")
#     writer = csv.writer(ofile, delimiter=out_delimiter, quotechar='"', quoting=quote ,lineterminator='\n')
#     
#     data = convertData(zfile, fo)
#     
    print("Done!")
    


#fast fix in data (remove later)
#"birth_date","register_date"
import zipfile
import io
import csv
from datetime import datetime
from parsers import base
import os

from datetime import datetime

def fix_date(din):
    d = str(din)
    dt = datetime.strptime(str(d),'%Y-%m-%d')
    newdate = str(dt.day) + "/" + str(dt.month) + "/" + str(dt.year)
    return newdate

in_dir ="F:"+os.path.sep+"z_dados"+os.path.sep+"us_voters"+os.path.sep
in_dir =os.path.sep+"home/thiago/dados"+os.path.sep+"us_voters"+os.path.sep
file = "ohio_voters_striped_full.csv"
data = base.readData(in_dir+file, sep=",")

data['birth_date'] = data['birth_date'].apply(fix_date)
data['register_date'] = data['register_date'].apply(fix_date)

base.writeData(data,in_dir+'ohio_voters.csv')


import sys
sys.exit()