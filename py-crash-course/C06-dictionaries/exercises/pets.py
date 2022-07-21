
# 6.8

pets = []

pet = {
    'name': 'lionel',
    'type': 'dog',
    'owner': 'ricardo luan',
    'breed': 'ibiraquera terrier',
}
pets.append(pet)

pet = {
    'name': 'muffin',
    'type': 'dog',
    'owner': 'ana carolina',
    'breed': 'lhasa apso',
}
pets.append(pet)

pet = {
    'name': 'leslie',
    'type': 'cat',
    'owner': 'maria conceição',
    'breed': 'calico',
}
pets.append(pet)

pet = {
    'name': 'kátia',
    'type': 'cat',
    'owner': 'lorena',
    'breed': 'frajola',
}
pets.append(pet)

for pet in pets:
    name = pet['name'].title()
    owner = pet['owner'].title()
    breed = pet['breed'].title()
    print(f"{name} is a {pet['type']} owned by {owner}. Its breed is {breed}.")  # Mesmo output que abaixo, mais simples

    print(
        f"{pet['name'].title()} is a {pet['type']} owned by {pet['owner'].title()}. Its breed is {pet['breed'].title()}.")

# Resolução do livro:

# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        if type(value) == str:  # Minha contribuição, para deixar bonito
            value = value.title()
        print(f"\t{key}: {value}")


# 6.9 Favorite Places


