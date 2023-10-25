import turtle
import math

arco = (60 * 125 * math.pi)/180 - 8
head = 0

def quadrado():
    turtle.fillcolor("yellow")
    turtle.penup()
    turtle.setposition(-150,150)
    turtle.setheading(-90)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(300)
        turtle.left(90)
    turtle.end_fill()
    
def triangulo(head):
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.penup()
    turtle.setposition(0,0)
    turtle.setheading(head)
    turtle.pendown()
    turtle.forward(125)
    turtle.left(90)
    turtle.circle(arco,60)
    turtle.setposition(0,0)
    turtle.end_fill()
    
def circulo():
    turtle.width(2)
    turtle.color("yellow")
    turtle.fillcolor("black")
    turtle.penup()
    turtle.setposition(-30,0)
    turtle.setheading(-90)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

quadrado()
triangulo(0)
triangulo(120)
triangulo(240)
circulo()

turtle.hideturtle()
turtle.exitonclick()