# All texts has index

text = 'Python is my priority'
print(text[0]) # P
# print(text[999]) #Error

ix = len(text) - 1   
print(text[ix])
print(text[len(text) - 1])

# Last indexs : 

print(text[-1]) # y

# Slicing from:to
print(text[6:10]) # is
print(text[0:5]) # Pytho
print(text[:5]) # Pytho

# n is my priorit
print(text[5:-1]) 
# n is my priority
print(text[5:])
