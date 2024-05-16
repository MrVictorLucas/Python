contador = soma = 0

while True:
    numero = int(input("Digite um número [999 para parar]: "))
    if numero==999:
        break
    contador+=1
    soma+=numero
print(f"Você digitou ao todo {contador} números.")
print(f"E a soma entre eles foi de {soma}.")