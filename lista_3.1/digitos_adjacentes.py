def adjacente(x):
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
        print("sim")
    else:
        print("não")

x = int(input("Digite um número inteiro: "))

adjacente(x)