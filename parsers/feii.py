from parsers import base

def readFile(in_dir,file,cols):
    data = base.readData(in_dir+file, sep=",",encoding='latin-1')
    
    delete_columns = []
    for d in data.columns:
        if not d in cols:
            delete_columns.append(d)
            
    return data[list(set(data.columns)-set(delete_columns))]


indir="F:\\z_dados\\fei\\"

##
## LEI
##
## 39 atributos orignais, utilizados 12 sndo 5 match e 7 nonmatch

#data = base.readData(indir+file, sep=",")
file = "LEI.csv"

#read cols
match_cols = ['LegalNameCleaned','LegalAddress_Line_Cleaned','LegalAddress_City',
        'LegalAddress_Region_2','LegalAddress_PostalCode_5','LegalAddress_Country']
non_match_cols = ['Register','BusinessRegisterEntityID','EntityStatus',
                  'InitialRegistrationDate','RegistrationStatus',
                  'NextRenewalDate', 'LegalForm']
cols = match_cols + non_match_cols

print("Read data : %s" % file)
lei_data = readFile(indir,file,cols)
len(lei_data['Register'].unique())
del file ,cols , match_cols, non_match_cols


##
## sec
##
## 24 atributos orignais, utilizados 6 (5 OU 4)

file = "SEC.csv"

#read cols
match_cols = ['CONFORMED_NAME','B_STREET','B_CITY','B_STPR','B_POSTAL','B_COUNTRY']
non_match_cols = []
cols = match_cols + non_match_cols

print("Read data : %s" % file)
sec_data = readFile(indir,file,cols)
del file ,cols , match_cols, non_match_cols


base.writeData(lei_data,indir+'dumas_lei.csv',index=True)
base.writeData(lei_data,indir+'parsed_lei.csv')
base.writeData(sec_data,indir+'dumas_sec.csv',index=True)
base.writeData(sec_data,indir+'parsed_sec.csv')