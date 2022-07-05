values = (input("Digite os valores ")).split()

A = int(values.pop(0))
B = int(values.pop(0))
C = int(values.pop(0))

maiorAB = (A + B + abs(A - B)) / 2

maior = (maiorAB + C + abs(maiorAB - C)) / 2

print(f"{int(maior)} eh o maior")
