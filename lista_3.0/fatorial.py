n = int(input("Digite o valor de n: "))
resp = 1;
count = 1;

while count <= n:
    resp *= count
    count += 1
    
print(resp)