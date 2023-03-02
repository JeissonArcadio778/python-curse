for i in range(1,11):
    print(i)

my_range = iter(range(1,4))

print(next(my_range))
print(next(my_range))
print(next(my_range)) # 3
print(next(my_range)) # StopIteration
