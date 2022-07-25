not_null = True

while not_null:
    xy = list(map(lambda n: int(n), input().split(" ")))
    x = xy[0]
    y = xy[1]

    if x == 0 or y == 0:
        not_null = False
    elif x > 0 and y > 0:
        print("primeiro")
    elif x < 0 and y > 0:
        print("segundo")
    elif x < 0 and y < 0:
        print("terceiro")
    else:
        print("quarto")