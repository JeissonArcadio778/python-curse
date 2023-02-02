# Decimal precision

x = 3.3 
print(x)

y = 1.1 + 2.2
print(y)

print(x == y) # Is for rule IEEE-754 2008. Limit of number to represent floats. Se pasan a binarios, se suman, pero en binario tienen infintos decimales. Por eso se trata de aproximar. 

# Hot to compare floats? 

y = round((1.1 + 2.2),1) # round: number of decimals
print(y)
print(x==y)






