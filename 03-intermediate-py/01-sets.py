# Conjuntos = sets

"""
    - They dont have duplicates items.
    - Doesn't have order
    - They can be modify

"""

set_countries = {'col', 'mx', 'bol', 'col'}
print(set_countries, type(set_countries))


set_types = {'Hello', True, 123, 12.2}
print(set_types, type(set_types))

# Create a Set from String
set_from_string = set("Hellooo")
print(set_from_string) # {'l', 'e', 'o', 'H'}

# Create a Set from tuple
set_from_tuple = set(('col', 'mx', 'bol', 'col'))
print(set_from_tuple)

# Create a Set from list
numbers = [1,2,3,1,2,3,4,5,6]
set_from_list = set(numbers)
print(set_from_list) # {1, 2, 3, 4, 5, 6}
unique_numbers = list(set_from_list)
print(unique_numbers) # [1, 2, 3, 4, 5, 6]
