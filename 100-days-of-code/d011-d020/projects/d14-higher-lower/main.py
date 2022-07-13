from random import choice, sample
from game_data import *
import art
import os

def clear():
    ''''Clear the screen'''
    os.system('cls' if os.name == 'nt' else 'clear')


def print_lines():
    '''Prints a line of hifen for decoration'''
    print(f"{'-':-^60}")

def play_again():
    '''Asks the user if wants to play again after finishing a game'''
    user_input = input("   Do you want to play again? Type 'y' or 'n': "). lower()
    if (user_input.lower() == 'y'):
        return True
    elif (user_input.lower() == 'n'):
        return False

# Determine which of them has more followers:
def higher(list):
    '''Takes the list of current itens in game and return the higher num of followers'''
    max_followers = 0
    for item in list:
        if item['follower_count'] > max_followers:
            max_followers = item['follower_count']
    return max_followers

def item_text(item):
    '''Generates the text for each item.'''
    description = item['description']
    if description[0].lower == 'a':
        article = 'An'
    else:
        article = 'A'
    text = f"{item['name']}.\n   {article} {item['description']}, from {item['country']}."
    return text

def print_text(list):
    '''Generate the game text with current itens for comparison'''
    print_lines()
    print(f"   Compare A: {item_text(list[0])}")
    print(art.vs)
    print(f"   Against B: {item_text(list[1])}")
    print_lines()

def user_answer():
    '''Asks for user which option has more followers and returns an index'''
    answer = input("   Who has more followers? Type 'A' or 'B': ").lower()
    if answer == 'a':
        return 0
    elif answer == 'b':
        return 1
    else: 
        print("   That's not a valid answer. Try again.")
        return user_answer()

def check_answer(max_followers, list):
    '''Takes the higher number of followers, the current list of itens, checks user answer and check if it is correct.'''
    i = user_answer()
    if list[i]['follower_count'] == max_followers:
        return True
    else:
        return False

def update_list(game_list, data):
    '''Removes option A (which turns option B into option A), gets a new item from data, checks if it is on current list, if not on list and adds new random item into option B'''
    del game_list[0]
    new_item = choice(data)
    while new_item in game_list:
        new_item = choice(data)
    game_list.append(new_item)
    return game_list


def start_game():
    score = 0
    ab_list = sample(data, 2)
    max_followers = higher(ab_list)

    clear()
    print(art.logo)

    print_text(ab_list)

    while check_answer(max_followers, ab_list):
        score += 1
        if score > 0:
            clear()
            print(art.logo)
            
            print(f"   You're right! CURRENT SCORE: [{score}].")
        a = ab_list[0]
        b = ab_list[1]

        ab_list = update_list(ab_list, data)
        max_followers = higher(ab_list)
        print_text(ab_list)
    
    print_lines()
    print(f"   Sorry, that's wrong. Final score: {score}.")

    if play_again():
        clear()
        start_game()
    else:
        print("   Thank you for playing the Higher Lower game! :)")
        quit()

start_game()


