import math

l = 7.62
d = 8.89
r = d/2


area_hamburguer_quadrado = l*l

area_hamburguer_redondo = math.pi * (r**2)

if area_hamburguer_redondo > area_hamburguer_quadrado:
    print("Pode reclamar com o design do novo hambúrguer")
else:
    print("Não precisa de reclamar com o design do novo hambúrguer")
    
