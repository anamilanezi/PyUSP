# IF statements
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:          # Loop percorre todos os elementos 
  if car == 'bmw':        # Condicional para um elemento
    print(car.upper())
  else:                   # Aqueles que não obedecem           
    print(car.title())
    
# Comparações são sensíveis à capitalização
# para evitar erros, usar lower() e comparar com minúsculas
car = 'Audi'
car == 'audi'           # False
car.lower() == 'audi'   # True

# Checar inequalidade !=

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")
    
# Comparações numéricas e condições múltiplas:
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21 # False
age_0 >= 21 or age_1 >= 21  # True

# Verificar se um valor está na lista com in: 

requested_toppings = ['mushrooms', 'onions', 'pineapple']

'mushrooms' in requested_toppings #True
'pepperoni' in requested_toppings # False

# Verificar se um valor NÃO está na lista com not in:

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Expressões booleanas podem ser atribuídas a variáveis
game_active = True
can_edit = False

# Declarações if else executa somente condição obedecida:
age = 17
if age >= 18:
    print("You are old enought to vote!")
    print("Have your registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
    
# Cadeia if-elif-else
age = 12
if age > 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

# modo alternativo

age = 12
if age > 4:
    price = 0
elif age < 18:
    price = 25
elif age > 65:
    price = 40 
else:
    price = 20

print(f"Your admission cost is ${price}.")

# Testar condições multiplas: a cadeia if-elif-else é apropriada somente se só precisa passar em um teste

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
    
print("\nFinished making your pizza!")

# Usar declarações if com listas:

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_topping:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")

print("\n Finished making your pizza!")

# Verificar se uma lista não está vazia:

requested_toppings = []

if requested_toppings:          # Se a lista não estiver vazia
    for requested_topping in requested_topping:
        print(f"Adding {requested_topping}.")
    print("\n Finished making your pizza!")
else:                           # Se a lista estiver vazia
    print("Are you sure you want a plain pizza?")

# Utilizando mais de uma lista

availabe_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni','pineapple', 'extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
    if requested_toppings in availabe_toppings:
        print(f"Adding {requested_topping}.")
    else: 
        print(f"Sorry, we don't have {requested_topping}.")
    
    print("\nFinished making your pizza!")
