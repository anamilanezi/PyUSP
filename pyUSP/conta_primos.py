def ehPrimo(x):
    div = 2
    if x == 2:
        return True
    while x % div != 0 and div <= x/2:
        div += 1
    if x % div == 0:
        return False
    else:
        return True

def n_primos(n):
    conta = 0
    while n >= 2:
        if ehPrimo(n):
            conta += 1
        n = n - 1
    return conta
