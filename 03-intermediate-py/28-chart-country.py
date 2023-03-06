# Graficar el pais con sus poblaciones a lo largo de los años. 

import csv 
import re

def read_csv(path):

    with open(path, 'r') as file_csv: 
        
        reader = csv.reader(file_csv, delimiter = ',')
        
        header = next(reader)
        
        data = []
        
        for row in reader: 
            
            iterable = zip(header, row)
            
            country_dict = { key : value for key, value in iterable}

            data.append(country_dict)

            return data

def get_country(country, data):
    
    result_country = list(filter(lambda item : item['Country/Territory'] == country, data))
    print(result_country)
    return result_country

def get_population_by_country(country):

    # if 'Population' in country:
    pass 
        

if __name__ == '__main__':
    data = read_csv('./world_population.csv')
    print(data[0])
    
    user_country = input('Hello, please send the country: ')
    
    country = get_country(user_country, data); 


    


