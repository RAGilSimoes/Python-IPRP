import math

print("Introduz a abcissa das coordenadas cartesianas:")
x = float(input())

print("Introduz a ordenada das coordenadas cartesianas:")
y = float(input())

r = math.sqrt((x**2)+(y**2))

teta = math.acos(x/r)

print("As coordenadas polares são: ", r, " e ",teta)