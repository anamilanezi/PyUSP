import pandas

dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary from CSV File
nato_dict = {row.letter: row.code for (index, row) in dataframe.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.

# invalid_word = True
#
# while invalid_word:
#     word = input("Enter a word: ").upper()
#     try:
#         nato_word_list = [nato_dict[letter] for letter in word]
#     except KeyError:
#         print("Sorry, only letter in the alphabet plase.")
#     else:
#         print(nato_word_list)
#         invalid_word = False


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        nato_word_list = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letter in the alphabet plase.")
        generate_phonetic()
    else:
        print(nato_word_list)


generate_phonetic()

