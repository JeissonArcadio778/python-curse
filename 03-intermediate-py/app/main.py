
import utils

from utils import get_population_by_country

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


def run(): 
    result = utils.get_items()
    print(result)

    result = get_population_by_country(list_countries, 'colombia')
    print(result)

# if is running from shell, run it, but if runnig from other file, not run it
if __name__ == '__main__':
    run()





