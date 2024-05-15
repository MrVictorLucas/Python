# Criando um Menu de Opções

pvalor = int(input("Digite o primeiro valor: "))
svalor = int(input("Digite o segundo valor: "))
opção = 0 

while opção != 5:
    
    print("=-="*10)
    print(" "*4, "[ 1 ] somar", " "*4)
    print(" "*4, "[ 2 ] multiplicar", " "*4)
    print(" "*4, "[ 3 ] maior", " "*4)
    print(" "*4, "[ 4 ] novos números", " "*4)
    print(" "*4, "[ 5 ] sair do programa", " "*4)
    print("=-="*10)
    
    opção = int(input(">>> Qual é sua opção? "))
    
    if opção==1:
        soma = pvalor+svalor
        print(f"A soma entre {pvalor} + {svalor} é igual a {soma}")
    elif opção==2:
        mult=pvalor*svalor
        print(f"A multiplicação entre {pvalor} x {svalor} é igual a {mult}")
    elif opção==3:
        if pvalor>svalor:
            print(f"Entre {pvalor} e {svalor} o maior valor é {pvalor}")
        elif pvalor<svalor:
            print(f"Entre {pvalor} e {svalor} o maior valor é {svalor}")
        elif pvalor==svalor:
            print("Ambos os valores são iguais")
    elif opção==4:
        pvalor = int(input("Digite o primeiro valor: "))
        svalor = int(input("Digite o segundo valor: "))
    elif opção==5:
        print("Até mais!")
    else:
        print("Opção não encontrada, tente novamente... ")