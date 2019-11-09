import pandas as pd
import csv

headers = ['caseNumber', 
'treatmentDate', 
'statWeight', 
'stratum', 
'age', 
'sex', 
'race', 
'diagnosis', 
'bodyPart', 
'disposition', 
'location', 
'product']

sens_data = ['caseNumber', 
'treatmentDate',
'bodyPart',
'location']

data = {}

def get_anonymised_data():
    anon_data = {}
    required_heads = []
    for i in headers:
        if i not in sens_data:
            anon_data[i] = []
            required_heads.append(i)
    l = len(data['age'])
    print('Initialisation done')
    print('Total entries : ',l)
    for i in range(l):
        for j in required_heads:
            if(j in ['age','statWeight']):
                t1 = int(float(data[j][i]))
                t2 = (t1//10)*10
                st = str(t2)+" - "+str(t2+10)
                anon_data[j].append(st)
            else:
                anon_data[j].append(data[j][i])
    print('Processed entries : ',len(anon_data['age']))
    print('Now writing data to the result.csv file')
    with open('result.csv',mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(required_heads)
        for i in range(l):
            itter = []
            for j in required_heads:
                itter.append(anon_data[j][i])
            writer.writerow(itter)
    print('Anonymised data written in result.csv')

def store_data():
    with open('nss15.csv') as f:
        csvread = csv.reader(f)
        header = True
        for row in csvread:
            if(header):
                header = False
                for i in row:
                    data[i] = []
                continue
            for i in range(len(row)):
                data[headers[i]].append(row[i])

if __name__ == "__main__":
    store_data()
    get_anonymised_data()