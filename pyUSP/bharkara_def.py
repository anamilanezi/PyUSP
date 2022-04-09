import math

def bhaskara(a, b, c):
    delta = ((b ** 2) - (4 * a * c))
    if (delta < 0):
        print ("esta equação não possui raízes reais")
    else:
        raiz = math.sqrt(delta) / 2 * a
            if delta == 0:
                return -b + raiz
            else:
                raiz1 = -b + raiz
                raiz2 = -b - raiz
            if raiz2 > raiz1:
                print ("as raízes da equação são", raiz1, raiz2)
            else:
                print ("as raízes da equação são", raiz2, raiz1)
                
                
