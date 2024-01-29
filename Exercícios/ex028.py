# Jogo de adivinhação
from random import choice
from time import sleep

sorteado = choice([0,1,2,3,4,5])
print("-=-"*20)
print("Vou pensar em um número entre 0 e 5, tente adivinhar...")
print("-=-"*20)

num = int(input("Em que número eu pensei? "))

print("PROCESSANDO...")
sleep(2)

if sorteado == num:
    print("Parabéns, você acertou!")
else:
    print(f"Que pena, você errou! O número que eu pensei foi {sorteado}")