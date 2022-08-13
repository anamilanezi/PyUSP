operacao = input()

matriz = []
for linhas in range(12):
    linha = []
    for colunas in range(12):
        linha.append(float(input()))
    matriz.append(linha)
diagonal = []

for i in range(1, 12):
    diagonal.append(matriz[i][0:i])

# Tranforma a lista de listas em uma lista única:
diagonal_list = sum(diagonal, [])

soma = sum(diagonal_list)
if operacao == "S":
    print(f"{soma:.1f}")
else:
    media = soma / len(diagonal_list)
    print(f"{media:.1f}")
