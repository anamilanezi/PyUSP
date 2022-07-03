
total = float(input())

notas = [100.0, 50.0, 20.0, 10.0, 5.0, 2.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
saque = []

for nota in notas:
    quantidade = total // nota
    resto = total % nota
    print(total, quantidade, nota)
    total = resto
    print(f"Total atual= {total}")