import turtle

angulo = 0
avanco = 0

def quadrados(angulo, avanco):
    for i in range(20):
        turtle.setheading(angulo)
        for i in range(4):
            turtle.forward(10+avanco)
            turtle.right(90)
        angulo += 10
        avanco += 10
    
quadrados(angulo, avanco)

turtle.exitonclick()