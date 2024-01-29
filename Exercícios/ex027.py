# Primeiro e último nome de uma pessoa
nome = str(input("Digite seu nome completo: ")).strip().split()

print("Muito prazer em te conhecer!")
print(f"Seu primeiro nome é {nome[0]}")
print(f"Seu último nome é {nome[len(nome)-1]}")