# Primeira e última ocorrência de uma string
frase = str(input("Digite uma frase: ")).upper().strip()

print(f"A letra A aparece {frase.count('A')} vezes na frase.")
print(f"A primeira letra A apareceu na posição {frase.find('A')+1}")
print(f"A última letra A apareceu na posição {frase.rfind('A')+1}")