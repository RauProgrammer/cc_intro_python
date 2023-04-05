import math

def delta(a, b, c):
    delta = ((b ** 2) - (4 * a * c))
    
    return delta

def raizes(delta, a, b):
    if (delta >= 0):
        x = (-b + math.sqrt(delta))//(2*a)
        y = (-b - math.sqrt(delta))//(2*a)
    
        if(x == y):
            print("a raiz desta equação é", x)
        else:
            if(x < y):
                print("as raízes da equação são", x, "e", y)
            elif(x > y):
                print("as raízes da equação são", y, "e", x)
    else:
        print("esta equação não possui raízes reais")

a =  float(input("Informe o valor de a:"))
b =  float(input("Informe o valor de b:"))
c =  float(input("Informe o valor de c:"))

raizes(delta(a, b, c), a, b)

