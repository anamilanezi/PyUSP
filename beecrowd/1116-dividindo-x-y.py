n_valores = int(input())

for _ in range(n_valores):
    xy = list(map(lambda n: int(n), input().split(" ")))
    x = xy[0]
    y = xy[1]

    if y == 0:
        print("divisao impossivel")
    else:
        print(x/y)
