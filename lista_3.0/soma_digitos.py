def soma_digitos(x):
    y = 0

    while x != 0:
        y += x % 10
        x //=10
 
    print(y)

x = int(input("Digite um número inteiro: "))

soma_digitos(x)