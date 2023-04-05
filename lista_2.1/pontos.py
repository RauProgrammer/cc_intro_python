import math

def dist_pontos(x1, x2, y1, y2):

    dist = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

    if(dist >= 10):
        print("longe")
    else:
        print("perto")
        
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())

dist_pontos(x1, x2, y1, y2) 