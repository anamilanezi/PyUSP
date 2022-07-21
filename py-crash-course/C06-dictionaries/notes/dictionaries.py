# Dicionários permitem armazenar informações relacionadas
# São constituidos de um par key:value e cridos usando {}

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])     # Imprime o valor associado a color = green
print(alien_0['points'])    # Imprime o valor associado a points = 5

# Acessar os valores em um dicionário

alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print(f"You just earned {new_points}!")

# Adicionar novos valores ao dicionário:

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Iniciar um dicionário vazio

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5

# Alterando valores de um dicionário

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is {alien_0['color']}.")

# Exemplo mais complexo de modificação dependente

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Mover o alien para a direita
# Determine a distância que o alien será movido na velocidade atual

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2 
else:
    # This must be a fast alien
    x_increment = 3

# A nova posição é a soma do incremento com a posição inicial
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# Remover pares key-value:

# del alien_0['points']            # Especificar a chave vai deletar o par

# Dicionário de objetos similares

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# Usar .get() para acessar valores através de chaves que podem não estar no dic.

alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])         # Resulta em um KeyError feia

point_value  = alien_0.get('points', 'No point value assigned')
print(point_value)   

### PERCORRER O DICIONÁRIO USANDO FOR LOOPS

# Percorrer todos os pares key:value -> 
# for key, value in nome_dicionario.itens():

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }            

for key, value in user_0.items():
    print(f"\nThis is the key: {key}.")
    print(f"This is the value: {value}.")

for key, value in user_0.items():
    print(f"\n{key}: {value.title()}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Percorrer somente pelas keys - comportamento padrão!
# for value in nome_dicionario.keys():

for name in favorite_languages.keys():
    print(name.title())

for name in favorite_languages:            # Omitir .keys() tem mesmo efeito em for/in,
    print(name.title())                    # visto que é o padrão da loop em dicionário

# É possível acessar o valor associado a qualquer chave dentro da loop utilizan-
# do a key atual (da loop):

friends = ['phil', 'sarah']                # Cria uma lista de chaves de interesse

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:                                        # Se a chave estiver na lista de interesse
        language = favorite_languages[name].title()            # Método da [] para acessar o valor usando a key que agora é name
        print(f"\t{name.title()}, I see you love {language}!") # Imprime a msg para aqueles que estão na lista

if 'erin' not in favorite_languages.keys():                    # Verifica se um valor NÃO ESTÁ no dicionário   
    print("Erin, please take our poll!")

# Looping através de keys de forma ordenada

for name in sorted(favorite_languages.keys()):                 # Com sorted(), faz com que os dados apareçam em ordem alfabética
    print(f"{name.title()}, thank you for taking the poll!")

for name in sorted(favorite_languages.keys(), reverse=True):   # reverse=True para ordem inversa.
    print(f"{name.title()}, thank you for taking the poll!")

# Looping através dos valores de um dicionário:
# for value in nome_dicionário.values()

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# Para retirar valores repetidos:

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# NESTING

# Lista de dicionários

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points:': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:            # Percorre a lista, cada dicionário é impresso
    print(alien)

# Fazer uma lista fazia para armazenar os aliens

aliens = []

# Criar 30 aliens verdes

for alien_number in range(30):      # Range cria a sequência de números que vai repetir a loop
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)        # Após criar o alien, é adicionado à lista

for alien in aliens[0:3]:             # Altera os três primeiro aliens  
    if alien['color'] == 'green':     # que tem a cor verde    
        alien['color'] = 'yellow'     # altera para amarelo
        alien['points'] = '10'      
        alien['speed'] = 'medium'

    elif alien['color'] == 'yellow':        
        alien['color'] = 'red'        
        alien['points'] = '15'
        alien['speed'] = 'fast'

# Exibir os primeiros cinco aliens que foram criados:
for alien in aliens[:5]:              # Percorre a lista até o 5º elemento da lista (0,1,2,3,4)
    print(alien)

print("...")

# Exibir quantos aliens já foram criados?
print(f"The total number of aliens: {len(aliens)}.") 

# Lista dentro de um dicionário:
# Armazenar mais de um value pra mesma key

# Armazenar informação sobre um pedido de pizza, com várias características da pizza

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Resumo do pedido
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

# Armazenar mais de um value pra mesma key, por exemplo numa enquete:

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) == 1: 
        suffix = 'language is'
    else: 
        suffix = 'languages are'
    print(f"\n{name.title()}'s favourite {suffix}:")
    for language in languages:
        print(f"\t{language.title()}")

# Um dicionário dentro de um dicionário

# Exemplo de usuários cadastrados em um site

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")        # Imprime as keys que receberam o nome "username" na chamada da loop
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

    print(f"Full name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")