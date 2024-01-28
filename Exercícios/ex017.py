# Calcúlando a Hipotenusa
from math import hypot

catop = float(input("Comprimento do cateto oposto: "))
catadj = float(input("Comprimento do cateto adjacente: "))
hipotenusa = hypot(catop, catadj)

print(f"A hipotenusa vai medir {hipotenusa:.2f}")