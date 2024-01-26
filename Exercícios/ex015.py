# Aluguel de Carros
dias = int(input("Quantos dias alugado? "))
km = float(input("Quantos Km rodados? "))
preço = (dias*60)+(km*0.15)

print(f"O valor total a se pagar é de R${preço:.2f}")