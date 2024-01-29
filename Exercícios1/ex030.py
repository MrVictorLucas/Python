# Ímpar ou Par
num = int(input("\033[33mDigite um número: \033[m"))
divisao = num%2
cores = {
    'limpa': "\033[m",
    'azul': "\033[36m",
    'vermelho': "\033[31m"
}

if divisao == 0:
    print(f"O número {num} é {cores['azul']}PAR{cores['limpa']}")
else:
    print(f"O número {num} é {cores['vermelho']}ÍMPAR{cores['limpa']}")