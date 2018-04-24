# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 09:59:34 2018

371480 registros 15 atributos

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
#indir =os.path.sep+"home/thiago/dados"+os.path.sep+"PublicEmployees"+os.path.sep

ds = "mpog" + os.path.sep
file = "20160630_Cadastro.csv"

civil = readFile(indir+ds,file)

#'DESCRICAO_CARGO',
#'UORG_LOTACAO', , 'ORG_LOTACAO',

delete_columns = ['COD_ORG_EXERCICIO','COD_ORG_LOTACAO','NIVEL_CARGO','SIGLA_FUNCAO', 'REGIME_JURIDICO','PADRAO_CARGO',
'TIPO_VINCULO','CODIGO_ATIVIDADE','DOCUMENTO_INGRESSO_SERVICOPUBLICO', 'DIPLOMA_INGRESSO_ORGAO','ID_SERVIDOR_PORTAL',
'OPCAO_PARCIAL','DATA_INGRESSO_CARGOFUNCAO','DATA_INGRESSO_ORGAO','SITUACAO_VINCULO', 'DIPLOMA_INGRESSO_SERVICOPUBLICO',
'DIPLOMA_INGRESSO_CARGOFUNCAO','COD_ORGSUP_EXERCICIO', 'UORG_EXERCICIO','CLASSE_CARGO', 'ORGSUP_LOTACAO','REFERENCIA_CARGO',
'FUNCAO', 'DATA_NOMEACAO_CARGOFUNCAO','NIVEL_FUNCAO','COD_ORGSUB_LOTACAO',
'COD_UORG_LOTACAO','ATIVIDADE','COD_UORG_EXERCICIO','COD_ORGSUP_LOTACAO']
 

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

del d,delete_columns,file,keep

data = civil.merge(remuneracao_civil,how='inner',
                    left_on='Id_SERVIDOR_PORTAL', right_on='ID_SERVIDOR_PORTAL',
                   suffixes=('', 'FR_'))



#data['MES_ANO'] = data['MES'].astype(str) + data['ANO'].astype(str)
delete_columns = ['Id_SERVIDOR_PORTAL','ID_SERVIDOR_PORTAL']
data = data[list(set(data.columns)-set(delete_columns))]

for i in data.columns:    
    try:
        data = data[data[i]!='']
    except TypeError:
        pass


print("Dumas")
#base.writeData(data.apply(lambda x: x.astype(str).str.replace(';','')),indir+'dumas_mpog.csv',index=True,dumasConvert=False)
print("BAP")
base.writeData(data,indir+'mpog.csv')


#file = "20160630_CadastroMilitares.csv"
#militar = readFile(indir+ds,file)