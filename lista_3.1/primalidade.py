n = int(input("Digite um número inteiro: "))
div = 0
seq = 0

while seq <= n:
    seq += 1
    aux = n % seq
    if aux == 0:
        div += 1
    
if(div <= 2):
    print("primo")
else:
    print("não primo")