def retangulo_vazado(l, a):
    line = 1
    
    while (line <= a):
        print("#", end =  "")
        col =  2
        
        while col < l:
            if ((line == 1) or (line == a) or (col == l)):
                print("#", end = "")
            else:
                print(end = " ")
            col += 1
        print("#")

        line += 1


def main():
    l = int(input("digite a largura: "))
    a = int(input("digite a altura: "))
    
    retangulo_vazado(l, a)
        
main()