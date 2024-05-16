print("-=-"*15)
print(f"{'BANCO MRV':^45}")
print("-=-"*15)

saque = int(input("Qual valor você deseja sacar? R$"))
total = saque
nota = 200
totalnotas = 0

while True:
    if total>=nota:
        total-=nota
        totalnotas+=1
    else:
        if totalnotas>0:
            print(f"Total de {totalnotas} cédulas de R${nota}")
        if nota == 200:
            nota=100
        elif nota == 100:
            nota=50
        elif nota == 50:
            nota=20
        elif nota == 20:
            nota=10
        elif nota == 10:
            nota=5
        elif nota == 5:
            nota=1
        totalnotas=0
        if total == 0:
            break
print("-=-"*15)
print(f"{'VOLTE SEMPRE AO BANCO MRV':^45}")
print("-=-"*15)