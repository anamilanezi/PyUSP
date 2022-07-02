import random

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
        print("You win!")

    if (player_choice == 2 and computer_choice == 0) or (player_choice == 1 and computer_choice == 2) or (player_choice == 0 and computer_choice == 1):
        print("You lose.")

    if (player_choice == computer_choice):
        print("That's a draw.")