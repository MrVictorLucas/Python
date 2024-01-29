# Ano Bissexto
from datetime import date
cores = {
    'limpa': "\033[m", 
    'azul': "\033[36;1;40m", 
    'vermelho': "\033[31;1;40m"
}
ano = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year
    
if ano%4==0 and ano%100!=0 or ano%400==0:
    print(f"O ano {ano} é {cores['azul']}BISSEXTO{cores['limpa']}")
else:
    print(f"O ano {ano} {cores['vermelho']}NÃO{cores['limpa']} é {cores['vermelho']}BISSEXTO{cores['limpa']}")