# Is easier to read and use that syntaxes  


'''
# The normal use: 
numbers = []
for element in range(1,11): 
    numbers.append(element*2)
print(numbers) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# List comprehension: 
numbers_lscom = [element * 2 for element in range(1,11)]
print(numbers_lscom) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

'''

# Using if
numbers = []
for element in range(1,26):
    if element % 2 == 0: 
        numbers.append(element*2)
print(numbers) # [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48]

numbers_ls_cmp = [i * 2 for i in range(1,26) if i % 2 == 0]
print(numbers_ls_cmp) # [4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48]


