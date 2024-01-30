# Classificando Atletas
from datetime import date

cores = {
    'limpa':"\033[m",
    'vermelho':"\033[31;1m",
    'verde':"\033[32;1m",
    'amarelo':"\033[33;1m",
    'azul':"\033[34;1m",
    'roxo':"\033[35;1m",
    'branco':"\033[7;30m",
    'azul_claro':"\033[36;1;40m"
}
ano_atual = date.today().year
print(f"{cores['azul_claro']}-=-"*20)
print(f"CONFEDERAÇÃO NACIONAL DE NATAÇÃO")
print(f"-=-"*20)
print(f"{cores['limpa']}")
nascimento = int(input("Ano de nascimento: "))
idade = (ano_atual-nascimento)


print(f"O atleta tem {idade} anos.")
if idade<0:
    print("Já é atleta dentro do saco do pai... Parabéns!")

elif idade<=9:
    print(f"Classificação: {cores['vermelho']}Mirim{cores['limpa']}")
elif idade>9 and idade<=14:
    print(f"Classificação: {cores['verde']}Infantil{cores['limpa']}")
elif idade>14 and idade<=19:
    print(f"Classificação: {cores['amarelo']}Junior{cores['limpa']}")
elif idade>19 and idade <=25:
    print(f"Classificação: {cores['azul']}Sênior{cores['limpa']}")
elif idade>25:
    print(f"Classificação: {cores['roxo']}Master{cores['limpa']}")