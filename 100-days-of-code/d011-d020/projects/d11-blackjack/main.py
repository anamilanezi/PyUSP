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

# Do you want to play a game of BlackJack? Type 'y' or 'n': 
# Your cards: [ , ], current score: 
# Computer's first card:
# Type 'y' to get another card, type 'n' to pass

from random import choice

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

cards_dic = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, }  



# random_card = choice(list(cards_dic.keys()))
# print(random_card)
# print(cards_dic[random_card])

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

def format_list(any_list):
    list_to_str = ' ][ '.join(any_list)
    return list_to_str

def get_result(player_score, computer_score):
    if player_score > 21:
        print("You went over. You lose.")
    elif player_score <= 21 and computer_score > 21:
        print("Opponent went over. You win! :)")
    elif player_score > computer_score:
        print("You win")
    else: 
        print("You lose")

def game_text(player_hand, player_score, computer_first_card):
    print(f"Your cards: [ {format_list(player_hand)} ], current score: {player_score}")
    print(f"Computer's first card: {computer_first_card}")


def final_text(player_hand, player_score, computer_hand, computer_score):
    print(f"Your final hand is [ {format_list(player_hand)} ], final score: {player_score}")
    print(f"Computer's final hand is [ {format_list(computer_hand)} ], final score: {computer_score} ")
    get_result(player_score, computer_score)


player_hand = start_hand()
player_score = get_score(player_hand)
computer_hand = start_hand()
computer_score = get_score(computer_hand)
computer_first_card = computer_hand[0]

game_text(player_hand, player_score, computer_first_card)

if player_score == 21:
    print("BLACKJACK! You win.")

while player_score < 21:
    get_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    if get_another_card == 'y':
        player_hand = add_new_card(player_hand)
        player_score = get_score(player_hand)
    game_text(player_hand, player_score, computer_first_card)

    if get_another_card == 'n':
        break

while computer_score < 17:
    computer_hand = add_new_card(computer_hand)
    computer_score = get_score(computer_hand)


final_text(player_hand, player_score, computer_hand, computer_score)