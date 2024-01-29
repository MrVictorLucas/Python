# Radar Eletrônico
velocidade = int(input("Qual é a velocidade atual do veículo? "))
multa = float(velocidade-80)*7
if velocidade > 80:
    print("\033[1;31mMULTADO! Você excedeu o limite permitido de 80Km/h\033[m")
    print(f"Você deve pagar uma multa de R${multa:.2f}!")
else:
    print("\033[1;32mMuito bem! Você está dentro do limite de velocidade respeitando a via, continue assim!\033[m")
    
print("\033[1;36mTenha um bom dia! Dirija com segurança!\033[m")