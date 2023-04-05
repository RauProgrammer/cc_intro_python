def fatorial(n):
    fat_n = 1;
    count = 1;

    if (n >= 0):
        while (count <= n):
            fat_n *= count
            count += 1
        
        print(fat_n)
    else:
        print("Não existe fatorial de número negativo")
        
n = int(input("Digite o valor de n: "))

fatorial(n)