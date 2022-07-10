salario = float(input())

aumentos = {
	400.0: 15,
	800.0: 12,
	1200.0: 10,
	2000.0: 7,
	float('inf'): 4
}

novo_salario = salario
reajuste = 0.0

for faixa_salarial in aumentos:
    if salario <= faixa_salarial:
        aumento = aumentos[faixa_salarial]
        reajuste = salario * (aumento / 100)
        novo_salario += reajuste
        break

print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {aumento} %')