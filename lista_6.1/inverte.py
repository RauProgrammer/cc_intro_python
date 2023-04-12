def inverte(lista):
    lista_invertida = []
    
    for item in lista:
        lista_invertida.append(item)
        
    lista_invertida.reverse()

    n = 0 
    
    while n < len(lista_invertida):
        print(lista_invertida[n])
        n += 1

def main():
    n = 1
    lista = []
    
    while (n != 0):
        n = int(input("Digite um número: "))
        if (n != 0):
            lista.append(n)

    inverte(lista)
    