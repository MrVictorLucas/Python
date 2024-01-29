# Informações das Variáveis
algo = input("Digite algo: ")

print(f"O tipo primitivo de {algo} é ", type(algo))
print("Só tem espaços? ", algo.isspace())
print("É um número? ", algo.isnumeric())
print("É alfabético? ", algo.isalpha())
print("É alfanumérico? ", algo.isalnum())
print("Está em maiúscula? ", algo.isupper())
print("Está em minúscula? ", algo.islower())
print("Está capitalziada? ", algo.istitle())