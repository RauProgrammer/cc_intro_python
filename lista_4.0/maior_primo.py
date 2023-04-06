def is_primo(x):
    primo = True
    div = 2
    
    while (x > div):
        if ((x % div) == 0):
            primo = False
        div += 1
    return primo

def maior_primo(x):
    aux = x
    while (aux > 1) and (is_primo(aux) == False):
        aux -= 1
    return aux
