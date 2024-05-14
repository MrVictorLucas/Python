#Analisador Completo

idadevelho = 0
nomevelho = ''
mulher20 = 0
médiaidade = 0
idadetotal = 0
 
for pessoa in range(1, 5):
    print(f"-----{pessoa}° PESSOA -----")
    
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    
    idadetotal+=idade
    
    if sexo in 'Mm' and idade>idadevelho:
        idadevelho=idade
        nomevelho=nome
        
    if sexo in 'Ff' and idade<20:
        mulher20+=1
            
médiaidade=idadetotal/4

print("")
print(f"A média de idades do grupo é de {médiaidade} anos")
print(f"O homem mais velho tem {idadevelho} anos e se chama {nomevelho}")
print(f"Ao todo são {mulher20} mulheres com menos de 20 anos")