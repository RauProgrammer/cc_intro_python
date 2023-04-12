def remove_repetidos(lista):
    lista_rep = []
    
    for item in lista:
        if item not in lista_rep:
            lista_rep.append(item)
       
    lista_rep.sort()     
    return lista_rep

