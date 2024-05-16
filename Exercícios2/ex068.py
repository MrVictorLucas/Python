from random import randint
vitoria = False
contador = 0

print("=-"*15)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-"*15)
while True:
    escolhajogador = str(input("PAR OU ÍMPAR? [P/I] ")).strip().upper()
    if not escolhajogador in 'PI':
        escolhajogador = str(input("OPÇÃO INVÁLIDA. Tente Novamente, PAR OU ÍMPAR? [P/I] ")).strip().upper()
    jogador = int(input("Digite um valor: "))
    maquina = randint(0, 10)
    soma = jogador+maquina
    
    if soma%2==0:
        print(f"Você jogou {jogador} e o computador {maquina}. Total de {soma} DEU PAR")
    else:
        print(f"Você jogou {jogador} e o computador {maquina}. Total de {soma} DEU ÍMPAR")
    
    if escolhajogador == 'P':
        if soma%2==0:
            vitoria = True
            contador+=1
        else:
            vitoria = False
    if escolhajogador == 'I':
        if soma%2!=0:
            vitoria = True
            contador+=1
        else:
            vitoria=False
    
    if vitoria == True:
        print("Você VENCEU!")
        print("Vamos jogar novamente...")
        print("=-"*15) 
    elif vitoria == False:
        print("Você PERDEU!")
        print("=-"*15)
        print(f"GAME OVER! Você venceu {contador} vezes consecutivas")
        break