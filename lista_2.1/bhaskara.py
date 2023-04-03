import math

a =  float(input("Informe o valor de a:"))
b =  float(input("Informe o valor de b:"))
c =  float(input("Informe o valor de c:"))

delta = ((b ** 2) - (4 * a * c))

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