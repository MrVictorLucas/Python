# Contagem Regressiva
from time import sleep
cores={
    'limpa':"\033[m",
    'azul':"\033[36;1m"
}
for c in range(10, 0, -1):
    print(f"{c}!")
    sleep(1)
print(f"🎆🎆🎆{cores['azul']}FELIZ ANO NOVO!!!{cores['limpa']}🎆🎆🎆")