# Sequência de Fibonacci v1.0

print("-=-"*10)
print("Sequência de Fibonacci")
print("-=-"*10)

sequencia = int(input("Quantos termos você quer que sejam exibidos?" ))
t1 = 0
t2 = 1
contador = 3

print("~~~"*30)
print(f"{t1} --> {t2}", end="")
while contador<=sequencia:
    t3 = t1+t2
    print(f" --> {t3}", end="")
    t1 = t2
    t2 = t3
    contador+=1
print(" --> FIM")
print("~~~"*30) 