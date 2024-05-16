total = caros =  barato = contador = 0
nomebarato = ''

while True:
    print("-=-"*8)
    print("     SUPER MERCADO     ")
    print("-=-"*8)

    produto = str(input("Nome do Produto: ")).strip().lower()
    preco = float(input("Preço: R$"))
    contador+=1
    
    total+=preco
    if preco>1000:
        caros+=1
    if contador == 1:
        barato=preco
        nomebarato=produto
    else:
        if preco<barato:
            barato=preco
            nomebarato=produto
        
    resposta = str(input("Quer continuar? [S/N] ")).strip().upper()
    if not resposta in "SN":
        resposta = str(input("Resposta Inválida! Quer continuar? [S/N] ")).strip().upper()
    if resposta in "Nn":
        print(f"Valor total gasto: R${total:.2f}")
        print(f"Produtos com valor acima de R$1000: {caros}")
        print(f"O produto {nomebarato} tem o menor valor, custando R$ {barato:.2f}")
        print("TENHA UM ÓTIMO DIA!!!")
        break