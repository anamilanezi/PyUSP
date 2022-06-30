nome = input("Digite o nome: ")
salario = float(input("Digite o salario: "))
vendas = float(input("Digite o total: "))

comissao = vendas * 0.15


total = salario + comissao

total_double = "{:0.2f}".format(total)
print(f"TOTAL = R$ {total_double}")

