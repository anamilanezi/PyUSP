num = input().split()
A = int(num.pop(0))
soma = []

for n in num:
    if int(n) > 0:
        N = int(n)

for n in range(N):
    soma.append(A + n)


print(sum(soma))
