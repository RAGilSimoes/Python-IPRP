import math

print("Introduz o número de objetos n: ")
n = float(input())

print("Introduz o número de objetos m: ")
m = float(input())

todos = n + m

proporcao_n = n / todos
proporcao_m = m / todos

somatorio = -((proporcao_n * math.log2(proporcao_n)) + (proporcao_m * math.log2(proporcao_m)))

print("A desordem do conjunto é: ", somatorio)