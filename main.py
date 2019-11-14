# Import all the required libraries first
# Use pip install <name> if got some error while importing
import pandas as pd
import csv

# Initialize the array with all the dataset headers (attributes)
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

# List of all the sensitive attributes which is has to be anonymised
sens_data = ['caseNumber', 
'treatmentDate',
'bodyPart',
'location']

data = {}

# Function to load the csv data into variable $data which is a dictionary
def store_data():
    # Reading the input csv file
    with open('nss15.csv') as f:
        csvread = csv.reader(f)
        # Use a flag to skip the 1st row i.e header data 
        header = True
        for row in csvread:
            if(header):
                header = False
                for i in row:
                    # Adds a empty list as value for key as the header name
                    data[i] = []
                continue
            # Now just fill the data into respective header as a key
            for i in range(len(row)):
                data[headers[i]].append(row[i])
        # So the csv vertical data is stored in a temporary form of a dictionary
        # to be used afterwards in the same python file

# Function which will return the anonymised data
def get_anonymised_data():
    # Intialisation on variables
    anon_data = {}
    required_heads = []
    for i in headers:
        #Check whether the attribute is sensitive or not and add into the return dataset
        if i not in sens_data:
            anon_data[i] = []
            required_heads.append(i)
    l = len(data['age'])
    print('Initialisation done')
    print('Total entries : ',l)
    # Loop through all the records
    for i in range(l):
        for j in required_heads:
            # check whether the attributes belongs to dependent sensitive attributes
            # which are age and weight to convert them into interval 
            if(j in ['age','statWeight']):
                # converting the float to an interval of 10's
                t1 = int(float(data[j][i]))
                t2 = (t1//10)*10
                st = str(t2)+" - "+str(t2+10)
                # getting the string ready and putting it into the result dataset
                anon_data[j].append(st)
            else:
                # simply copy paste the original data as its not sensitive
                anon_data[j].append(data[j][i])
    print('Processed entries : ',len(anon_data['age']))
    print('Now writing data to the result.csv file')
    # now write the generated data into the csv file names result.csv
    with open('result.csv',mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(required_heads)
        for i in range(l):
            itter = []
            for j in required_heads:
                itter.append(anon_data[j][i])
            writer.writerow(itter) # prints a row in the file
    print('Anonymised data written in result.csv')

# main function gets called automatically whenever the main.py is initialised
if __name__ == "__main__":
    store_data() # retrive data into memory
    get_anonymised_data() # process the data and store it into result.csv