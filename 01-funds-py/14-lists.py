# Lists

# number list 

numbers = [1,2,3,4,5,6,7,8]

print(numbers, type(numbers)) # [1, 2, 3, 4, 5, 6, 7, 8] <class 'list'>

# Things about lists: 

types = ['Make a dishes', 'play videogames', 2000, True]
print(types, type(types))

print(types[0]) #Vector

# Modify in lists

## The Strings are immutables. 

types[0] = 'Watch platzi courses'
print(types, type(types))


# Slicing in lists
print(numbers[2:4])

# Questions:
print(True in types) # True!


# CRUD LISTS - LIST METHODS:

# READ
numbers = [1,2,3,4,5,6]
print(numbers[1])


# CREATED
numbers[-1] = 'Replace last postion'
print("Replace =>", numbers)
# Replace => [1, 2, 3, 4, 5, 'Replace last postion']

numbers.append(700) # Last position

numbers.insert(0,'Hello') # anyone position: 0,1,2,3-- And does not erased the old element

numbers.insert(2,'Change, but not replace')

print(numbers)
# ['Hello', 1, 'Change', 2, 3, 4, 5, 'Replace last postion', 700]

# Add two lists: sum lists

task_uni = ['Read Calculus', 'Do exercises']
task_platzi = ['Practice Python', 'Lear AWS']
tasks_yy = task_uni + task_platzi
print(tasks_yy) # ['Read Calculus', 'Do exercises', 'Practice Python', 'Lear AWS']

# UPDATE

# Ask where is the index

ix = tasks_yy.index('Practice Python')
tasks_yy[ix] = 'Learn and practice python'
print(tasks_yy)

# DELETE

tasks_yy.remove('Do exercises')
print(tasks_yy)

task_platzi.pop() # delete last element

tasks_yy.pop(0) # delete 0 index == position

tasks_yy.reverse() #Reverse lists

# SORT 

sorting_list = [4,2,10,1,0]
sorting_list.sort()
print(sorting_list)

sorting_letters = ['z', 'e', 'a', 'r']
sorting_letters.sort()
print(sorting_letters)
# But is impossible sort list with different type elements

# [0, 1, 2, 4, 10]
# ['a', 'e', 'r', 'z']