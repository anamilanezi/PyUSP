# B > C and D > A and ((C+D) > (A + B)) and C > and D > 0 and (A % 2 == 0)

values = input().split(" ")

A = int(values.pop(0))
B = int(values.pop(0))
C = int(values.pop(0))
D = int(values.pop(0))

if ((B > C) and (D > A)     and ((C+D) > (A + B)) and (C > 0) and (D > 0) and (A % 2 == 0)):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")
    