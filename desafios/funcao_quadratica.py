#programa para saber as raízes de uma função quadrada

import math

a =  int(input("Informe o valor de a:"))
b =  int(input("Informe o valor de b:"))
c =  int(input("Informe o valor de c:"))

delta = ((b ** 2) - (4 * a * c))

if (delta >= 0):
    r1 = (-b + math.sqrt(delta))//(2*a)
    r2 = (-b - math.sqrt(delta))//(2*a)
    
    if (r1 != r2):
        print("Essa função possui duas raízes reais distintas que são:", r1,"e", r2)
    elif (r1 == r2):
        print("Essa função possui duas raízes reais iguais que são:", r1,"e", r2)

else:
    print("Essa função não contém raízes reais")