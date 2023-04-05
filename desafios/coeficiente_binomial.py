def fatorial(x):
    count = 1
    fat_x = 1
    
    if (x >= 0):
        while (count <= x):
            fat_x *= count
            count +=1
        
        return fat_x
    else:
        print("Não existe fatorial de número negativo!")

def coeficiente_binomial(n, k):
    binomial = fatorial(n)//(fatorial(k) * fatorial(n-k)) 
    
    print(binomial) 
    
coeficiente_binomial(10,6)  

