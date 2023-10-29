import math 

v = float(input("Introduz a velocidade da descolagem: "))
a = float(input("Introduz a aceleração da descolagem: "))

c = (v**2)/(2*a)

print("Velocidade de descolagem (m/s): %d" % (v))
print("Aceleração para descolagem (m/s²): %.1f " % (a))
print("Para a velocidade %d e aceleração %.1f o comprimento da pista é: %.2f" % (v,a,c))