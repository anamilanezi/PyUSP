def par_impar(n):
    paridade = ""
    sinal = ""
    if n == 0:
        return "NULL"
    if n > 0:
        sinal = "POSITIVE"
    else:
        sinal = "NEGATIVE"
    if n % 2 == 0:
        paridade = "EVEN"
    else:
        paridade = "ODD"
    return f"{paridade} {sinal}"


t = int(input())

for i in range(t):
    n = int(input())
    print(par_impar(n))