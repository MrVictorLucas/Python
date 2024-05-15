sexo = str(input("Informe seu sexo [M/F]: ")).upper().strip()

while not sexo == 'M' and not sexo == 'F':
    print("Error!")
    sexo = str(input("Informe novamente seu sexo [M/F]: "))
    
print(f"Sexo {sexo} registrado com sucesso")