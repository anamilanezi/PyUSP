valores = input().split(" ")

for i in range(len(valores)):
    valores[i] = float(valores[i])

valores_ordenados= sorted(valores, reverse=True)

A = valores_ordenados.pop(0)
B = valores_ordenados.pop(0)
C = valores_ordenados.pop(0)

if A >= (B + C):
    print("NAO FORMA TRIANGULO")
else:
    if (A ** 2) == ((B ** 2) + (C ** 2)):
        print("TRIANGULO RETANGULO")
    elif (A ** 2) > ((B ** 2) + (C ** 2)):
        print("TRIANGULO OBTUSANGULO")
    elif (A ** 2) < ((B ** 2) + (C ** 2)):
        print("TRIANGULO ACUTANGULO")
    if (A == B) and (B == C):
        print("TRIANGULO EQUILATERO")
    elif (A == B) or (A == C) or (B == C):
        print("TRIANGULO ISOSCELES")