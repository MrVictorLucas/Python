# Sorteando nomes
from random import choice

nome1 = str(input("Digite o nome do Primeiro Aluno: "))
nome2 = str(input("Digite o nome do Segundo Aluno: "))
nome3 = str(input("Digite o nome do Terceiro Aluno: "))
nome4 = str(input("Digite o nome do Quarto Aluno: "))
lista = [nome1, nome2, nome3, nome4]

# random.choice() / escolhe um valor aleatório da lista
print(f"O aluno escolhido foi {choice(lista)}")