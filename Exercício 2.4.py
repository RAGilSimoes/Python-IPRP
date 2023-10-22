import turtle 

raio = int(input("Introduz o raio da figura: "))
lados = int(input("Introduz o tamanho dos lados: "))
num_lados = int(input("Introduz o número de lados: "))

def poligono(raio,lados,num_lados):
    for i in range(num_lados):
        turtle.forward(raio)
        turtle.forward(lados)
        turtle.left(360/num_lados)
        
poligono(raio, lados, num_lados)
turtle.exitonclick()