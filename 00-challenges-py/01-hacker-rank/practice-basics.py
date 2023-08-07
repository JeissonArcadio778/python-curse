# Ejercicio 1: Saludo Personalizado
# Pide al usuario su nombre y luego salúdalo imprimiendo "¡Hola, [nombre]!".

def sayHello( user_name:str ) -> str:
    return f"Hello {user_name}!"
result: str = sayHello("Yeye")
print(result)

# Ejercicio 2: Suma de Dos Números
# Pide al usuario dos números y muestra la suma de ambos.
def sum_numbers ( num_a: int, num_b: int ) -> int:
    return num_a + num_b
result: int = sum_numbers(1,2)
print(result)

# Ejercicio 3: Calculadora de Área de un Círculo
# Pide al usuario el radio de un círculo y calcula su área utilizando la fórmula A = π * r^2.

import math

def calculate_circle_are (r:float) -> float:
    return math.pi * (r ** 2) 

result: float = calculate_circle_are(3.6)
print(result)

# TODO: Ejercicio 4: Conversor de Temperatura
# Convierte grados Celsius a Fahrenheit y viceversa. Pide al usuario que ingrese una temperatura y si quiere convertirla a Celsius o Fahrenheit.

# Ejercicio 5: Número Par o Impar
# Pide al usuario un número e indica si es par o impar.

def isOdd (number: int) -> bool:
    if (number == 0):
        return False
    elif (number % 2 == 0):
        return True
    else:
        return False

user_number = int(input("Write a number: "))
print(f"Number {user_number} is {isOdd(user_number)}")

# Ejercicio 6: Mayor de Tres Números
# Pide al usuario tres números y encuentra el mayor de los tres.

def max_number(numbers: [int]):
    max_number = 0
    for number in numbers: 
        if number > max_number: 
            max_number = number
    return max_number
print(f"Max Number {max_number([10,5,1])}")

# Min Number:
def min_number(numbers: [int]) -> list:
    min_number = 100
    for number in numbers:
        if number < min_number:
            min_number = number
    return min_number
print(f"Min Number {min_number([10,5,1])}")

# Ejercicio 7: Calificación de Examen
# Pide al usuario su calificación en un examen (0-100) y asigna una letra correspondiente (A, B, C, etc.) según la calificación.

def notes(note: int) -> str:
    if (note > 80):
        return "E"
    elif (note < 80 and note > 60):
        return "S"
    
print(notes(70))

# Ejercicio 8: Lista de Compras
# Permite al usuario ingresar varios elementos en una lista de compras y luego imprime toda la lista.

def show_items_in_list (items: list):
    for item in items:
        print(item)
show_items_in_list(['Water', 'Eggs', 'Rice'])

# Ejercicio 9: Contador de Vocales y Consonantes
# Pide al usuario que ingrese una cadena y cuenta el número de vocales y consonantes en ella.

import re

def count_vocals_consonants (word: str) -> int:
    word = word.lower()

    patter_vocals = r'[aeiou]'
    patter_consonants = r'[bcdfghjklmnpqrstvwxyz]'

    count_vocals = len(re.findall(patter_consonants, word))
    count_consonants = len(re.findall(patter_consonants, word))

    return count_vocals, count_consonants


number_vocals, number_consonants = count_vocals_consonants('CASA')

print(f"Vocals {number_vocals}. Consonants {number_consonants}")

# Ejercicio 10: Calculadora de Promedio
# Pide al usuario que ingrese una serie de números (podría ser calificaciones, por ejemplo) y luego calcula e imprime el promedio.

def averague_notes (notes: list) -> int:
    sum_notes = 0
    for note in notes: 
        sum_notes += note     
    return sum_notes/len(notes)

print(averague_notes([3,3,3]))

# PRACTICTE COMPREHENSIONS:

# Ejercicios con List Comprehensions:

# 1. Generar una lista con los cuadrados de los primeros 10 números naturales.

numbers = [number for number in range(1,11)]
print(numbers)
numbers_sqrt = [number ** 2 for number in numbers]
print(numbers_sqrt) 
# Better way
squares = [x** 2 for x in range(1,11)]

# 2. Filtrar los números pares de una lista dada.

numbers = [number for number in range(1,11)]
odd_numbers = [number for number in numbers if number % 2 == 0]
print(odd_numbers)

# 3. Convertir una lista de cadenas a una lista de sus respectivas longitudes.
string_list = ['Loquita', 'Yeye', 'Maria', 'Julio', 'Valen', 'Pulga']
count_string_list = [len(string) for string in string_list]
print(count_string_list)

# 4. Obtener una lista de las vocales presentes en una cadena de texto.
full_name = 'Sara Isabel Gomez Jaramillo'
vocals = 'aeiou'
vocals_in_full_name = [ vocal for vocal in full_name.lower() if vocal.lower() in vocals]
print(vocals_in_full_name)

# 5. Generar una lista de las potencias de 2 hasta el exponente 10.
potences = [2 * exponent for exponent in range(1, 11)]
print(potences)

# Ejercicios con Dict Comprehensions:

# 6. Crear un diccionario con los cuadrados de los primeros 5 números naturales como claves y sus respectivos valores originales.

# 7. Convertir una lista de palabras en un diccionario donde las claves son las palabras y los valores son sus longitudes.


# 8. Obtener un diccionario con las letras de una cadena de texto y su frecuencia en la cadena.

# 9. Crear un diccionario con los primeros 5 números naturales como claves y sus raíces cuadradas como valores.

# 10. Generar un diccionario con los caracteres de una cadena de texto como claves y el número de veces que aparecen como valores.