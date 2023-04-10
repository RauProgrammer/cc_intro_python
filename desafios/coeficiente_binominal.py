def fatorial(x):
    fat_x = 1
    count = 1
    
    while (count <= x):
        fat_x *= count
        count += 1
        
    return fat_x     

def coeficiente_binomial(n, k):
    if (n < 0 or k < 0):
        print("Não existe fatorial negativo!")
    else:
        binomial = (fatorial(n))//(fatorial(k) * fatorial(n-k))
        
        print(binomial)
        
coeficiente_binomial(10, 6)  

