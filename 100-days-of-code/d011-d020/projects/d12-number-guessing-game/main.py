import random
from art import logo
import os

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def clear():
    '''Clears the console'''
    os.system('cls' if os.name == 'nt' else 'clear')

def play_again():
    '''Asks the user if wants to play again after finishing a game'''
    user_input = input("Do you want to play again? Type 'y' or 'n': "). lower()
    if (user_input.lower() == 'y'):
        return True
    elif (user_input.lower() == 'n'):
        return False

def choose_difficulty():
    '''Ask the user which difficulty and return the total attempts.'''
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == 'easy':
        attempts = EASY_LEVEL_TURNS
    elif difficulty == 'hard':
        attempts = HARD_LEVEL_TURNS
    else:
        print("Sorry, that's not a valid answer. Please try again.")
        return choose_difficulty()
    return attempts

def print_lines():
    '''Prints a line of hifen for decoration'''
    print(f"{'-':-^50}")

def check_answer(attempts_remaining, guess, random_number):
    '''Compares the user answer with the right number, gives a hint and update the number of turns'''
    print_lines()
    if guess < random_number:
        print("Too low.\nGuess again.")
        turns = attempts_remaining - 1
        return turns
    elif guess > random_number:
        print("Too high.\nGuess again.")
        turns = attempts_remaining - 1
        return turns

def start_game():
    '''Starts the guessing number game'''
    print_lines()
    print(logo)
    print_lines()
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    print_lines()

    random_number = random.randint(1,100)
    attempts_remaining = choose_difficulty()
    guess = 0
    
    print_lines()    
    # print(f"Pssst here's the answer: {random_number}")
    
    while guess != random_number and attempts_remaining > 0:
        print(f"You have {attempts_remaining} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        attempts_remaining = check_answer(attempts_remaining, guess, random_number) 
        print_lines() 
    
    if attempts_remaining == 0:
        print_lines()
        print(f"You have no attempts left. The answer was {random_number}.")
        print_lines()

    if guess == random_number:
        print(f"YOU GOT IT!!! The answer was {random_number}.")
        print_lines()

    if play_again():
        clear()
        start_game()
    else:
        print("Thank you for playing the game! :)")
        quit()

start_game()

