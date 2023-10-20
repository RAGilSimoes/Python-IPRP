import turtle

lados = int(input("Introduza o número de lados: "))
avanco = int(input("Introduza a quantidade de avanços da tartaruga: "))
angulo = float(input("Introduza o ângulo de rotação: "))

for i in range(lados):
    turtle.forward(avanco)
    turtle.left(angulo)
    
turtle.exitonclick()