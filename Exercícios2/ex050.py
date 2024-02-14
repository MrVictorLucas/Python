# Soma dos pares
cores={
    'limpa':"\033[m",
    'azul':"\033[36;1m"
}
soma=0
cont=0
for c in range(1, 7):
    num = int(input(f"Digite o  {c}° valor: "))
    if num%2==0:
        soma+=num
        cont+=1
print(f"Você informou {cores['azul']}{cont} números pares{cores['limpa']}, e a soma deles é {cores['azul']}{soma}{cores['limpa']}!")