# Jogo da Adivinhação v2.0
from random import randint
from time import sleep

contador = 1
jogo = str(input("Olá, está afim de jogar um jogo?[S/N] ")).upper().strip()

if jogo == 'S':
    print("Ok, então vamos lá!!!")
    numero = randint(0,10)
    sleep(1)
    print("Acabei de pensar em um número de 0 a 10.")
    palpite = int(input("Consegue adivihar qual é o número? "))
    sleep(1)
    
    while palpite != numero:
        if palpite<numero:
            palpite = int(input("Mais... Tente mais uma vez: "))
            contador+=1
        elif palpite>numero:
            palpite = int(input("Menos... Tente mais uma vez: "))
            contador+=1
        sleep(1)
        
    print(f"Parabéns, você acertou com {contador} tentativas")

else:
    print("Ok, tenha um bom dia!!!")            