def is_hipotenusa(i, j):
    hip = ((i ** 2) + (j ** 2))
    return hip

def soma_hipotenusas(n):
    h = 1
    soma = 0
    
    while (h <= n):
        hip = (h ** 2)
        i = 1
        j = 1
        
        while (i < n):
            while (j < n):
                if (hip == is_hipotenusa(i, j)):
                    soma += h
                    i = n
                    break
                j += 1
            i += 1
            j = i
        h += 1
    return soma
