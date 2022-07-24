not_equal = True

while not_equal:
    numbers = list(map(lambda x: int(x), input().split(" ")))
    if numbers[0] == numbers[1]:
        not_equal = False
    elif numbers[0] > numbers[1]:
        print("Decrescente")
    else:
        print("Crescente")

