import turtle
from turtle import Screen

Screen().bgcolor("blue")

turtle.color("red")
turtle.shape("turtle")
turtle.shapesize(0.5)
turtle.penup()

for i in range(36):
    turtle.forward(i + 10)
    turtle.right(20)
    turtle.stamp()


turtle.exitonclick()
