def verificapalindromo(palavra):

    #Formata o texto para inverter
    palavra = palavra.replace(" ", "").lower()
    
    #Compara a palavra com a inversão
    return palavra == palavra[::-1]

palavrausuario = input("Digite uma palavra: ")

#Estrutura
if verificapalindromo(palavrausuario):
    print(f"{palavrausuario} é um palíndromo")
else:
    print(f"{palavrausuario} não é um palíndromo")