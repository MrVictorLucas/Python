# A parte inteira de um número
from math import trunc

num = float(input("Digite um valor: "))

print(f"O valor digitado foi {num} e a sua porção inteira é {trunc(num)}") # ou {int(num)}