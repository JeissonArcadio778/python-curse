# Una variable solo esta disponible dentro de la región donde fue creada


prince = 100 # global

def scope():
  prince = 200 # funcion
  prince += 10
  return prince


print(prince) # global
prince_2 = scope()
print(prince_2) # funcion