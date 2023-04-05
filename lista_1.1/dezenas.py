def dezena(numero):
    unidade = numero % 10

    numero = numero - unidade

    numero = numero // 10

    dezena = numero % 10

    print("O dígito das dezenas é", dezena)

numero =  int(input("Digite um número inteiro: "))

dezena(numero)

