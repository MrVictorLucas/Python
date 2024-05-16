while True:
    numero = int(input("Quer ver a tabuado de qual valor? "))
    if numero<0:
        print("PROGRAMA ENCERRADO. Tenha um bom dia!")
        break
    print("-=-"*8)
    for contador in range(1, 11):
        print(f"{numero} X {contador} = {numero*contador}")
    print("-=-"*8)