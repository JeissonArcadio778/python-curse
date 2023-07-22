#01-funds

print('Hello World')
name: str = input("whats your name? ")
words:str = f'Welcome {name} !!!'
print(words)

# Type
print(type(name))

# Stings: are inmutables
print(words.count('e')) 
if words.startswith('Wel'):
    print('Yes!' * 3)
print(words.replace('Welcome', 'Hello')) 

# Arith
print(2//3) # Int divition 

#Floats
print(1.1 + 2.2) #3.300000...
print(round( 1.1 + 2.2 ), 1) # 3.1 =~ n < 5

#Lists
numbers = [1,2,3,4,5,6,7,8]
people = ['loquita', 'julio', 'maria']
print(1 in numbers) # Tue
print(numbers[-1]) # 8
numbers.append(700)
numbers.insert(0,'Not reemplace') # Don't delete
numbers.index(2) # 1
people.remove('maria')
people.pop()
people.pop(0)
numbers.reverse()
lists = numbers + people
sorting_letters = ['z', 'e', 'a', 'r']
sorting_letters.sort()

#Tuples: are inmutables
numbers = (1,2,3,4,5)
names = ('loquita', 'loquito')
"""
index, count, convert tuple() - list()
"""

#Dicts: 
presidentOfUSA = {
    'name': 'Fank',
    'last_name': 'Underwood',
    'age': 55,
    'skin': 'white',
    'kills': ['Peter Russi', 'Zoe Bares'],
}
president_last_name = presidentOfUSA.get('last_name')
print(f"Francis {presidentOfUSA['last_name']}")
print(presidentOfUSA['kills'][1]) # Zoe...

# CRUD
presidentOfUSA['isSingle'] = True
presidentOfUSA['kills'].append('Remy')

presidentOfUSA['isSingle'] = False
presidentOfUSA['age'] += 3

del presidentOfUSA['last_name']
presidentOfUSA.pop('skin')
print(presidentOfUSA)

# Some methos
print("Keys:::", list(presidentOfUSA.keys()))
print("Values:::", list(presidentOfUSA.values()))
print("Items:::", list(presidentOfUSA.items())) # [(),()]

#Loops

counter = 0
while counter < 20:
    print(f"Counter in: {counter}")
    if counter == 15:
        print('break, STOP!')
        break
    counter += 1

counter = 0
while counter < 20:
    counter += 1
    if counter < 15:
        print('Continue...')
        continue
    print(f"Counter in: {counter}")

# For, for conditions

for number in range(20): # 0-19
    print(number)

for number in numbers:
    print(number)

for key in presidentOfUSA.keys():
    print(key)

for values in presidentOfUSA.values():
    print(values)

for key, value in presidentOfUSA.items():
    print(f"The Key is {key} and this value: {value}")

# Example:
data_harry = [
    {
        "name": "Hermione Granger",
        "species": "human",
        "gender": "female",
    },
     {
    
        "name": "Harry Potter",
        "species": "human",
        "gender": "male",     
    },
]

for person in data_harry:
    print(person['name'])

# loops anidados

matriz = [
  [1, 2, 3], 
  [4, 5, 6], 
  [7, 8, 9]
]

for i in range(3): 
    for j in range(3):
        print(matriz[j][i])

print('----------------')

for row in matriz:
    print(row)
    for column in row:
        print(column)
