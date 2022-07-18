def fatorial(n):
    """Recebe um número inteiro n e retorna seu número fatorial"""
    fatorial = 1
    while n > 1:
        fatorial *= n
        n -= 1
    return fatorial

n = 1

while n >= 0:
    n = int(input("Digite um número inteiro para obter seu fatorial "
                  "(negativo para sair): "))
    print(fatorial(n))



