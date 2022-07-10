####################### Scope #########################

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}") # 2

increase_enemies()
print(f"enemies outside function: {enemies}")    # 1

# Local Scope: variables and functions are available only inside the function

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion() #2
#print(potion_strength)  # NameError: name 'potion_strength' is not defined

# Global Scope: variables and functions are available outside and 
# inside functions, no matter how nested they are

player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
print(player_health)

# A nested function works only inside its scope:
def game():
    def drink_booster():     
        potion_strength = 2
        print(player_health)

    drink_booster()

drink_booster() # NameError: name 'drink_booster' is not defined

# There is no Block Scope

game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

# Usually it's not a good practice to use the same name of a 
# global scope variable in a local variable with a different use.

# To modify a global variable inside a function, we must add 'global variable_name'
# inside it to specify that we want to manipulate in the function, but this should
# be avoided

enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}") # 2

increase_enemies()
print(f"enemies outside function: {enemies}")    # 1

# It's better to simply return the value that we want from calling the function