# Gerenciador de Pagamentos
cores = {
    'limpa':"\033[m",
    'vermelho:':"\033[31;1m",
    'azul':"\033[36;1m",
    'amarelo':"\033[33;1m",
    'verde':"\033[32;1m"
}
print(f"{cores['amarelo']}="*10, "LOJAS QUALQUER", "="*10, f"{cores['limpa']}")

preco = float(input(f"Preço das Compras: {cores['verde']}R${cores['limpa']} "))
pagamento = int(input('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinherio/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
Qual é a opção? '''))

if pagamento==1:
    total = preco-(preco*10/100)
elif pagamento==2:
    total = preco-(preco*5/100)
elif pagamento==3:
    total = preco
    parcelas = total/2
    print(f"Sua compra será parcelada em {cores['azul']}2x{cores['limpa']} de {cores['verde']}R${parcelas}{cores['limpa']} SEM JUROS")
elif pagamento==4:
    total = preco+(preco*20/100)
    parcelas = int(input("Quantas parcelas? "))
    parcela = total/parcelas
    print(f"Sua compra será parcelada em {cores['azul']}{parcelas}x{cores['limpa']} de {cores['verde']}R${parcela:.2f}{cores['limpa']} COM JUROS")
else:
    total = preco
    print(f"{cores['vermelho:']}OPÇÃO DE PAGAMENTO INVÁLIDA{cores['limpa']}. Tente novamente!")
    
print(f"Sua compra de {cores['verde']}R${preco:2f}{cores['limpa']} vai custar {cores['verde']}R${total:.2f}{cores['limpa']} no final.")