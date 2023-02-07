#  UNION 

set_a = {'col', 'bol', 'arg'}
set_b = {'col', 'mx', 'pe'}

set_c = set_a.union(set_b)
print(set_c)
# same : 
print (set_a | set_b) # {'arg', 'mx', 'pe', 'col', 'bol'}

# INTERSECTION 

set_c = set_a.intersection(set_b)
print(set_c) # {'col'}


# DIFFERENCE: the second subtract to first
set_c = set_a.difference(set_b)
print(set_a - set_b)
#Same
print(set_c) # {'bol', 'arg'}

# Symmetric Difference: leave the repeated elements 
set_c = set_a.symmetric_difference(set_b)
print(set_c) # {'arg', 'bol', 'pe', 'mx'}







