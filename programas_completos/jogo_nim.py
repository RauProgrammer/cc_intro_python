
def computador_escolhe_jogada(n, m):
    pc_remove = 1
    
    while (pc_remove != m):
        if (n - pc_remove) % (m + 1) == 0:
            return pc_remove
        else:
            pc_remove += 1
    
    return pc_remove
        

def usuario_escolhe_jogada(n, m):
    is_valido = False
    
    while not is_valido:
        jogada = int(input("\nQuantas peças você vai tirar? "))
        
        if (jogada > m) or (jogada < 1):
            print("\nJogada inválida, tente novamente!")
        else:
            is_valido = True
    
    return jogada
    

def partida():
        
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))    

    pc_turn = False
    
    if (n % (m + 1) == 0):
        print("\nVocê começa!")
        
    else:
        print("\nComputador começa!")
        pc_turn = True
        
    while (n > 0):
        if pc_turn:
            pc_remove = computador_escolhe_jogada(n, m)
            n -= pc_remove
            if (pc_remove == 1):
                print("\nO computador tirou uma peça")
            else:
                print("\nO computador tirou {} peças".format(pc_remove))
            
            pc_turn = False
            
        else:
            jogador_remove = usuario_escolhe_jogada(n, m)
            n -= jogador_remove
            if (jogador_remove == 1):
                print("\nVocê tirou uma peça")
            else:
                print("\nVocê tirou {} peças".format(jogador_remove))
                
            pc_turn = True
        if (n == 1):
            print("Agora resta apenas uma peça no tabuleiro.")
        elif(n != 0):
            print("Agora restam {} peças no tabuleiro.".format(n))
    print("Fim do jogo! O computador ganhou!")
    
def campeonato():
    num_partida = 1
    
    while num_partida <= 3:
        print("\n**** Rodada {} ****\n".format(num_partida))
        partida()
        num_partida +=1
        
    print("\n**** Final do campeonato! ****")
    
    return "\nPlacar: Você 0 X 3 Computador"

def main():
    print("Bem vindo ao jogo do NIM! Escolha:\n")
    print("1 - para jogar uma partida isolada")
    op = int(input("2 - para jogar um campeonato "))
    
    if (op == 1):
        print("\nVocê escolheu um partida isolada!")
        partida()
    elif(op == 2):
        print("\nVocê escolheu um campeonato!")
        print(campeonato())

main()   
