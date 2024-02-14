# Números Primos
cores={
    'limpa':"\033[m",
    'vermelho':"\033[31;1m",
    'azul':"\033[36;1m",
    'verde':"\033[32;1m",
    'amarelo':"\033[33;1m",
}

print(f"{cores['amarelo']}", "=="*20)
print(" "*7, "ANALISANDO UM NÚMERO PRIMO", ""*7)
print("=="*21, f"{cores['limpa']}")

num = int(input("Digite um número: "))
total=0

for c in range(1, num+1):
    if num%c==0:
        print(f"{cores['vermelho']}", end='')
        total+=1
    else:
        print(f"{cores['azul']}", end='')
    print(f"{c} ", end='')
    
print(f"{cores['limpa']}")
print(f"O número {num} foi divisível {total} vezes!")

if total==2:
    print(f"Logo, {cores['azul']}ELE É{cores['limpa']} um número {cores['verde']}PRIMO{cores['limpa']}")
else:
    print(f"Logo {cores['vermelho']}ELE NÃO É{cores['limpa']} um número {cores['verde']}PRIMO{cores['limpa']}")