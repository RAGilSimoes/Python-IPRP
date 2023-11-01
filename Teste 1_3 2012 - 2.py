lado1 = int(input("Introduz o lado do triângulo: "))
lado2 = int(input("Introduz o lado do triângulo: "))
lado3 = int(input("Introduz o lado do triângulo: "))

if ((lado1 == lado2) and (lado2 == lado3)):
    print("O triângulo é equilátero.")
elif ((lado1 == lado2) and (lado2 != lado3)):
    print("O triângulo é isósceles.")
elif ((lado1 != lado2) and (lado2 != lado3) and (lado1 != lado3)):
    print("O triângulo é escaleno.")
    