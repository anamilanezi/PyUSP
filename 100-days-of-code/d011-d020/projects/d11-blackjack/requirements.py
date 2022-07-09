from random import choice
from art import *
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

cards_dic = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, }  

def get_random_card():
    return choice(list(cards_dic.keys()))

def start_hand():
    player_hand = []
    while len(player_hand) < 2:
        random_card = get_random_card()
        player_hand.append(random_card)
    return player_hand

def get_score(current_cards):
    score = 0
    for card in current_cards:
        score += cards_dic[card]

    if 'A' in current_cards and score > 21:
        score -= 10

    return score

def add_new_card(current_cards):
    random_card = choice(list(cards_dic.keys()))
    current_cards.append(random_card)
    return current_cards

########
def get_result(player_score, computer_score):

    result = ""
    if player_score > 21:
        print_lines()
        decor_text("You went over.")
        result = lose
    elif player_score <= 21 and computer_score > 21:
        print_lines()
        decor_text("Opponent went over.")
        result = win
    elif player_score > computer_score:
        result = win
    elif player_score == computer_score:
        result = draw
    else:
        result = lose 
    decor_text(result, True)



def wants_to(user_input):
    if (user_input.lower() == 'y'):
        return True
    elif (user_input.lower() == 'n'):
        return False

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def format_list(any_list):
    list_to_str = ' ][ '.join(any_list)
    return list_to_str

def print_lines():
    print(f"{'-':-^62}")

def decor_text(any_string, with_line=False):
    if with_line:
        print_lines()
        print(f"{any_string:^62}")
        print_lines()
    else:
        print(f"{any_string:^62}")

def game_text(player_hand, player_score, computer_first_card):

    text_list = [
        f"Your cards: [ {format_list(player_hand)} ]", 
        f"Current score: {player_score}", 
        f"Computer's first card: {computer_first_card}"
        ]

    print_lines()
    
    for line in text_list:
        decor_text(line)

    print_lines()

def final_text(player_hand, player_score, computer_hand, computer_score):

    text_list = [
        f"Your final hand is [ {format_list(player_hand)} ]", 
        f"Your final score is {player_score}", 
        f"Computer's final hand is [ {format_list(computer_hand)} ]", 
        f"Computer final score is {computer_score}"
        ]
    
    for line in text_list:
        decor_text(line)

    get_result(player_score, computer_score)