# Analisando um Triângulo v1.0
cores = {
    'limpa':"\033[m", 
    'amarelo':"\033[33;1m", 
    'azul':"\033[36;1;40m", 
    'vermelho':"\033[31;1;40m"
}
print(f"{cores['amarelo']}-=-{cores['limpa']}"*20)
print(f"{cores['azul']}Analisador de Triângulos{cores['limpa']}")
print(f"{cores['amarelo']}-=-{cores['limpa']}"*20)

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1<(r2+r3) and r2<(r1+r3) and r3<(r1+r2):
    print(f"Os segmentos acima {cores['azul']}PODEM FORMAR{cores['limpa']} um triângulo!")
else:
    print(f"Os segmentos acima {cores['vermelho']}NÃO PODEM FORMAR{cores['limpa']} um triângulo!")