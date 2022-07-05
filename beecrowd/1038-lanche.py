codigo_e_quantidade = input().split(" ")

codigo = int(codigo_e_quantidade.pop(0))
quantidade = int(codigo_e_quantidade.pop(0))

precos = [4.0, 4.5, 5.0, 2.0, 1.50]

for num in range(1,len(precos) + 1):
    if codigo == num:
        total = "{:.2f}".format(quantidade * precos[num - 1])
        print(f"Total: R$ {total}")