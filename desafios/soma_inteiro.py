#programa para somar os números de um número inteiro
#exemplo: 1234 = 1 + 2 + 3 + 4 = 10

x = int(input())
y = 0

while x != 0:
    y += x % 10
    x //=10
 
print(y)   