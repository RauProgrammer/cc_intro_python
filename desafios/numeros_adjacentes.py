#programa para saber se um número tem números adjacentes iguais
#exemplo: 12345567 

x = int(input())
y = 0
aux = 1
tem_adjacente = False


while x != 0:
    y = x % 10
    x //= 10
    
    if (y == aux):
        tem_adjacente = True
    aux = y
    
if tem_adjacente:
    print("Esse número contém números adjacentes!")
else:
    print("Esse número não contém números adjacentes!")    