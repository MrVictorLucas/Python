# Conversor de Bases Numéricas
cores = {
    'limpa':"\033[m", 
    'azul':"\033[36;1;40m", 
    'vermelho':"\033[31;1;40m",
    'verde':"\033[32;1;40m", 
    'amarelo':"\033[33;1;40m"
}
print(f"{cores['amarelo']}-=-{cores['limpa']}"*20)
print(f"{cores['azul']}Conversor de Bases Numéricas{cores['limpa']}")
print(f"{cores['amarelo']}-=-{cores['limpa']}"*20)

num = int(input("Digite um número inteiro: "))
conversão = int(input(f'''Escolha uma das bases para conversão:
[ 1 ] converter para {cores['azul']}BINÁRIO{cores['limpa']}
[ 2 ] converter para {cores['verde']}OCTAL{cores['limpa']}
[ 3 ] converter para {cores['vermelho']}HEXADECIMAL{cores['limpa']}
Sua opção: '''))

if conversão==1:
    print(f"{num} convertido para {cores['azul']}BINÁRIO{cores['limpa']} é igual a {bin(num)[2:]}")
elif conversão==2:
    print(f"{num} convertido para {cores['verde']}OCTAL{cores['limpa']} é igual a {oct(num)[2:]}")
elif conversão==3:
    print(f"{num} convertido para {cores['vermelho']}HEXADECIMAL{cores['limpa']} é igual a {hex(num)[2:]}")
else:
    print(f"{cores['amarelo']}Opção Inválida! Tente novamente.{cores['limpa']}")