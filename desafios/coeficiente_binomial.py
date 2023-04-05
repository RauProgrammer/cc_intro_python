def resp_final(resp_n, resp_k, resp_nk):
    resp_final = (resp_n)//(resp_k * resp_nk)
    
    print(resp_final)

def fatorial(n, k):
    count1 = 1
    count2 = 1
    count3 = 1
    
    fat_n = 1
    fat_k = 1
    fat_nk = 1
    
    nk = n - k

    while count1 <= n:
        fat_n *= count1
        count1 += 1
    
    while count2 <= k:
        fat_k *= count2
        count2 +=1
    
    while count3 <= nk:
        fat_nk *= count3
        count3 +=1
    
    resp_final(fat_n, fat_k, fat_nk)

def coeficiente_binomial(n, k):
    fatorial(n, k)  
    
coeficiente_binomial(10,6)  

