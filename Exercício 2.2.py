import turtle

lados = 5 #int(input("Introduza o número de lados: "))
avanco = 100 #int(input("Introduza a quantidade de avanços da tartaruga: "))
angulo = 144 #float(input("Introduza o ângulo de rotação: "))
a = 10
turtle.setposition(0.0, 0.0)
turtle.speed(10)

for i in range(100):
    a += 10
    turtle.forward(avanco + a)
    turtle.left(angulo)
    
turtle.exitonclick()