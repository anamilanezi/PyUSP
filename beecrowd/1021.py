
total = float(input())

notas = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
saque = []

for nota in notas:
    if (nota == 0.01):
        quantidade = total / nota
    else:
        quantidade = total // nota
        resto = (total % nota)
        resto = float("{:.2f}".format(resto))
        total = resto
    saque.append(int(quantidade))

# TO DO: Criar um loop para impressão
print("NOTAS:")
print(f"{saque[0]} nota(s) de R$ 100.00")
print(f"{saque[1]} nota(s) de R$ 50.00")
print(f"{saque[2]} nota(s) de R$ 20.00")
print(f"{saque[3]} nota(s) de R$ 10.00")
print(f"{saque[4]} nota(s) de R$ 5.00")
print(f"{saque[5]} nota(s) de R$ 2.00")
print("MOEDAS:")
print(f"{saque[6]} moeda(s) de R$ 1.00")
print(f"{saque[7]} moeda(s) de R$ 0.50")
print(f"{saque[8]} moeda(s) de R$ 0.25")
print(f"{saque[9]} moeda(s) de R$ 0.10")
print(f"{saque[10]} moeda(s) de R$ 0.05")
print(f"{saque[11]} moeda(s) de R$ 0.01")
