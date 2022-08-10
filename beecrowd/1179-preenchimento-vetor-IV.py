par = []
impar = []
for _ in range(15):
    n = int(input())
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    if len(par) == 5:
        for i in range(len(par)):
            print(f"par[{i}] = {par[i]}")
        par = []
    elif len(impar) == 5:
        for i in range(len(impar)):
            print(f"impar[{i}] = {impar[i]}")
        impar = []

for i in range(len(impar)):
    print(f"impar[{i}] = {impar[i]}")
for i in range(len(par)):
    print(f"par[{i}] = {par[i]}")