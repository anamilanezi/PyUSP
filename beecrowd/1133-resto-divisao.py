x = int(input())
y = int(input())

if x > y:
    n_list = list(range(y + 1, x))
elif y > x:
    n_list = list(range(x + 1, y))

for n in n_list:
    if n % 5 == 2 or n % 5 == 3:
        print(n)

