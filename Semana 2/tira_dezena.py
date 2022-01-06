#S203 - Recebe um número e retorna o dígito da dezena

valor_entrada = int(input("Digite um número inteiro:"))

dezena = valor_entrada % 100       #Resto da divisão contendo os dois últimos dígitos
digito_dezena = dezena // 10       #Quociente inteiro na divisão por 10 representa a dezena

print("O dígito das dezenas é", digito_dezena)

