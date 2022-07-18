def resto_2(n):
    """Recebe um número e imprime todos os valores entre 1 e 10000 que divididos por n apresentam o resto = 2 """
    for i in range(10001):
        if i % n == 2:
            print(i)


n = int(input())

resto_2(n)