import turtle
from turtle import Screen

Screen().bgcolor("lightgreen")
turtle.color("red")

angulo = 0

def relogio(angulo):
    for i in range(12):
        turtle.setheading(angulo)
        turtle.penup()
        turtle.forward(250)
        turtle.pendown()
        turtle.forward(25)
        turtle.penup()
        turtle.setposition(0,0)
        angulo += 30
        
relogio(angulo)

turtle.exitonclick()