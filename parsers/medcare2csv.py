'''
Created on 25 de fev de 2017

@author: Thiago Nobrega
'''


def readData(file):
    from util.csvutil import readQuoted
    data = readQuoted(file)
    return data
    

def filterData(data,header):
    
    fdata = []
    fdata.append(header)
    
    
    for row in data:
        
        if (row[6] == 'I'):
            #npi,lastname,firstname,middle inicial, credencia, gender, street1,street2, city , zip , state , country , especiality 
            entity = [row[0],row[1],row[2],row[3] , row[4] , row[5] , row[7] , row[8] , row[9] , row[10] , row[11] , row[12] , row[13]]
            fdata.append(entity)
    
    
    return fdata


if __name__ == '__main__':
    filet = "F:\\temp\\Medicare_Physician_and_Other_Supplier_NPI_Aggregate_CY2014.txt"
    
    data = readData(filet)
    print("read!")
    
    header = ['npi','lastname','firstname','middlename_inicial', 'credencia', 'gender', 'street1' , 'street2' , 'city' , 'zip' , 'state' , 'country' , 'especiality' ]
    fd = filterData(data,header)
    
    print("filter!")
    
    print(fd[0])
#     print(data[1])
    print(fd[1])
#     print(data[2])
    print(fd[2])
#     print(data[3])
    print(fd[3])
    
    from util.csvutil import write2csv2
     
    fo = "F:\\temp\\medpos.csv"
    write2csv2(fo,fd)
#     
    print("Done!")