file = open("./text.txt")

print(file.read())

print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

for line in file: 
    print(line)

file.close() # Its for clone the file.

with open('./text.txt') as file: 
    for line in file: 
        print(line)

# They close automatically