'''
Created on 24 de fev de 2017

@author: Thiago Nobrega
'''

import zipfile
import io

import csv

#head powershell
#gc log.txt | select -first 10 # head

def convertData(file,outfile,delimiter = '\t', out_delimiter=',', quote=csv.QUOTE_ALL):
    """
        Read data from ziped file
    """
    import codecs
#     f = codecs.iterdecode(file, "utf-8")
    f = codecs.iterdecode(file, "ISO-8859-1")
    
    
    
    
    data = []
    
    reader = csv.reader(f,delimiter=delimiter,quotechar='"',quoting=csv.QUOTE_ALL, skipinitialspace=True)
    
    ofile  = open(outfile, "w" ,encoding="UTF-8")
    writer = csv.writer(ofile, delimiter=out_delimiter, quotechar='"', quoting=quote ,lineterminator='\n')
    
    count = 0
    
    for row in reader:
#         data.append(filterData(row))
        writer.writerow(filterData(row))
        count+=1
        if count % 100000 == 0:
            print(count)
    
    ofile.close() 

    return data

def filterData(data):
    row = data
#     fdata = []
    

    ##
    ## Adress Basic Data : data about voter adress
    ##
    ### basic
    ###    county ,street,city,state,zip, phone
    #bad = [row[1],row[13],row[14],row[15],row[16], row[24]]
    
    ###    county , phone
    bad = [row[1], row[24]]
    
    ### extra
    ### mail_adddr1,mail_addr2,mail_city,mail_state,mail_zip
    #ead = [row[17] ,row[18] , row[21] , row[22] , row[23] ]
    ### mail_adddr1,mail_city,mail_state,mail_zip
    ead = [row[17] , row[21] , row[22] , row[23] ]
    
    ##
    ## Personal Data : data about the voter (name,gender,bith,etc...)
    ##
    ### basic personal data
    ### voter_id, lastname , firstname , midlname ,  name_sufix , gender, age , race , ethinic
    #bpd = [ row[2],row[9],row[10],row[11],row[12],row[28],row[29], row[25],row[26] ]
    ### lastname , firstname , midlname ,  name_sufix , gender, age , race , ethinic
    bpd = [ row[9],row[10],row[11],row[12],row[28],row[29], row[25],row[26] ]
    ### extra personal data
    ### birth_place , register_date ,ncid
    #epd = [ row[30], row[32], row[68] ]
    ### birth_place , register_date
    epd = [ row[30], row[32] ]
        
    entity = bpd + bad + epd + ead
#     fdata.append(entity)

    
    return entity

def filterDataO(data):
    
    fdata = []
    
    for row in data:
        print(row)
        ##
        ## Adress Basic Data : data about voter adress
        ##
        ### basic
        ###    county ,street,city,state,zip, phone
        bad = [row[1],row[13],row[14],row[15],row[16], row[24]]
        ### extra
        ### mail_adddr1,mail_addr2,mail_city,mail_state,mail_zip
        ead = [row[17] ,row[18] , row[21] , row[22] , row[23] ]
        
        ##
        ## Personal Data : data about the voter (name,gender,bith,etc...)
        ##
        ### basic personal data
        ### voter_id, lastname , firstname , midlname ,  name_sufix , gender, age , race , ethinic
        bpd = [ row[2],row[9],row[10],row[11],row[12],row[28],row[29], row[25],row[26] ]
        ### extra personal data
        ### birth_place , register_date ,ncid
        epd = [ row[30], row[32], row[68] ]
            
        entity = bpd + bad + epd + ead
        fdata.append(entity)
    
    
    return fdata

def listFiles(dir):
    import os
    for file in os.listdir(dir):
        if file.startswith("ncvoter"):
            print(os.path.join(dir, file))

if __name__ == '__main__':
    
    dir = "F:\\Arquivo_Morto\\DataSet\\US\\NC_Voter\\"
#     listFiles(dir)
#     import sys
#     sys.exit()
    
    file = dir + 'ncvoter_Statewide.zip'
    print(file)
    
#     file = "F:\\temp\\ncvoter3.zip"
    
    z = zipfile.ZipFile(file,'r')    
#     data = z.read(z.infolist()[0])

    zfile = z.open(z.namelist()[0])
    
#     for line in zfile:
#         print(line)
    
    fo = "F:\\temp\\ncvoter.csv"
    
    data = convertData(zfile, fo)
#     
    print("Done!")