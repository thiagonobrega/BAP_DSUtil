'''
Created on 14 de mar de 2017

Pick a sample from a file

@author: Thiago Nobrega
'''
import csv
import random 
import time

def selectRandom(n,fin,lineNumber,percent,reposition=True,encode="UTF-8"):
    """
        n : number of samples
        fin : Input file
        lineNumber: Number of line in orginal file
        percent : number of records of the sample
    """
    
    data_in = open(fin,'rt')
    
    #fp = codecs.iterdecode(file, "ISO-8859-1")
    import string
    sl = list(string.ascii_lowercase)
    
    
    set_of_lines = []
    fp_outs = []
    
    #abrindo os files outs
    for i in range(0,n):
        lines = []
        set_of_lines.append(lines)
        fout = fin.split(".")[0]+"-"+sl[i] + "_random_selected_" + str(percent) + ".csv"
        
        data_out = open(fout, "w" ,encoding="UTF-8")
        fp_outs.append(data_out)
        
    
    sample_size = percent
    
    if percent >= lineNumber:
        sample_size = lineNumber
        
    # escolhendo as linhas
    for i in range(0,n):
        for j in range(0,int(sample_size)):
            num = random.randrange(1, lineNumber,1)
            
            if (not reposition):
                while num in lines:
                    num = random.randrange(1, lineNumber,1)
            
            set_of_lines[i].append(num)
            
    
    reader = csv.reader(data_in,delimiter=',',quotechar='"',quoting=csv.QUOTE_ALL, skipinitialspace=True)
    
    # create file writers
    lists_of_csv_writers = []
    for j in range(0,n):
        writer = csv.writer(fp_outs[j], delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL ,lineterminator='\n')
        lists_of_csv_writers.append(writer)
        
    
    i = 0
    selectedLines = []
    
    for line in reader:
        for j in range(0,n):
            local_writer = lists_of_csv_writers[j]
            #header
            if i == 0:
                local_writer.writerow(line)
                #selectedLines.append(line)
            
            if i in set_of_lines[j]:
                local_writer.writerow(line)
                #print(line)
        i +=1
    
    for i in range(0,n):
        fp_outs[i].close()
    
    data_in.close()
    r = []
    
    for lines in set_of_lines:
        r.append(len(lines))
    return r

def wcl(file,encode):
    n = 0
    with open(file) as f:
        n = sum(1 for _ in f)
    return n
    
if __name__ == '__main__':
    
    import argparse

    parser = argparse.ArgumentParser(
        description='Example with nonoptional arguments',
    )
    parser.add_argument('file', action="store", help='Original file')
    
    parser.add_argument('-n', action="store", dest='num_file' ,
                        help='num of files')

    parser.add_argument('-p', action='append',
                        dest='percents',
                        default=[],
                        help='Generate a newsubset with a -p percent of original dataset')
    
    args = parser.parse_args()
    percents = args.percents
    fin = args.file
    n = int(args.num_file)
    
    #encoding = "utf_16_le"
    #fin = "F:\\temp\\ncvoter3.csv"
    #n = 2
    #percents = [10]
    
    
    lineNumber = wcl(fin,"UTF-8") - 1
                    
    print("Linhas arquivo Original : %d" % lineNumber)

    for percent in percents:
        now = time.ctime()
        print("Gerando arquivos para ("+ str(fin) +") com %d linhas as  [ %s ] " % (int(percent), now) )
        lll = selectRandom(n,fin,lineNumber,int(percent),)
        print(lll)
        now = time.ctime()
        print("Arquivo gerado ("+ str(fin) +") as [ %s ] " % now)
    
    print("Done!")