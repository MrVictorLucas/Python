#Super Progressão Aritmética v3.0

print("-=-"*10)
print("Super Gerador de PA")
print("-=-"*10)

numero = int(input("Primeiro termo: "))
razao = int(input("Razão da PA: "))
termo = numero
contador = 1
total = 0
termosmais = 10

while termosmais != 0:
    total=total+termosmais
    while contador<=total:
        print(f"{termo} --> ", end="")
        termo+=razao
        contador+=1
    print("PAUSA")
    termosmais = int(input("Quantos termos a mais você quer exibir? "))
print(f"Progressão finalizada com {total} termos")