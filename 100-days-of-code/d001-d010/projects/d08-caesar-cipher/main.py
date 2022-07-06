import art

print(art.lines)
print(art.logo)
print(art.lines)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

end_game = False

def caesar(text_input, shift_amount, cipher_direction):
    final_msg = ""
    
    for char in text_input:
        if char not in alphabet:
            new_char = char
        else:
            char_index = alphabet.index(char)
            if (cipher_direction == 'encode'):
                new_char_index = char_index + shift_amount
            elif (cipher_direction == 'decode'):
                new_char_index = char_index - shift_amount
            new_char = alphabet[new_char_index]
        final_msg += new_char

    print(f'The {cipher_direction}d text is "{final_msg.capitalize()}"')

while not end_game:
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26    # Prevent bugs from shifts greater than expected

    caesar(text,shift,direction)
    
    play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if play_again.lower() == "no":
        end_game = True
        print("Good bye!")

