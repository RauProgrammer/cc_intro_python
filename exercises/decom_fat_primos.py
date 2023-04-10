def primo(x):
    is_primo = False
    
    div = 0
    seq = 0
    
    while (seq <= x):
        seq += 1
        aux = x % seq
        if (aux == 0):
            div += 1
    
    if (div <= 2):
        is_primo = True
    else:
        is_primo = False

    return is_primo

def fator_primos(n):
    fator = 2
    mult = 0
    
    while (n > 1):
        if primo(fator):
            while (n % fator == 0):
                mult += 1
                n /= fator
            if (mult > 0):
                print("Fator {} tem multiplicidade {}".format(fator, mult))
            fator += 1
            mult = 0
        else:
            fator += 1
            mult = 0

def main():
    n = int(input("Informe um número maior que 1: "))
    
    fator_primos(n)
    
main()