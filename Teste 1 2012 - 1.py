import math

raio = int(input("Introduz o valor do raio da circunferência: "))

angulo = (360/5)/2

hipotenusa = raio / math.cos(angulo)

metade_lado = math.sin(angulo) * hipotenusa

lado_pentagono = metade_lado * 2

print("Para uma circunferência de raio ", raio, ", o lado do pentágono inscrito vai ter ", lado_pentagono, " de tamanho.")