# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 10:46:35 2018

@author: Thiago
"""

from parsers import base
import pandas as pd
import os

def readFile(in_dir,file,cols,sep=";",encoding='latin-1'):
    data = base.readData(in_dir+file, sep=sep,encoding=encoding)
    
    delete_columns = []
    for d in data.columns:
        if not d in cols:
            delete_columns.append(d)
            
    return data[list(set(data.columns)-set(delete_columns))]


###############    IPTU
### 20 atributos
### 3.349.769 de resgistros

#colunas

cols_iptu = ['NUMERO DO CONTRIBUINTE', 'ANO DO EXERCICIO', 'NUMERO DA NL',
              'DATA DO CADASTRAMENTO', 'TIPO DE CONTRIBUINTE 1',
              'NUMERO DO CONDOMINIO', 'CODLOG DO IMOVEL',
              'NOME DE LOGRADOURO DO IMOVEL', 'NUMERO DO IMOVEL','COMPLEMENTO DO IMOVEL',
              'BAIRRO DO IMOVEL', 'REFERENCIA DO IMOVEL','CEP DO IMOVEL',
              'QUANTIDADE DE ESQUINAS/FRENTES','AREA DO TERRENO', 
              'VALOR DO M2 DO TERRENO', 'VALOR DO M2 DE CONSTRUCAO',
              'TIPO DE USO DO IMOVEL', 'TIPO DE PADRAO DA CONSTRUCAO',
              'ANO DE INICIO DA VIDA DO CONTRIBUINTE']


#indir =os.path.sep+"home/thiago/dados"+os.path.sep+"SP_Adresses"+os.path.sep
indir="F:\\z_dados\\SP_Adresses\\"


files = base.checkDir(indir+"IPTU"+os.path.sep)
data = readFile(indir+"IPTU"+os.path.sep,files[0],cols_iptu)
for file in files[1:]:
    print("Read data from IPTU : %s" % file)
    df = readFile(indir+"IPTU"+os.path.sep,file,cols_iptu)
    data = pd.concat([data,df])
    del df
del file ,files

##STANDARD FORMAT
#upercase
print("Converting to Standart Format...")

data = data.apply(lambda x: x.astype(str).str.upper())
#alternatica
#capitalizer = lambda x: x.upper()
#df['name'].apply(capitalizer)


print("Writing : IPTU")
base.writeData(data,indir+'parsed_iptu.csv')

#################### CNEF
### 8 atributos
### 65535 de resgistros

file='DEINFO_DADOS_US_CNEFE_2010.csv'
cols_cnef=['CEP','TIPO_LOGRA', 'NOME_LOGRA', 'NUMERO_EDI','LOCALIDADE',
      'ESPECIE_EN','IDENT_ESTA', 'NUM_FACE' , 'AREAP']
data = readFile(indir+"CNEF"+os.path.sep,file,cols_cnef,sep=",")

#criando o logradouro
#data['LOGRADOURO'] = data['TIPO_LOGRA'] + " " + data['NOME_LOGRA']
#data = data[list(set(data.columns)-set(['TIPO_LOGRA','NOME_LOGRA']))]

print("Writing : CNEF")
base.writeData(data,indir+'parsed_cnef.csv')

####
#### DUMAS
####

base.writeData(data,indir+'dumas_cnef.csv',index=True)

data = readFile(indir+"IPTU"+os.path.sep,'IPTU_Part_05_750K.csv',cols_iptu)
base.writeData(data,indir+'dumas_iptu.csv',index=True)



