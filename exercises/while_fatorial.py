def fatorial(n):
    count = 1
    fat = 1
    
    if(n > 0):
        while (count <= n):
                fat *= count
                count += 1 
        print(fat)
    elif (n < 0):
        print("Não existe fatorial de número negativo!")   

def main():
    n = 1

    while n != 0:
        n = int(input("Informe o número que deseja saber o fatorial (digite 0 para cancelar): "))
        fatorial(n)

main()