import math

print("Introduz a altura do cone:")
altura = float(input())

print("Introduz o raio da base:")
raio = float(input())

volume_cone = (math.pi * (raio**2) * altura) / 3

print("O volume do cone é: ", round(volume_cone, 2))