operacao = input()

matriz = []
for linhas in range(12):
    linha = []
    for colunas in range(12):
        linha.append(float(input()))
    matriz.append(linha)

direita = []

for i in range(1, 6):
    direita.append(matriz[i][12-i:12])

col = 5
for i in range(6, 12):
    direita.append(matriz[i][12 - col:12])
    col -= 1

direita_list = sum(direita, [])

soma = sum(direita_list)
if operacao == "S":
    print(f"{soma:.1f}")
else:
    media = soma / len(direita_list)
    print(f"{media:.1f}")
