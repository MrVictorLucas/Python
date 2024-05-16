maior = homens = mulheres = 0

while True:
    print("-"*30)
    print("     CADASTRE UMA PESSOA     ")
    print("-"*30)
    
    nome = str(input("Nome: ")).strip().upper()
    idade = int(input("Idade: "))
    if idade<0:
        idade = int(input("Idade Inválida! Tente Novamente. Idade: "))
    sexo = str(input("Sexo: [M/F] ")).strip().upper()
    if not sexo in "MF":
        sexo = str(input("Sexo Inválido! Tente novamente. Sexo: [M/F] "))
    
    if idade>=18:
        maior+=1
    if sexo == "M":
        homens+=1
    if sexo == "F" or idade<20:
        mulheres+=1
    
    resposta = str(input("Quer continuar? [S/N] ")).strip().upper()
    if not resposta in "SN":
        resposta = str(input("Resposta Inválida! Quer continuar? [S/N] ")).strip().upper()
    if resposta == "N":
        print(f"Total de pessoas com mais de 18 anos: {maior}.")
        if homens == 1:
            print(f"Ao todo temos {homens}")
        else:
            print(f"Ao todo temos {homens} homem cadastrado.")
        if mulheres == 1:
            print(f"E temos {mulheres} mulher com menos de 20 anos")
        else:
            print(f"E temos {mulheres} mulheres com menos de 20 anos")
        break
        