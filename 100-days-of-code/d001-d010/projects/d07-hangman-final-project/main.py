import random
import hangman_art
import hangman_words
import os

stages = hangman_art.stages

word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6 

# The next line clears the console
os.system('cls' if os.name == 'nt' else 'clear')

print(hangman_art.logo)
# print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"


while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    # The next line clears the console
    os.system('cls' if os.name == 'nt' else 'clear') 

    if guess in display:
        print(f"You already guessed {guess}")
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
    else:
        print("")

    if "_" not in display:
        print("***You win.***")
    elif lives == 0:
        print(f'You lose. The word is "{chosen_word}".')
    
    print(f"{' '.join(display)}")
    print(stages[lives])