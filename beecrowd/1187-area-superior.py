operacao = input()

matriz = []
for linhas in range(12):
    linha = []
    for colunas in range(12):
        linha.append(float(input()))
    matriz.append(linha)

diagonal = []

for i in range(0, 5):
    diagonal.append(matriz[i][i+1:11-i])

diagonal_list = sum(diagonal, [])

soma = sum(diagonal_list)
if operacao == "S":
    print(f"{soma:.1f}")
else:
    media = soma / len(diagonal_list)
    print(f"{media:.1f}")
