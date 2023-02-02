import random

options = ('rock', 'paper','scissors')

user_option = input('rock, paper, scissors: ')
user_option = user_option.lower()

if not user_option in options: 
    print('its not a correct choice')

computer_option = random.choice(options)

print('User option => ', user_option)
print('Computer option => ', computer_option)


if user_option == computer_option: 
    print('Tid')
elif user_option == 'paper':
    if computer_option == 'scissors':
        print('Computer Wins')
    else:
        print('User Wins')
elif user_option == 'rock':
    if computer_option == 'paper':
        print('Computer Wins')
    else:
        print('User Wins')
else: 
    if computer_option == 'rock':
        print('Computer Wins')
    else:
        print('User Wins')