# Aquele clássico de Média
cores = {
    'limpa':"\033[m", 
    'vermelho':"\033[31;1m",
    'azul':"\033[36;1m", 
    'amarelo':"\033[33;1m", 
    'roxo':"\033[35;1m"
}
print(f"{cores['roxo']}-=-{cores['limpa']}"*20)
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
print(f"{cores['roxo']}-=-{cores['limpa']}"*20)
média = (nota1+nota2)/2

print(f"Tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {média:.1f}")
if média<5:
    print(f"O aluno está {cores['vermelho']}REPROVADO{cores['limpa']}")
elif média>=5 and média<7:
    print(f"O aluno está de {cores['amarelo']}RECUPERAÇÃO{cores['limpa']}")
elif média>=7:
    print(f"O aluno está {cores['azul']}APROVADO{cores['limpa']}!")