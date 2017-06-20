'''
Created on 24 de fev de 2017

@author: Thiago Nobrega
'''

def readData(file):
        
    
    with open(file, 'r') as f:
        
        separator = ";"
        header = "doc_number","lastname","firstname","midnamesufix","gender","race","brith"
        
        data = []
        data.append(header)
        #trim
        for line in f:
            #DOC number
            doc_number= line[1:8].strip()
            #lastname
            lastname = line[8:27].strip()
            #fistname
            firstname = line[27:38].strip()
            # mid name suffic
            midname_sufix = line[38:39].strip()
            gender = line[46:75].strip()
            race = line[76:106].strip()
            birthdate = line[106:116].strip()
            
            entite = doc_number , lastname , firstname , midname_sufix , gender , race , birthdate
            
            data.append(entite)
            
        return data

if __name__ == '__main__':
    filet = "F:\\temp\\INMT4AA1.dat"
    
    data = readData(filet)
    
    from util.csvutil import write2csv2
    
    fo = "F:\\temp\\INMT4AA1.csv"
    write2csv2(fo,data)
    
    print("Done!")