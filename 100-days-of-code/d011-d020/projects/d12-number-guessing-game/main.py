import random
from art import logo
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_again():
    user_input = input("Do you want to play again? Type 'y' or 'n': "). lower()
    if (user_input.lower() == 'y'):
        return True
    elif (user_input.lower() == 'n'):
        return False

def choose_difficulty():
    '''Ask the user which difficulty and return the total attempts.'''
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if difficulty == 'easy':
        attempts = 10
    elif difficulty == 'hard':
        attempts = 5
    return attempts

def print_lines():
    print(f"{'-':-^55}")

def game_play(guessed, attempts_remaining, random_number):
    '''Takes a boolean, number of remaining attempts and the random number, asks for user
    to guess until finds the right answer or there's no more attempts'''
    while not guessed:

        while attempts_remaining > 0:
            print_lines()
            print(f"You have {attempts_remaining} attempts remaining to guess the number.")
            
            guess = int(input("Make a guess: "))

            if guess < random_number:
                print("Too low.\nGuess again.")
                attempts_remaining -= 1
            elif guess > random_number:
                print("Too high.\nGuess again.")
                attempts_remaining -= 1
            elif guess == random_number:
                guessed = True
                print(f"YOU GOT IT! The answer was {random_number}.")
                break
        if attempts_remaining == 0:
            print(f"You have no attempts left. The answer was {random_number}.")
            break

def start_game():
    
    print(logo)
    print_lines()
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

    random_number = random.randint(1,100)
    # print(f"Pssst here's the answer: {random_number}")

    guessed_the_number = False
    attempts_remaining = choose_difficulty()

    game_play(guessed_the_number, attempts_remaining, random_number)    

    print_lines()

    if play_again():
        clear()
        start_game()
    else:
        print("Thank you for playing the game! :)")
        quit()

start_game()

