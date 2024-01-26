# Conversão de Moedas
real = float(input("Quantos reais você tem na carteira? R$"))
dólar = real / (4.92)
euro = real / (5.34)

print(f"Com R${real:.2f} você consegue comprar US${dólar:.2f}")
print(f"Com R${real:.2f} você consegue comprar €{euro:.2f}")