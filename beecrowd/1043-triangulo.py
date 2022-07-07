# Dados três segmentos de reta distintos, se a soma das medidas de dois deles é sempre maior que a medida do terceiro, então, eles podem formar um triângulo.

# Não é necessário fazer as três somas para verificar a possibilidade de um triângulo existir. Basta fazer a soma entre os dois lados menores.

valores = input().split(" ")

for i in range(len(valores)):
    valores[i] = float(valores[i])

valores_ordenados= sorted(valores)

if valores_ordenados[0] + valores_ordenados[1] > valores_ordenados[2]:
    perimetro = 0
    for v in valores_ordenados:
        perimetro += v
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = ((valores[0] + valores[1]) * valores[2]) / 2
    print(f"Area = {area:.1f}")