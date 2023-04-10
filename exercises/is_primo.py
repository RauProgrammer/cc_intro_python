def is_primo(n):
    div = 0
    seq = 0

    while seq <= n:
        seq += 1
        aux = n % seq
        if aux == 0:
            div += 1
    
    if(div <= 2 and n != 1):
        return "É primo"
    else:
        return "Não é primo"

def main ():
    n = 1
    
    while n != 0:
        n = int(input("Informe um número maior que 1 para saber se é primo (informe 0 para cancelar): "))
        if (n != 0):    
            print(is_primo(n))

main()