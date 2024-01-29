# Cálculando o Seno, Cos e Tan
from math import sin, cos, tan, radians

ang = float(input("Digite o ângulo que você deseja: "))
seno = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print(f"O ângulo de {ang:.0f}° tem o SENO de {seno:.2f}")
print(f"O ângulo de {ang:.0f}° tem o COSSENO de {cos:.2f}")
print(f"O ângulo de {ang:.0f}° tem a TANGENTE de {tan:.2f}")