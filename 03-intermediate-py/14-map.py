# Map: return a transformation array. 

numbers = [1, 2, 3, 4]
numbers_v2 = []
for i in numbers:
  numbers_v2.append(i * 2)

numbers_v3 = list(map(lambda i: i * 2, numbers))

print(numbers)
print(numbers_v2)
print(numbers_v3)

# [1, 2, 3, 4]
# [2, 4, 6, 8]
# [2, 4, 6, 8]

numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]

print(numbers_1)
print(numbers_2)

# [1, 2, 3, 4]
# [5, 6, 7]

result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result)



