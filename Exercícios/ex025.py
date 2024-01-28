# Procurando uma string dentro de outra
nome = str(input("Digite seu nome completo: ")).strip().lower()
print(f"Seu nome tem Silva? {'silva' in nome}")