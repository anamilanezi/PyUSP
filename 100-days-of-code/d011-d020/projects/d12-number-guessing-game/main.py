import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

random_number = random.randint(1,100)
print(random_number)

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5

guessed_the_number = False

while not guessed_the_number:
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        if guess < random_number:
            print("Too low.\nGuess again.")
            attempts -= 1
        elif guess > random_number:
            print("Too high.\nGuess again.")
            attempts -= 1
        elif guess == random_number:
            guessed_the_number = True
            print(f"You got it. The answer was {random_number}")
            break
    if attempts == 0:
        print(f"You have no attempts left. The answer was {random_number}.")
        break