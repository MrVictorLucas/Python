# Jogo: Pedra, Papel e Tesoura
from random import randint
from time import sleep
cores = {
    'limpa':"\033[m",
    'vermelho':"\033[31;1m",
    'azul':"\033[36;1m",
    'amarelo':"\033[32;1m",
    'roxo':"\033[35;1m"
}
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print("""Sua opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")
jogador = int(input("Qual a sua jogada? "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!!!")

print(f"{cores['roxo']}-="*12, f"{cores['limpa']}")
print(f"Computador jogou {cores['roxo']}{itens[computador]}{cores['limpa']}")
print(f"Jogador jogou {cores['roxo']}{itens[jogador]}{cores['limpa']}")
print(f"{cores['roxo']}-="*12, f"{cores['limpa']}")

if computador==0: #Computador jogou PEDRA
    if jogador==0: #Jogador jogou PEDRA
        print(f"{cores['amarelo']}EMPATE!{cores['limpa']}")
    elif jogador==1: #Jogador jogou PAPEL
        print(f"{cores['azul']}JOGADOR GANHOU!{cores['limpa']}")
    elif jogador==2: #Jogador jogou TESOURA
        print(f"{cores['vermelho']}JOGADOR PERDEU!{cores['limpa']}")
    else:
        print(f"{cores['vermelho']}JOGADA INVÁLIDA!{cores['limpa']}")
        
elif computador==1: #Computador jogou PAPEL
    if jogador==0: # PEDRA
        print(f"{cores['vermelho']}JOGADOR PERDEU!{cores['limpa']}")
    elif jogador==1: #PAPEL
        print(f"{cores['amarelo']}EMPATE!{cores['limpa']}")
    elif jogador==2: #TESOURA
        print(f"{cores['azul']}JOGADOR GANHOU!{cores['limpa']}")
    else:
        print(f"{cores['vermelho']}JOGADA INVÁLIDA!{cores['limpa']}")
        
elif computador==2: #Computador jogou TESOURA
    if jogador==0: #PEDRA
        print(f"{cores['azul']}JOGADOR GANHOU!{cores['limpa']}")
    elif jogador==1: #PAPEL
        print(f"{cores['vermelho']}JOGADOR PERDEU!{cores['limpa']}")
    elif jogador==2: #TESOURA
        print(f"{cores['amarelo']}EMPATE!{cores['limpa']}")
    else:
        print(f"{cores['vermelho']}JOGADA INVÁLIDA!{cores['limpa']}")
print(f"{cores['roxo']}-="*12, f"{cores['limpa']}")