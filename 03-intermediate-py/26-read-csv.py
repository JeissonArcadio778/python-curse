import csv 

def read_csv(path):

    with open(path, 'r') as file_csv: 
        reader = csv.reader(file_csv, delimiter = ',')


