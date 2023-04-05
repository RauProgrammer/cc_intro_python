#programa para somar os números de um número inteiro
#exemplo: 1234 = 1 + 2 + 3 + 4 = 10

def soma_inteiro(x):
    y = 0

    while x != 0:
        y += x % 10
        x //=10
 
    print(y)   

x = int(input())

soma_inteiro(x)
