# Índice de Massa Corporal
cores = {
    'limpa':"\033[m",
    'azul':"\033[36;1m",
    'amarelo':"\033[33;1m"
}
print(f"{cores['amarelo']}-=-"*20)
print("        CÁLCULO DE ÍNDICE DE MASSA CORPORAL")
print("-=-"*20, f"{cores['limpa']}")

peso = float(input("Qual é seu peso? (Kg) "))
altura = float(input("Qual a sua altura? (m) "))
imc = peso/(altura**2)

print(f"{cores['amarelo']}-=-"*20, f"{cores['limpa']}")
print(f"O seu IMC é de {imc:.1f}")

if imc<=(18.5):
    print(f"Você está {cores['azul']}Abaixo do Peso{cores['limpa']}!")
elif imc>(18.5) and imc<25:
    print(f"Você está no {cores['azul']}Peso Ideal{cores['limpa']}!")
elif imc>=25 and imc<30:
    print(f"Você está com {cores['azul']}Sobrepeso{cores['limpa']}!")
elif imc>=30 and imc<35:
    print(f"Você está com {cores['azul']}Obesidade Grau I{cores['limpa']}!")
elif imc>=35 and imc<40:
    print(f"Você está com {cores['azul']}Obesidade Grau II (Severa){cores['limpa']}!")
elif imc>=40:
    print(f"Você está com {cores['azul']}Obesidade Grau III (Mórbida){cores['limpa']}!")