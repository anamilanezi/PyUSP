t = int(input())


def media_ponderada(a, b, c):
    return round(((a * 2) + (b * 3) + (c * 5)) / 10, 1)


for i in range(t):
    valores = input().split(" ")
    a = float(valores.pop(0))
    b = float(valores.pop(0))
    c = float(valores.pop(0))
    print(media_ponderada(a, b, c))


