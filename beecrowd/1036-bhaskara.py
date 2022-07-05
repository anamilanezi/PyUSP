# delta = (b ** 2) - (4 * a * c)
# x1 = ((-b) + (delta ** 0.5)) / 2 * a
# x1 = ((-b) - (delta ** 0.5)) / 2 * a

# if (2 * a == 0 or delta < 0)

abc = (input()).split(" ")

a = float(abc.pop(0))
b = float(abc.pop(0))
c = float(abc.pop(0))

def bhaskara(a, b, c):

    delta = (b ** 2) - (4 * a * c)
    if (a == 0 or delta < 0):
        print("Impossivel calcular")
    else:
        x1 = ((-b) + (delta ** 0.5)) / (2 * a)
        x2 = ((-b) - (delta ** 0.5)) / (2 * a)
        x1 = "{:.5f}".format(x1)
        x2 = "{:.5f}".format(x2)
        print(f"R1 = {x1}")
        print(f"R2 = {x2}")

bhaskara(a,b,c)

