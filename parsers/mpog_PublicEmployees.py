# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 09:59:34 2018

699023 registros 43 atributos

@author: Thiago
"""

import pandas as pd
import numpy as np
from parsers import base
import os
from datetime import datetime


def readFile(in_dir,file):
    return base.readData(in_dir+file, sep="\t", encoding="iso-8859-1")

indir ="F:"+os.path.sep+"z_dados"+os.path.sep+"PublicEmployees"+os.path.sep
ds = "mpog" + os.path.sep
file = "20160630_Cadastro.csv"

civil = readFile(indir+ds,file)

maybe = ['COD_ORG_EXERCICIO','COD_ORG_LOTACAO','COD_UORG_LOTACAO','COD_UORG_EXERCICIO']
delete_columns = ['NIVEL_CARGO','PADRAO_CARGO','TIPO_VINCULO',]

for d in list(civil.columns):
    if "_AFASTAMENTO" in d:
        delete_columns.append(d)

civil = civil[list(set(civil.columns)-set(delete_columns))]


file = "20160630_Remuneracao.csv"
remuneracao_civil = readFile(indir+ds,file)

keep = ['ANO', 'MES', 'ID_SERVIDOR_PORTAL','REMUNERAÇÃO BÁSICA BRUTA (R$)']
delete_columns = []

for d in list(remuneracao_civil.columns):
    if d not in keep:
        delete_columns.append(d)

remuneracao_civil = remuneracao_civil[list(set(remuneracao_civil.columns)-set(delete_columns))]

del d,delete_columns,file,keep,maybe

data = civil.merge(remuneracao_civil,how='inner',
                    left_on='Id_SERVIDOR_PORTAL', right_on='ID_SERVIDOR_PORTAL',
                   suffixes=('', 'FR_'))



data['MES_ANO'] = data['MES'].astype(str) + data['ANO'].astype(str)
delete_columns = ['Id_SERVIDOR_PORTAL','MES','ANO']
data = data[list(set(data.columns)-set(delete_columns))]


print("Dumas")
base.writeData(data.apply(lambda x: x.astype(str).str.replace(';','')),indir+'dumas_mpog.csv',index=True,dumasConvert=False)
print("BAP")
base.writeData(data,indir+'mpog.csv')


#file = "20160630_CadastroMilitares.csv"
#militar = readFile(indir+ds,file)