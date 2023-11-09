# Tuples are immutables

numbers = (1,2,3,4)
stringsTuple = ('loquita', 'julio', 'maria', 'maria')

print('-1 =>', numbers[-1], type(numbers))

# Methods:
 
# Index
print(stringsTuple.index('maria'))

print(stringsTuple[1], "////////")

# Count
print(stringsTuple.count('maria'))

# list --- convert

new_list = list(stringsTuple)
print(new_list, type(new_list)) #['loquita', 'julio', 'maria', 'maria'] <class 'list'>

# tuple --convert
new_tuple = tuple(new_list)
print(new_tuple, type(new_tuple))


