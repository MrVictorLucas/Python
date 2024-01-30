# Aprovando empréstimo

cores = {
    'limpa':"\033[m", 
    'azul':"\033[36;1;40m", 
    'vermelho':"\033[31;1;40m", 
    'verde':"\033[32;1;40m"
}

valor_casa = float(input(f"Valor da casa {cores['verde']}R${cores['limpa']}"))
salario = float(input(f"Qual o salário do comprador? {cores['verde']}R${cores['limpa']}"))
anos = int(input("Quantos anos de financiamento? "))
parcelas = (anos*12)
prestações = float(valor_casa/parcelas)

print(f"Para pagar uma casa de {cores['verde']}R${valor_casa:.2f}{cores['limpa']} em {anos} anos a prestação será de {cores['verde']}R${prestações:.2f}{cores['limpa']}")
if prestações>(salario*30/100):
    print(f"Empréstimo {cores['vermelho']}NEGADO{cores['limpa']}!")
else:
    print(f"Empréstimo pode ser {cores['azul']}CONCEDIDO{cores['limpa']}")