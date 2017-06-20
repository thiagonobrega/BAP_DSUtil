'''
Created on 20 de jun de 2017

This class manipulate datasets, creating compound attributes in dataset. 
As an example you can transform a dataset A (lastname,firstname, dob) in B( fullname ,don).

Where Fullname is a compound attributs (firstname + lastname)

@author: Thiago Nobrega
'''
import csv
import random 
import time

def check(dirToScreens):
    import os
    from os import path
    files = []
    for f in os.listdir(dirToScreens):
        if f.endswith(".csv"):
            files.append(f)
    return files

def convertData(file,atrributeName,attributeParts,delimiter = ',', quote=csv.QUOTE_ALL):
    """
        Read data from ziped file
    """
    
    from util.csvutil import readQuoted
    data = readQuoted(file,delimiter = ',', headers=True)
    
    dm = []        
    count = 0
    
    for row in data:
        if count == 0: # headers
            dm.append(convetRowHeaders(row, atrributeName, attributeParts))
        else:    
            dm.append(convetRow(row,attributeParts))
        
        count += 1
        
    
    return dm

def convetRow(row,attributeParts,separator=" "):
    lenr = len(row)
    c = 0
    newatt = ""
    
    for j in attributeParts:
        if c == 0:
            newatt = row[j]
        else:
            if row[j] != "":
                newatt += " " + row[j]
            
        c += 1
    
    nr = [ newatt ]
    for i in range(0,lenr):
        if i not in attributeParts:
            nr.append(row[i])
    
    return nr

def convetRowHeaders(row,newlabel,attributeParts,separator=" "):
    lenr = len(row)
    
    nr = [ newlabel ]
    for i in range(0,lenr):
        if i not in attributeParts:
            nr.append(row[i])
        
    return nr
            
    
if __name__ == '__main__':
    
    import argparse

    parser = argparse.ArgumentParser(
        description='Exemplo',
    )
    
    parser.add_argument('dir', action="store", help='Original file')
    
    parser.add_argument('-outdir', dest='outdir',
                        action="store", help='Original file')
    
    parser.add_argument('-an', dest='att_name', 
                        action="store", help='Original file')
    
    parser.add_argument('-ap', action='append',
                        dest='att_parts',
                        default=[],
                        help='Compaund attribute position')
    
    
    args = parser.parse_args()
    dir = args.dir
    outdir = args.outdir
    
    attName = args.att_name
    attParts = []
    
    for i in args.att_parts:
        attParts.append(int(i))
    
    files = check(dir)
    
    try:
        import os
        os.makedirs(outdir)
    except FileExistsError:
        print("Path ja criado")
            
    for file in files:
        md = convertData(dir+ os.sep +file, attName, attParts)
        
        from util.csvutil import write2csv2
        fname = file.split('.csv')[0]
        
        p = "" #compound attribute identification        
        for j in attParts:
            p += "-" + str(j)
        
        out = outdir + os.sep + fname + "_" + attName + p + ".csv" 
        print(out)
        write2csv2(out,md)
        
    
    
    