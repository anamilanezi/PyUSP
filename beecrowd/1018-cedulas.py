total = int(input())

# 100
notas_100 = total // 100
resto_100 = total % 100

# 50
notas_50 = resto_100 // 50
resto_50 = resto_100 % 50

# 20
notas_20 = resto_50 // 20
resto_20 = resto_50 % 20

# 10
notas_10 = resto_20 // 10
resto_10 = resto_20 % 10

# 5
notas_5 = resto_10 // 5
resto_5 = resto_10 % 5

# 2
notas_2 = resto_5 // 2
resto_2 = resto_5 % 2

# 1
notas_1 = int(resto_2 / 1)

msg = "nota(s) de R$ "

# Funciona mas com Presentation Error
# print(
#         f"{total}\n"
#         f"{notas_100} {msg}100,00\n"
#         f"{notas_50} {msg}50,00\n"
#         f"{notas_20} {msg}20,00\n"
#         f"{notas_10} {msg}10,00\n"
#         f"{notas_5} {msg}5,00\n"
#         f"{notas_2} {msg}2,00\n"
#         f"{notas_1} {msg}1,00\n"
#     )


# Aceito
print(total)
print(f"{notas_100} {msg}100,00")
print(f"{notas_50} {msg}50,00")
print(f"{notas_20} {msg}20,00")
print(f"{notas_10} {msg}10,00")
print(f"{notas_5} {msg}5,00")
print(f"{notas_2} {msg}2,00")
print(f"{notas_1} {msg}1,00")