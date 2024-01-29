# Maior e menor valores

cores = {
    'limpa':"\033[m", 
    'azul':"\033[36;1;40m", 
    'vermelho':"\033[31;1;40m"
}
num1 = int(input("Primeiro valor: "))
num2 = int(input("Segundo valor: "))
num3 = int(input("Terceiro valor: "))

# Verificando o menor número
if num1<num2 and num1<num3:
    menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3
    
# Verificando o maior número
if num1>num2 and num1>num3:
    maior = num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3
    
print(f"O {cores['vermelho']}menor número{cores['limpa']} digitado foi {menor}")
print(f"O {cores['azul']}maior número{cores['limpa']} digitado foi {maior}")