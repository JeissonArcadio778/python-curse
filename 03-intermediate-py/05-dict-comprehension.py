
'''
dict_num = {}
for i in range(1,6):
    dict_num[i] = i * 2
print(dict_num)   # {1: 2, 2: 4, 3: 6, 4: 8, 5: 10} 

dict_num_ls_cmp = {i: i* 2 for i in range(1,6)}
print(dict_num_ls_cmp)   # {1: 2, 2: 4, 3: 6, 4: 8, 5: 10} 
'''

# we can use more fors? and ifs in the sentences:
countries = ['mx', 'col', 'brz', 'arg']
dict_countries = {i:country for country in countries for i in range(len(countries))}
print(dict_countries) # {0: 'arg', 1: 'arg', 2: 'arg', 3: 'arg'}


# Other example
import random

countries = ['mx', 'col', 'brz', 'arg']
population = {}

for country in countries: 
    population[country] = random.randint(1, 100)
print(population) # {'mx': 5, 'col': 49, 'brz': 97, 'arg': 74}


population = { country : random.randint(1,100) for country in countries}
print(population) # {'mx': 22, 'col': 80, 'brz': 85, 'arg': 13}

# union two list to convert to dictionary 
names = ['yy', 'lokita', 'maria', 'julio']
ages = [22,21,21,99]
dict_person = {names[i]: ages[i] for i in range(len(names))}
print(dict_person)