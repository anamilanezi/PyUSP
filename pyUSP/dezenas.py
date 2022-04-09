numero_str = input("Digite um número inteiro: ")
numero = int(numero_str)
calcula_dezena = numero % 100
dezena = calcula_dezena // 10
print("O dígito das dezenas é", dezena)
