largura = int(input("digite a largura: "))
altura = int(input("digite a altura: "))
desenha_largura = largura
desenha_altura = altura

def preenche(x):
    while x > 0:
        print ("#", end = "")
        x -= 1
def vazio(a, b):
    while a > 0:
        if a == b or a == 1:
            print("#", end = "")
        else:
            print(" ", end = "")
        a -= 1

while desenha_altura > 0:
    if (desenha_altura == altura) or (desenha_altura == 1):
        preenche(desenha_largura)
    else:
        vazio(desenha_largura, largura)

    print()
    desenha_altura -= 1
    desenha_largura = largura
