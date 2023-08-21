# Normal Function
def sum_function(a, b):
    print(a + b)


sum_function(2, 3)  # 5


# Function with RETURN

def return_sum(a, b):
    return a + b


print(return_sum(2, 6))  # 8


## Ex: sum numbers from min to max
def sum_numbers(min, max):
    sum_values = 0

    for i in range(min, max):
        sum_values += i
        # print(sum_values)

    return sum_values


print(sum_numbers(10, 12))


# DEFAULT ARGS AND MULTIPLE RETURNS

def find_volume(length=2, width=2, depth=1):
    return length * width * depth, width, 'This Was A Simple Calculate'
    # return [length * width * depth, width, 'hola'] for return like a list


result = find_volume(20, 10, 11)
print(result)  # tuple: (2200, 10, 'This Was A Simple Calculate')

result, width, string = find_volume(30, 10)
print(result, width, string)  # 2200, 10, 'This Was A Simple Calculate'

result = find_volume(20, 10, 11)
print(result[0])  # 2200
