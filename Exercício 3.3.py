import math

print("Introduza o ângulo que a escada faz com o solo: ")
ang_graus = float(input())

ang_radianos = (math.pi / 180) * ang_graus

alt = math.cos(ang_radianos)

comp = alt / math.sin(ang_radianos)

print("A escada tem um comprimento de ", comp)