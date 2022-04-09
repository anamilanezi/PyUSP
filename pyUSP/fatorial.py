n = int(input("Digite o valor de n: "))
fat = 1
def fatorial(x):
    while x > 1:
        global fat
        fat = fat * x
        x = x - 1
        return fat
while n >= 0:
    while n > 1:
        print(fatorial(n))

    n = int(input("Digite o valor de n: "))
