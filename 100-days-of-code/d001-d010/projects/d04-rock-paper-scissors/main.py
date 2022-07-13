import random
import os

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def clear():
    ''''Clear the screen'''
    os.system('cls' if os.name == 'nt' else 'clear')

def play_again():
    '''Asks the user if wants to play again after finishing a game'''
    user_input = input("Do you want to play again? Type 'y' or 'n': "). lower()
    if (user_input.lower() == 'y'):
        return True
    elif (user_input.lower() == 'n'):
        return False

def start_game():
    clear()
    player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    drawings = [rock, paper, scissors]

    if (player_choice >= 3) or (player_choice < 0):
        print("You typed an invalid number, you lose!")
    else:
        print(drawings[player_choice])

        computer_choice = random.randint(0,2)
        print("Computer chose:")
        print(drawings[computer_choice])

        # Rock wins against scissors        (0 wins 2)
        # Scissors wins against paper       (2 wins 1)
        # Paper wins against rock           (1 wins 0)

        if (player_choice == 0 and computer_choice == 2) or (player_choice == 2 and computer_choice == 1) or (player_choice == 1 and computer_choice == 0):
            print("You win!\n")

        if (player_choice == 2 and computer_choice == 0) or (player_choice == 1 and computer_choice == 2) or (player_choice == 0 and computer_choice == 1):
            print("You lose.\n")

        if (player_choice == computer_choice):
            print("That's a draw.\n")
        
        if play_again():
            clear()
            start_game()
        else:
            print("Thank you for playing Rock Paper Scissors :)")
            quit()

start_game()