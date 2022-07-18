# 6.1 Person

luan = {
	'first_name' : 'ricardo luan', 
	'last_name': 'modesto de assis', 
	'age': 29, 
	'city': 'nova veneza'
	}

print(luan['first_name'].title())
print(luan['last_name'].title())
print(luan['age'])
print(luan['city'].title())

## Pode associar o valor a um objeto:
full_name = f"{luan['first_name'].title()} {luan['last_name'].title()}"
print(full_name)


# 6.2 Favorite numbers

favorite_numbers = {
	'gi': 13, 
	'maria': 19, 
	'rodeval': 71, 
	'luan': 88, 
	'lorena': 7, 
	'ana': 13
	}

number = favorite_numbers['gi']
print(f"Gi's favorite number is {number}.")

number = favorite_numbers['maria']
print(f"Maria's favorite number is {number}.")

number = favorite_numbers['rodeval']
print(f"Rodeval's favorite number is {number}.")

number = favorite_numbers['luan']
print(f"Luan's favorite number is {number}.")

number = favorite_numbers['lorena']
print(f"Lorena's favorite number is {number}.")

number = favorite_numbers['ana']
print(f"Ana's favorite number is {number}.")

# 6.3 Glossary

glossary = {
	'list': 'Lists are used to store multiple items in a single variable.',
	'tuple': 'A tuple is a collection which is ordered and unchangeable.',
	'dictionary': 'Dictionaries are used to store data values in key:value' 
	' pairs.',
	'if_elif_else': 'Allows to perform actions based on conditions.',
	'for_loop': 'A for loop is used for iterating over a sequence (that is eit'
	'her a list, a tuple, a dictionary, a set, or a string).',
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    }

# Sugestão de resolução do livro

word = 'string'
print(f"\n{word.title()}: {glossary[word]}")

word = 'comment'
print(f"\n{word.title()}: {glossary[word]}")

# Minha resolução 

meaning = glossary['list']
print(f"List: {meaning}")

meaning = glossary['tuple']
print(f"Tuple: {meaning}")

meaning = glossary['dictionary']
print(f"Dictionary: {meaning}")

meaning = glossary['if_elif_else']
print(f"If-elif-else: {meaning}")

meaning = glossary['for_loop']
print(f"For loop: {meaning}")

# 6.4

glossary = {
	'list': 'Lists are used to store multiple items in a single variable.',
	'tuple': 'A tuple is a collection which is ordered and unchangeable.',
	'dictionary': 'Dictionaries are used to store data values in key:value' 
	' pairs.',
	'if_elif_else': 'Allows to perform actions based on conditions.',
	'for_loop': 'A for loop is used for iterating over a sequence (that is eit'
	'her a list, a tuple, a dictionary, a set, or a string).',
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'set' : 'is a collection which is unordered, unchangeable, and unindexed.'
    ' No duplicate members.',
    'boolean': 'Booleans represent one of two values: True or False.',
    'variable': 'Variables are containers for storing data values.',
    'operators': 'Operators are used to perform operations on variables and v'
    'alues.'
    }

print("Here is the python glossary I've made so far:")

for word, meaning in sorted(glossary.items()):
	print(f"\n{word.title()}:")
	print(meaning)

# 6.5

rivers = {
	'nile': 'egypt',
	'amazon': 'brazil',
	'parana': 'brazil',
	'paraguai': 'paraguai',
	'seine': 'france',
	'mississipi': 'united states',
	'river plate': 'argentina',
	}

for name, country in sorted(rivers.items()):
	print(f"The {name.title()} runs through {country.title()}.")

print("\n\tHere are all the rivers recorded:")
for name in sorted(rivers):
	print(name.title())

print("\n\tHere are all the countries recorded:")
for country in set(sorted(rivers.values())):
	print(country.title())

# 6.6

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

coders = ['maria', 'giovana', 'phil', 'jen']

for coder in sorted(coders):
	if coder not in favorite_languages.keys():
		print(f"{coder.title()}, please take our poll!")
	else:
		print(f"{coder.title()}, thank you for taking our poll!")

# 6.7 REVISAR!!

people = []				# Começa com uma lista vazia

person = {				# Cria o dicionário de uma pessoa
	'first_name' : 'ricardo luan', 
	'last_name': 'modesto de assis', 
	'age': 29, 
	'city': 'salvador'
	}
people.append(person)	# Adiciona à lista

person = {
	'first_name' : 'giovana', 
	'last_name': 'medeiros milanezi', 
	'age': 34, 
	'city': 'criciúma'
	}
people.append(person)

person = {
	'first_name' : 'ana carolina', 
	'last_name': 'medeiros milanezi', 
	'age': 31, 
	'city': 'nova veneza'
	}
people.append(person)

person = {
	'first_name' : 'paula', 
	'last_name': 'martinelli vieira da rosa', 
	'age': 36, 
	'city': 'florianópolis'
	}
people.append(person)

for person in people:
	full_name = f"{person['first_name'].title()} {person['last_name'].title()}"
	city = person['city'].title()
	print(f"\nFull name: {full_name} \n\tCity: {city}\n\tAge: {person['age']}.")

# Lista contendo dicionário: como todos os elementos da lista recebem o mesmo nome, para chamar, não precisa especificar, só percorrer a lista
# pedindo pelos valores utilizando sempre o mesmo nome que foi atribuído (no caso, person)

# Minha resolução inicialmente tinha uma lista [ana, luan, ...] após "for person in people"
# for key, information in person.items(): 
# ESSA LINHA QUE EU INSERI NÃO É NECESSÁRIA, por percorria e imprimia os valores 4x

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
	print(f"{name} is a {pet['type']} owned by {owner}. Its breed is {breed}.") # Mesmo output que abaixo, mais simples

	print(f"{pet['name'].title()} is a {pet['type']} owned by {pet['owner'].title()}. Its breed is {pet['breed'].title()}.")

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
        if type(value) == str:			# Minha contribuição, para deixar bonito
        	value = value.title()
        print(f"\t{key}: {value}")