senha_invalida = True

while senha_invalida:
    senha = int(input())
    if senha == 2002:
        print("Acesso Permitido")
        senha_invalida = False
    else:
        print("Senha Invalida")