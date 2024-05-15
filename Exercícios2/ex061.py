# Progressão Aritmética v2.0

print("-=-"*10)
print("Gerador de PA")
print("-=-"*10)

numero = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = numero
contador = 1

while contador<=10:
    print(f"{termo} --> ", end="")
    termo+=razao
    contador+=1
print("FIM")