idade_em_dias = int(input())

anos = idade_em_dias // 365
resto_em_dias = idade_em_dias % 365

meses = resto_em_dias // 30
resto_em_dias = resto_em_dias % 30

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{resto_em_dias} dia(s)")
