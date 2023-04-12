def maior_elemento(lista):
    i = 0
    maior = lista[i]
    
    for i in lista:
        if i > maior:
            maior = i
        i += 1
        
    return maior

