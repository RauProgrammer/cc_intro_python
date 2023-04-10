def is_primo(n):
    div = 0
    seq = 0

    while seq <= n:
        seq += 1
        aux = n % seq
        if aux == 0:
            div += 1
    
    if(div <= 2 and n != 1):
        return True
    else:
        return False
    
def n_primos(n):
    count_primo = 0

    while (n >= 2):
        if is_primo(n):
            count_primo += 1    
        n -= 1

    return count_primo
