# Grupo da Maioridade
from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for pessoa in range(1,8):
    
    nascimento = int(input(f"Em que ano a {pessoa}ª pessoa nasceu? "))
    idade = atual - nascimento

    if idade>=21:
        totalmaior=totalmaior+1
    else:
        totalmenor=totalmenor+1
print(f"Ao todo, {totalmaior} são da Maioridade")
print(f"E {totalmenor} são da menoridade")