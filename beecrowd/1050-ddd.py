ddd = int(input())

ddds = {
    61: 'Brasilia',
    71: 'Salvador',
    11: 'Sao Paulo',
    21: 'Rio de Janeiro',
    32: 'Juiz de Fora',
    19: 'Campinas',
    27: 'Vitoria',
    31: 'Belo Horizonte'
}

if ddd in ddds:
    print(ddds[ddd])
else:
    print("DDD nao cadastrado")