# Dictionaries 

my_dict = {
    'name' : 'Jeisson',
    'last_name' : 'Beltran',
    'age' : 22
}

print(my_dict, type(my_dict), len(my_dict))
print(my_dict['age']) #22
print(my_dict.get('avalue')) # None or this real value
print('name' in my_dict) # True

# CRUD

person = {
    'name' : 'Jeisson',
    'last_name' : 'Beltran',
    'age' : 22, 
    'langs': ['NodeJS', 'Python']
}

# Update: 

person['name'] = 'Eduardo'
person['age'] -= 8
# Its a list
person['langs'].append('Go')

print(person)
