import pandas

dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary from CSV File
nato_dict = {row.letter: row.code for (index, row) in dataframe.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()

nato_word_list = [nato_dict[letter] for letter in word]

print(nato_word_list)
