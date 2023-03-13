set_countries = {'col', 'mx', 'bol', 'col'}


size = len(set_countries)
print(size) #3

print('peru' in set_countries) # False


# CRUD

# CREATE
set_countries.add('pe')
set_countries.add('us')
print(set_countries)

# UPDATE
set_countries.update({'ar', 'ecua', 'pe'})
print("Update", set_countries)

# DELETE
set_countries.remove('ar') # If not exists: Error.
set_countries.discard('arg') # If the element is not a member, do nothing.
print(set_countries)

set_countries.clear()
print(len(set_countries)) # 0

