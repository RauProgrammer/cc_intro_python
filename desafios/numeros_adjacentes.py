#programa para saber se um número tem números adjacentes iguais
#exemplo: 12345567 

x = int(input())
aux = x % 10
x //= 10
tem_adjacente = False
cont = 0

while x != 0:
    y = x % 10
    if (y == aux):
        tem_adjacente = True
    else:
        cont += 1
    aux = y
    x //= 10
    
if tem_adjacente:
    print("Esse número contém números adjacentes!")
else:
    print("Esse número não contém números adjacentes!")    