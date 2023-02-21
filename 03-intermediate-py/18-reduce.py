# REDUCE: tomar una lista y sacar una sola conclusión de esa lista. EXAMPLE: sacar mayor valor, sumarlos todos. 
import functools

numbers = [1,2,3,4]

def accum(counter, item):
    print("Counter => ", counter)
    print("item => ", item)
    return counter + item

sum_reduce = functools.reduce(accum, numbers)
sum_reduce = functools.reduce(lambda counter, item: counter + item, numbers) 
print(sum_reduce)

"""
Counter =>  1
item =>  2
Counter =>  3
item =>  3
Counter =>  6
item =>  4
10
"""
'''
iteration counter item return
   1         0      1    1
   2         1      2    3
   3         3      3    6
   4         6      4    10
'''

# Example: 


items = [
    {'name':'Mouse',
    'price':100,
    'id': 1},
    {'name':'Teclado',
    'price': 300,
    'id': 2},
    {'name':'Monitor',
    'price':200,
    'id': 3},
    {'name':'Celular',
    'price':150,
    'id':4},
    {'name':'Alcohol',
    'price':475,
    'id': 5},
    {'name':'Control',
    'price': 750,
    'id': 6},
    {'name':'Cuaderno',
    'price':45,
    'id': 7},
    {'name':'Tablero',
    'price':650,
    'id':8}
]  

# Map

list_prices = list(map(lambda item : item['price'], items))
print(list_prices)

sum_prices = functools.reduce(lambda counter, item : counter + item, list_prices)
print(sum_prices)

# [100, 300, 200, 150, 475, 750, 45, 650]
# 2670


