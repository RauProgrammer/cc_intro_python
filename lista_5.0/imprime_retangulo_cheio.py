def retangulo_cheio(l, a):
    line = 1
    while(line <= a):
        col = 1
        while(col <= l):
            print("#", end = "")
            col += 1
        print("")
        line += 1

def main():
    l = int(input("digite a largura: "))
    a = int(input("digite a altura: "))
    
    retangulo_cheio(l, a)
        
main()