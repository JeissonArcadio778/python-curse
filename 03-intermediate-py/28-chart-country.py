# Graficar el pais con sus poblaciones a lo largo de los años. 

import csv 
import re
import matplotlib.pyplot as plt 

years_list = {
    "2022" : "2022 Population",
    "2020" : "2020 Population",
    "2015" : "2015 Population",
    "2010" : "2010 Population",
    "2000" : "2000 Population",
    "1990" : "1990 Population",
    "1980" : "1980 Population",
    "1970" : "1970 Population",
}

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
    return result_country

def get_population_by_country(data): 
    
    country = input('Seleccione un país: ' ).capitalize()

    countries = list(filter(lambda item : item['Country/Territory'] == country, data))

    return { key: value for (key, value) in countries[0].items() if key in years_list.values()}

def generate_bar_chart(labels, values): 
    print('Charts!')
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()   

def get_population(data):
    
    new_dict = {}
    
    country = input('Seleccione un país: ' ).capitalize()

    #Obtengo la lista del pais
    
    countries = [x for x in data if x['Country/Territory'] == country]
    
    #Al ser una lista de diccionarios tomo su primer y unico valor 
    
    for key, value in countries[0].items():
    
        #Busco si la llave termina en 'ation' de 'Population'
    
        if key[-5:] == 'ation':
    
            #De ser así tomo los primeros 4 digitos como clave con su respectivo valor
            new_dict[key[0:4]] = value
            
    return new_dict


if __name__ == '__main__':
    data = read_csv('./world_population.csv')    
    result = get_population(data)
    print(result)

    result = get_population_by_country(data) 
    print(result)



    


