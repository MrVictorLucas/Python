# Tratando vários valores v1.0
numeros = 0
contador = 0
soma = 0

while numeros != 999:
    numeros = int(input("Digite um número [999 para parar]: "))
    if numeros != 999:
        contador+=1
        soma+=numeros
        
print(f"Você digitou {contador} números e a soma entre eles foi {soma}.")