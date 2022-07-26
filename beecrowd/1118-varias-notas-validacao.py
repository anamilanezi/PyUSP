recebe_nota = True
notas = []

while recebe_nota:
    n = float(input())
    if 0 <= n <= 10:
        notas.append(n)

        if len(notas) == 2:
            media = sum(notas) / len(notas)
            print(f"media = {media:.2f}")

            novo_calculo = 0

            while novo_calculo < 1 or novo_calculo > 2:
                print("novo calculo (1-sim 2-nao)")
                novo_calculo = int(input())
            if novo_calculo == 2:
                recebe_nota = False
            else:
                notas = []
    else:
        print("nota invalida")
