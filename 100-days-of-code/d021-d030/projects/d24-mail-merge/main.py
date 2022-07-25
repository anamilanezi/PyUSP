# Get starting letter text content
with open("./Input/Letters/starting_letter.txt") as letter:
    letter_txt = letter.read()
    print(letter_txt)

# Geting the names from file as a list
with open("./Input/Names/invited_names.txt") as names:

    name_list = names.read().splitlines()
    print(name_list)

# Changing the placeholder on starting letter and saving a file for each name of list
for name in name_list:
    letter = letter_txt.replace("[name]", name)
    file_name = f"./Output/ReadyToSend/letter_for_{name}.txt"
    with open(file_name, mode="w") as file:
        file.write(letter)

