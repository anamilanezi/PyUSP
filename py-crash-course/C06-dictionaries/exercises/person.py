# 6.1 Person

luan = {
    'first_name': 'ricardo luan',
    'last_name': 'modesto de assis',
    'age': 29,
    'city': 'nova veneza'
}

print(luan['first_name'].title())
print(luan['last_name'].title())
print(luan['age'])
print(luan['city'].title())

full_name = f"{luan['first_name'].title()} {luan['last_name'].title()}"
print(full_name)

# 6.7 REVISAR!!

people = []  # Começa com uma lista vazia

person = {  # Cria o dicionário de uma pessoa
    'first_name': 'ricardo luan',
    'last_name': 'modesto de assis',
    'age': 29,
    'city': 'salvador'
}
people.append(person)  # Adiciona à lista

person = {
    'first_name': 'giovana',
    'last_name': 'medeiros milanezi',
    'age': 34,
    'city': 'criciúma'
}
people.append(person)

person = {
    'first_name': 'ana carolina',
    'last_name': 'medeiros milanezi',
    'age': 31,
    'city': 'nova veneza'
}
people.append(person)

person = {
    'first_name': 'paula',
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
