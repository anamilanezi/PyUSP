x = int(input())
y = int(input())

if x > y:
    n_list = list(range(y, x + 1))
elif y > x:
    n_list = list(range(x, y + 1))

nao_multiplos_13 = [n for n in n_list if n % 13 != 0]
print(sum(nao_multiplos_13))