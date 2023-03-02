try: 
    print(0/0)
except ZeroDivisionError as error: 
    print(error)

try: 
    assert 1 != 1, 'One is not equal one'
except AssertionError as error: 
    print(error)
 
print('Normal way')


# Capturar cualquier error: Exception. 
try:
    pass
except Exception as e:
    raise
else:
    pass
finally:
    pass

# .
# El bloque else se ejecuta cuando todo lo del bloque ‘try’ se ejecuta correctamente, es decir, sin excepciones.
# .
# El bloque finally se ejcuta haya o no excepciones en el bloque ‘try’, es decir, que su ejecución es obligatoria