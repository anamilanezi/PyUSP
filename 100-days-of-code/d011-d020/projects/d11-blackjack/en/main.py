############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import *
from requirements import *
from random import choice
import os

def start_game():
    play = input("Do you want to play a game of BlackJack? Type 'y' or 'n': ")

    if wants_to(play):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(logo)
        player_hand = start_hand()
        player_score = get_score(player_hand)
        computer_hand = start_hand()
        computer_score = get_score(computer_hand)
        computer_first_card = computer_hand[0]

        game_text(player_hand, player_score, computer_first_card)

        if player_score == 21:
            decor_text("BLACKJACK!")
            decor_text(win, True)
            start_game()

        while player_score < 21:
            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

            if wants_to(get_another_card):
                print_lines()
                player_hand = add_new_card(player_hand)
                player_score = get_score(player_hand)
                game_text(player_hand, player_score, computer_first_card)

            if not wants_to(get_another_card):
                print_lines()
                break

        while computer_score < 17: 
            computer_hand = add_new_card(computer_hand) 
            computer_score = get_score(computer_hand)   

        
        final_text(player_hand, player_score, computer_hand, computer_score)
        start_game()

    else: 
        quit()

clear()
decor_text(welcome, True)
start_game()