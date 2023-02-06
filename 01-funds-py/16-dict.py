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

# CREATE: 

person['nickname'] = 'yeye'


# UPDATE: 

person['name'] = 'Eduardo'
person['age'] -= 8

# Its a list:
person['langs'].append('Go')

print(person)


# DELETE: 

del person['last_name']

person.pop('age') # Is necessary the argument 
print(person)

# Other Methods: 

# *they return in tuples*
print('Items')
print(person.items())

print('Keys')
print(person.keys())

print('Values')
print(person.values())

# Items
# dict_items([('name', 'Eduardo'), ('langs', ['NodeJS', 'Python', 'Go'])])
# Keys
# dict_keys(['name', 'langs'])
# Values
# dict_values(['Eduardo', ['NodeJS', 'Python', 'Go']])

# Convert tuples tu lists

k = list(person.keys())
v = list(person.values())
print(k)
print(v)