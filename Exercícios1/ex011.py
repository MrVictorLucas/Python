# Pintando Parede

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))
área = largura*altura
tinta = área/3

print(f"Sua parede tem a dimensão de {largura:.1f}X{altura:.1f} e sua área é de {área:.1f}m²")
print(f"Para pintar a sua parede você ira precisar de {tinta:.1f}L de tinta")