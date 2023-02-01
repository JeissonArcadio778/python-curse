# WHILE: continue and break

counter = 0

while counter < 20:
    # counter = counter + 1
    
    counter += 1
    
    # print(f"Hello World: {counter} times") 

    if counter == 15:
        # print('STOP! - break')
        break



while counter < 20:
    # counter = counter + 1
    counter += 1
    if counter < 15:
        continue # Continue to complete the sentence
    # print(counter)


# FOR: is used when we have some number of conditions for some element

for element in range(20): # 0-19
    print(element)


numbers = [23,21,44,56,33]
for element in numbers:
    print(element)


tuple_names = ('yeye', 'loquita', 'marianita')
for name in tuple_names:
    print(name)


person = {
    'name' : 'loquita',
    'job' : 'Eulajecutiva',
    'age' : 21
}

for key in person:
    # print(key)
    print(key, '=>', person[key])

for key, value in person.items():
    # print(key)
    print(key, '=>', value)

# name => loquita
# job => Eulajecutiva
# age => 21


# IMPORTANT:

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
    {
        "name": "Ron Weasley",
        "species": "human",
        "gender": "male",
    },
    {
        "name": "Draco Malfoy",
        "species": "human",
        "gender": "male",
    }
]    

for character in data_harry:
    print('Name =>', character["name"])

# Ciclos anidados

matriz = [
  [1, 2, 3], 
  [4, 5, 6], 
  [7, 8, 9]
]

# Imprime la primera fila de la matriz
print(matriz[0])

# Imprime el elemento 2 de la primera fila
print(matriz[0][1])

'''
Recorremos las filas (row) de la matriz y por cada fila recorremos cada una de las columnas (column)
'''
for row in matriz:
  print(row)
  for column in row:
    print(column)

# [1, 2, 3]
# 1
# 2
# 3
# [4, 5, 6]
# 4
# 5
# 6
# [7, 8, 9]
# 7
# 8
# 9



    