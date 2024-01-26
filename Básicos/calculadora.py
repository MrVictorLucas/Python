#soma
def soma(x, y):
    return x + y

#subtração
def subt(x, y):
    return x - y

#multiplicação
def mult(x, y):
    return x * y

#divisão
def div(x, y):
    #Verificação para evitar uma divisão por zero
    if y != 0:
        return x/y
    else:
        return "Um número não pode ser dividido por 0"

#Recebendo os valores   
num1 = float(input("Digite um numero: "))
operacao = input("Escolha a operação ( +  -  *  / ) ")
num2 = float(input("Digite um numero: "))

#Estrutura
if operacao == "+":
    resultado = soma(num1, num2)
elif operacao == "-":
    resultado = subt(num1, num2)
elif operacao == "*":
    resultado = mult(num1, num2)
elif operacao == "/":
    resultado = div(num1, num2)
    
else:
    resultado = "Operação Inválida"
    
print(f"Resultado: {resultado}")