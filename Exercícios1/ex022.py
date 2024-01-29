# Analisador de texto
nome = str(input("Digite seu nome completo: ")).strip()

print("Analisando seu nome...")
print(f"Seu nome em maiúsculas: {nome.upper()}")
print(f"Seu nome em minúsculas: {nome.lower()}")
print(f"Seu nome tem ao todo {len(nome)-nome.count(' ')} letras")

separado = nome.split()
print(f"Seu primeiro nome tem ao todo {len(separado[0])} letras")