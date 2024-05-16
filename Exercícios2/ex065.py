# Maior e Menor valores

numero = int(input("Digite um número: "))
resposta = str(input("Quer continuar? [S/N] ")).upper().strip()
contador = 1
media = maior = menor = 0

soma = numero

while resposta != 'N':
    if resposta != 'S' and resposta != 'N':
        resposta = str(input("Resposta inválida... Quer continuar? [S/N] ")).strip().upper()
    else:
        if resposta == 'S':
            if contador == 1:
                maior = menor = numero
            else:
                if numero>maior:
                    maior=numero
                if numero<menor:
                    menor=numero
            contador+=1
            numero = int(input("Digite um número: "))
            soma+=numero
        resposta = str(input("Quer continuar? [S/N] ")).upper().strip()
    
media = soma/contador      
print(f"Você digitou {contador} números e a média foi {float(media):.2f}.")
print(f"O maior valor foi {maior} e o menor foi {menor}")