#  STRINGS

name = 'Jeisson'
last_name = 'Beltran'
print(name, last_name)

# FullName
full_name = name + ' ' + last_name
print(full_name)

# How to use apostrophe
quote = "I'm Yeye"
print(quote)

quote2 = "And she said: 'Helloo World'";
print(quote2)

# Format:

template = "Hello, my name is {} and my last name is {}".format(name, last_name)
print(template)

name = "Sarita"
last_name= "Gomez"
age = 20
my_city = "Bellokistan"

impresion = f"Hola {name} {last_name}, tu edad es {age} y vivo en {my_city}"

print(impresion); 


# Some methods: 

text = 'Python is my priority'

if 'JS' in text:
    print('TRUE', True)
else: 
    print('FALSE',False)

# Size: 

size = len(text)
print(size)

# Transformations: 

print(text)
print(text.upper())
print(text.lower())

print(text.count('i'))

print(text.swapcase()) # Past lower to Upper and Upper to lower.

if text.startswith('Python'): # .endswith()
    print(True)
else: 
    print(False)

print(text.replace('Python', 'Go'))

text_2 = 'This is a title'

print(text_2.capitalize())
print(text_2.title()) # This Is A Title

print(text_2.isdigit()) # False
print("323".isdigit()) # True
