# 6.2 Favorite numbers

favorite_numbers = {
    'gi': [13, 8],
    'maria': [19, 21],
    'rodeval': [71, 22, 13],
    'luan': [88, 31, 13],
    'lorena': [7, 13, 11, 4],
    'ana': [13, 30, 7, 3]
}

for person in favorite_numbers:
    print(f"{person.title()} favorite numbers are:")
    for n in favorite_numbers[person]:
        print(n)

# number = favorite_numbers['gi']
# print(f"Gi's favorite number is {number}.")
#
# number = favorite_numbers['maria']
# print(f"Maria's favorite number is {number}.")
#
# number = favorite_numbers['rodeval']
# print(f"Rodeval's favorite number is {number}.")
#
# number = favorite_numbers['luan']
# print(f"Luan's favorite number is {number}.")
#
# number = favorite_numbers['lorena']
# print(f"Lorena's favorite number is {number}.")
#
# number = favorite_numbers['ana']
# print(f"Ana's favorite number is {number}.")