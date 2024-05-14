# Detector de Palíndromo
cores={
    'limpa':"\033[m",
    'azul':"\033[36;1m",
    'vermelho':"\033[31;1m",
    'amarelo':"\033[33;1m"
}

frase = str(input("Digite uma frase: ")).upper().strip()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for letra in range(len(junto)-1, -1, -1) :
    inverso+=junto[letra]
    
if inverso==junto:
    print(f"{cores['amarelo']}{frase}{cores['limpa']} {cores['azul']}é um palíndromo!{cores['limpa']}")
else:
    print(f"{cores['amarelo']}{frase}{cores['limpa']} {cores['vermelho']}não é um palíndromo{cores['limpa']}, pois seu inverso é {cores['amarelo']}{inverso}{cores['limpa']}")