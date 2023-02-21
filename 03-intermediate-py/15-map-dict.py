items = [
    {
        'product': 'shirt',
        'price' : 100
    },
    {
        'product': 't-shirt',
        'price' : 200
    },
    {
        'product': 'jean',
        'price' : 300
    },
]

# Get prices values in list:
price_list = list(map(lambda item : item['price'], items)) 
print(price_list) # [100, 200, 300]

# Agregate a new attribute in the object: 
def add_taxes(item_list):
    item_list['taxes'] = item_list['price'] * .19
    return item_list

new_items = list(map(add_taxes, items))
print(new_items) # [{'product': 'shirt', 'price': 100, 'taxes': 19.0}, {'product': 't-shirt', 'price': 200, 'taxes': 38.0}, {'product': 'jean', 'price': 300, 'taxes': 57.0}]
print(items) # [{'product': 'shirt', 'price': 100, 'taxes': 19.0}, {'product': 't-shirt', 'price': 200, 'taxes': 38.0}, {'product': 'jean', 'price': 300, 'taxes': 57.0}]





