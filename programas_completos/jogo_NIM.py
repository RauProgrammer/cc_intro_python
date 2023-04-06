
def computador_escolhe_jogada(m, n):
    print("\nComputador começa!")

def usuario_escolhe_jogada(m, n):
    print("\nVocê começa!")
    
    qtd_peças = int(input("\nQuantas peças você vai tirar? "))

def partida():
    print("\nVocê escolheu um partida isolada!")
    
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))    

    if (n % (m + 1) == 0):
        print(usuario_escolhe_jogada(m, n))
    else:
        print(computador_escolhe_jogada(m, n))
    
def campeonato():
    print("\nVocê escolheu um campeonato!")

def main():
    print("Bem vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada")
    op = int(input("2 - para jogar um campeonato "))
    
    if (op == 1):
        partida()
    elif(op == 2):
        print(campeonato())

main()    