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
# r+ read and write (but not rewrite)
# w+ read and write (rewrite)
with open('./text.txt', 'r+') as file: 
    for line in file: 
        print(line)
    file.write('New line wrote \n')
    file.write('New line wrote \n')

    

# They close automatically


