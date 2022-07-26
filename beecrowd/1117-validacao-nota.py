recebe_nota = True
notas = []

while recebe_nota:
    n = float(input())
    if 0 <= n <= 10:
        notas.append(n)
        if len(notas) == 2:
            recebe_nota = False
            media = sum(notas) / len(notas)
            print(f"media = {media:.2f}")
    else:
        print("nota invalida")
