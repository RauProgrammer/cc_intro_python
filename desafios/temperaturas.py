def maior_temperatura(lista):
    i = 0
    maior = lista[i]
    
    for i in lista:
        if i > maior:
            maior = i
        i += 1
    
    return maior

def menor_temperatura(lista):
    i = 0
    menor = lista[0]
    
    for i in lista:
        if i < menor:
            menor = i
        i += 1
    
    return menor


def maior_menor_temperaturas(lista):
    print("A maior temperatura foi: {}° C".format(maior_temperatura(lista)))
    print("A menor temperatura foi: {}° C".format(menor_temperatura(lista)))
    
    
    
def main():
    lista = [5, 4, 3]
    
    maior_menor_temperaturas(lista)
    
    
main()