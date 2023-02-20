def increment(x):
    return x + 1

print(increment(10))

# lambda == anonima

increment_v2 = lambda x : x + 1 
print(increment_v2(20))

# Ex

full_name = lambda name, last_name : f"Your full name is {name.title()} {last_name.title()}"

print(full_name('Yeye', 'Beltran'))