'''
Created on 15 de jun de 2016

@author: Thiago Nobrega
@mail: thiagonobrega@gmail.com
'''

import csv

def readQuoted(file, delimiter = '\t', headers = False):
    """"
        Read a csv file with comma
        delimiter : comma (,) default
        headers : include headers in return
        
        return : list of rows (list) e.g: [[id,name,date],[1,joao,21],[2,maria,19]]  
    """
    rows = []
    with open(file, 'r') as f:
        reader = csv.reader(f,delimiter=delimiter,quotechar='"',quoting=csv.QUOTE_ALL, skipinitialspace=True)
        for row in reader:
            rows.append(row)
    if not headers:
        rows = rows[1:]
    return rows

def readZipedQuoted(file, delimiter = '\t', headers = True):
    """"
        Read a zipped csv file with \t 
        delimiter : comma (,) default
        headers : include headers in return
        
        return : list of rows (list) e.g: [[id,name,date],[1,joao,21],[2,maria,19]]  
    """
    rows = []    
    reader = csv.reader(file,delimiter=delimiter,quotechar='"',quoting=csv.QUOTE_ALL, skipinitialspace=True)
    
    for row in reader:
        rows.append(row)
        
    if not headers:
        rows = rows[1:]
    return rows


def read(file, delimiter = ',', headers = False):
    """"
        Read a csv file with comma
        delimiter : comma (,) default
        headers : include headers in return
        
        return : list of rows (list) e.g: [[id,name,date],[1,joao,21],[2,maria,19]]  
    """
    rows = []
    with open(file, 'r' , encoding='utf-8') as f:
        reader = csv.reader(f,delimiter=delimiter)
        for row in reader:
            rows.append(row)
    if not headers:
        rows = rows[1:]
    return rows

def write2csv(outfile,data,delimiter=';', quote=csv.QUOTE_NONE ):
    """"
        Write a csv file 
        data : a list of list to be 
        delimiter : dot comma (;) default  
    """
    ofile  = open(outfile, "w")
    writer = csv.writer(ofile, delimiter=delimiter, quotechar='"', quoting=quote ,lineterminator='\n')
    #writer = csv.writer(ofile, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    for row in data:
        writer.writerow(row)
    ofile.close()

def write2csv2(outfile,data,delimiter=',', quote=csv.QUOTE_NONNUMERIC ):
    """"
        Write a csv file 
        data : a list of list to be 
        delimiter : comma (,) default  
    """
    ofile  = open(outfile, "w")
    writer = csv.writer(ofile, delimiter=delimiter, quotechar='"', quoting=quote ,lineterminator='\n')
    #writer = csv.writer(ofile, delimiter=';', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    for row in data:
        writer.writerow(row)
    ofile.close()