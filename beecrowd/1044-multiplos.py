valores = input().split(" ")

n1 = int(valores.pop(0))
n2 = int(valores.pop(0))

if (n1 % n2 == 0) or (n2 % n1 == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")