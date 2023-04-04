x = int(input("Digite um número inteiro: "))
y = 0

while x != 0:
    y += x % 10
    x //=10
 
print(y)