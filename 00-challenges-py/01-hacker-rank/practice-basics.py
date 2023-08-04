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

# Ejercicio 4: Conversor de Temperatura
# Convierte grados Celsius a Fahrenheit y viceversa. Pide al usuario que ingrese una temperatura y si quiere convertirla a Celsius o Fahrenheit.

# Ejercicio 5: Número Par o Impar
# Pide al usuario un número e indica si es par o impar.

# Ejercicio 6: Mayor de Tres Números
# Pide al usuario tres números y encuentra el mayor de los tres.

# Ejercicio 7: Calificación de Examen
# Pide al usuario su calificación en un examen (0-100) y asigna una letra correspondiente (A, B, C, etc.) según la calificación.

# Ejercicio 8: Lista de Compras
# Permite al usuario ingresar varios elementos en una lista de compras y luego imprime toda la lista.

# Ejercicio 9: Contador de Vocales y Consonantes
# Pide al usuario que ingrese una cadena y cuenta el número de vocales y consonantes en ella.

# Ejercicio 10: Calculadora de Promedio
# Pide al usuario que ingrese una serie de números (podría ser calificaciones, por ejemplo) y luego calcula e imprime el promedio.
