def soma_elementos(lista):
    soma = 0
    
    for item in lista:
        soma += item

    return soma

lista = [1, 2, 3, 4]

print(soma_elementos(lista))