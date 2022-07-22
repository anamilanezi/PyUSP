
def soma_decimos(x):
    n = x + 0.2
    return n


i = 0
jlist = [1, 2, 3]

for _ in range(11):
    for j in jlist:
        if i == 0 or i == 1.0 or i > 1.9:
            print(f"I={i:.0f} J={j:.0f}")
        else:
            print(f"I={i:.1f} J={j:.1f}")
    for j in range(3):
        j = soma_decimos(j)
    i = soma_decimos(i)




