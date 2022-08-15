operacao = input()

matriz = []
for linhas in range(12):
    linha = []
    for colunas in range(12):
        linha.append(float(input()))
    matriz.append(linha)

esquerda = []

for i in range(1, 6):
    esquerda.append(matriz[i][0:i])

col = 1
for i in range(6, 11):
    esquerda.append(matriz[i][0:i-col])
    col += 2

esquerda_list = sum(esquerda, [])

soma = sum(esquerda_list)
if operacao == "S":
    print(f"{soma:.1f}")
else:
    media = soma / len(esquerda_list)
    print(f"{media:.1f}")
