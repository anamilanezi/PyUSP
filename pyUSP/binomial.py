def fatorial(n):
    conta = 2
    fat = 1

    if n == 0 or n == 1:
        return 1
    else:
        while conta <= n:
            fat = fat * conta
            conta = conta + 1
        return fat
        
def binomial(a, b):
    return fatorial(a) / (fatorial(b) * fatorial(a - b))


binomial(5, 3)
