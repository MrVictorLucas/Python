# Alistamento Militar
from datetime import date
cores = {
    'limpa':"\033[m", 
    'vermelho':"\033[31;1m", 
    'azul':"\033[36;1m", 
    'amarelo':"\033[33;1m", 
    'verde':"\033[32;1m"
}
print(f"{cores['amarelo']}-=-{cores['limpa']}"*20)
print(f"{cores['verde']}ALISTAMENTO MILITAR{cores['limpa']}")
print(f"{cores['amarelo']}-=-{cores['limpa']}"*20)

ano_atual = date.today().year
nascimento = int(input("Ano de nascimento: "))
idade = (ano_atual-nascimento)

print(f"Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}")
if idade==18:
    print(f"Você {cores['vermelho']}DEVE{cores['limpa']} se alistar {cores['vermelho']}IMEDIATAMENTE!{cores['limpa']}")
    
elif idade<18:
    saldo=(18-idade)
    print(f"Você não tem 18 anos. Ainda faltam {saldo} anos para o alistamento")
    ano=(ano_atual+saldo)
    print(f"Seu alistamento {cores['azul']}SERÁ EM {ano}{cores['limpa']}")
    
elif idade>18:
    saldo=(idade-18)
    print(f"Você já deveria ter se alistado há {saldo} anos")
    ano=(ano_atual-saldo)
    print(f"Seu alistamento {cores['azul']}FOI EM {ano}{cores['limpa']}")