
import utils

from utils import get_population_by_country

result = utils.get_items()
print(result)


list_countries = [
    {
        'country' : 'colombia', 
        'population' : 1000
    },
    {
        'country' : 'chile', 
        'population' : 1200
    }
]

result = get_population_by_country(list_countries, 'colombia')
print(result)







