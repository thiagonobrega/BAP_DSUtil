'''
Created on 27 de jun de 2017

@author: Thiago
'''

import json
import csv

def json2csv(jsonFile,csvFilePath):
    jsonData = json.loads(jsonFile)
    jdata = jsonData['employee_details']

    # open a file for writing
    csvFile = open(csvFilePath, 'w')
    csvwriter = csv.writer(csvFile)

    count = 0
    
    for row in jdata:
        if count == 0:
            header = row.keys()
            csvwriter.writerow(header)
            count += 1

        csvwriter.writerow(row.values())

    csvFile.close()

def owl2csv():
    pass
