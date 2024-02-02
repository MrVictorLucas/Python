# Analisando Triângulos v2.0
cores = {
    'limpa':"\033[m",
    'vermelho':"\033[31;1m",
    'azul':"\033[34;1m",
    'amarelo':"\033[33;1m",
    'verde':"\033[32;1m"
}

print(f"{cores['amarelo']}-=-"*20)
print("    ANALISADOR DE TRIÂNGULOS")
print("-=-"*20, f"{cores['limpa']}")

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

print(f"{cores['amarelo']}-=-"*20, f"{cores['limpa']}")

if r1<r2+r3 and r2<r1+r3 and r3<r1+r2:
    print(f"Os segmentos acima {cores['azul']}PODEM FORMAR{cores['limpa']} um triângulo ", end='')
    
    if r1==r2==r3:
        print(f"{cores['verde']}EQUILÁTERO{cores['limpa']}!")
    elif r1!=r2!=r3!=r1:
        print(f"{cores['verde']}ESCALENO{cores['limpa']}!")
    else:
        print(f"{cores['verde']}ISÓCELES{cores['limpa']}!")
else:
    print(f"Os segmentos acima {cores['vermelho']}NÃO PODEM{cores['limpa']} formar um triângulo!")