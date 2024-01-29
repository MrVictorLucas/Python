# Custo da Viagem
cores = {
    'limpa': "\033[m",
    'azul': "\033[1;36;40m"
}
distancia = float(input("Qual é a distância da sua viagem em Km? "))

print(f"Você está prestes a começar uma viagem de {cores['azul']}{distancia:.1f}Km.{cores['limpa']}")
if distancia<=200:
    print(f"E o preço da sua passagem será de {cores['azul']}R${(distancia*0.50):.2f}{cores['limpa']}")
else:
    print(f"E o preço da sua passagem será de {cores['azul']}R${(distancia*0.45):.2f}{cores['limpa']}")