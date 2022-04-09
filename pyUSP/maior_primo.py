def éPrimo(x):
    div = 2
    if x == 2:
        return True
    while x % div != 0 and div <= x/2:
        div += 1
    if x % div == 0:
        return False
    else:
        return True

def maior_primo(n):
    if éPrimo(n):
        return n
    else:
        while n > 2 and not éPrimo(n):
            n = n - 1
            if éPrimo(n):
                return n
        
