dia_inicial_str = input("Digite o dia inicial: ")
dia_final_str = input("Digite quantos dias ficará fora: ")

dia_inicial = int(dia_inicial_str)
dia_final = int(dia_final_str)

total_dias = dia_inicial + dia_final
conta_dias = total_dias % 7
if (conta_dias == 0):
	print("Retorna domingo")
if (conta_dias == 1):
	print("Retorna segunda-feira")
if (conta_dias == 2):
	print("Retorna terça-feira")
if (conta_dias == 3):
	print("Retorna quarta-feira")
if (conta_dias == 4):
	print("Retorna quinta-feira")
if (conta_dias == 5):
	print("Retorna sexta-feira")
if (conta_dias == 6):
	print("Retorna sábado")