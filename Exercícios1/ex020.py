# Sorteando uma ordem na lista
from random import shuffle

nome1 = str(input("Primeiro Nome: "))
nome2 = str(input("Segundo Nome: "))
nome3 = str(input("Terceiro Nome: "))
nome4 = str(input("Quarto Nome: "))
lista = [nome1, nome2, nome3, nome4]
# Embaralhando a lista / random.shuffle()
shuffle(lista)

print(f"A ordem de aprensentação será {lista}")