def verifica_primo(numero):
    # Um número menor ou igual a 1 não é primo
    if numero <= 1:
        return False
    # Verifica se o número é divisível por algum outro número de 2 até o número - 1
    for i in range(2, numero):
        if numero % i == 0:
            return False

    # Se não foi encontrado nenhum divisor, o número é primo
        else:
            return True

# Solicita ao usuário um número
numero_usuario = int(input("Digite um número inteiro: "))

# Verifica se o número é primo e exibe o resultado
if verifica_primo(numero_usuario):
    print(f"{numero_usuario} é um número primo.")
else:
    print(f"{numero_usuario} não é um número primo.")