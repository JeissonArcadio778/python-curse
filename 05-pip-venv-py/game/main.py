# Functions:

def choose_option():
    options = ('rock', 'paper','scissors')
    user_option = input('rock, paper, scissors: ')
    user_option = user_option.lower()

    while not user_option in options:
        user_option = input('Again: rock, paper, scissors: ')
        user_option = user_option.lower()

    computer_option = random.choice(options)

    print('User option => ', user_option)
    print('Computer option => ', computer_option)

    return user_option, computer_option

def check_rules(user_option, computer_option, user_points, computer_points):

    if user_option == computer_option:
        print('Tid')
    elif user_option == 'paper':
        if computer_option == 'scissors':
            print('Computer point')
            computer_points += 1
        else:
            print('User point')
            user_points += 1
    elif user_option == 'rock':
        if computer_option == 'paper':
            print('Computer point')
            computer_points += 1
        else:
            print('User point')
            user_points += 1
    else:
        if computer_option == 'rock':
            print('Computer point')
            computer_points += 1
        else:
            print('User point')
            user_points += 1

    return user_points, computer_points

def finish_game(user_points, computer_points):
        if computer_points == 2:
            print('Computer wins')
            exit()
        if user_points == 2:
            print('User wins')
            exit()

import random

def run_game():

    computer_points = 0
    user_points = 0
    rounds = 1

    while True:

        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)

        user_option, computer_option = choose_option()

        user_points, computer_points = check_rules(user_option, computer_option, user_points, computer_points)

        finish_game(user_points, computer_points)

        rounds += 1

run_game()