l1 = input("1")            
l2 = input("2")            

l1 = l1.split(" ")      
l2 = l2.split(" ")

n1 = int(l1[1])
v1 = float(l1[2])

n2 = int(l2[1])
v2 = float(l2[2])

t1 = n1 * v1
t2 = n2 * v2
total = t1 + t2
total = "{:0.2f}".format(total)

print(f"VALOR A PAGAR: R$ {total}")
