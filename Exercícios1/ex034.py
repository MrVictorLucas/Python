# Aumentos múltiplos
cores = {
    'limpa':"\033[m", 
    'verde':"\033[32;1;40m", 
    'vermelho':"\033[31;1;40m"
}
salario = float(input("Qual é o salário do funcionário? R$"))

if salario<=(1250):
    aumento = salario+(salario*15/100)
else:
    aumento = salario+(salario*10/100)

print(f"Quem ganhava {cores['vermelho']}R${salario:.2f}{cores['limpa']} passa a ganhar {cores['verde']}R${aumento:.2f}{cores['limpa']} agora.")