# Errors: 

print('Normal way')

sum_ = lambda x,y : x + y

# its a basic validation: 
# assert sum_(2,2) == 5 # ERROR!

print('Final way')

age = 17

if age < 18 : 
    raise Exception('Age Minors, cant enter')

