# Progressão Aritmética
print("="*40)
print(" "*8, "10 TERMOS DE UMA PA", " "*8)
print("="*40)

primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
décimo = primeiro+(10)*razão

for termo in range(primeiro, décimo, razão):
    print(f"{termo} => ", end='')
print("ACABOU")