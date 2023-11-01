import math

raio = int(input("Introduz o raio da circunferência: "))
lado = int(input("Introduz o tamanho do lado do quadrado: "))

if raio <= lado/2:
    print("O círculo está todo dentro do quadrado.")
else:
    print("O círculo não está todo dentro do quadrado.")