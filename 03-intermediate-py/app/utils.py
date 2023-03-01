
def get_items():
    keys = ['Mazda', 'BMW']
    values = ['CX5', 'BMcito']
    return keys, values 

def get_population_by_country(list_countries, country):
    print('get population')
    return list(filter(lambda item : item['country'] == country, list_countries))