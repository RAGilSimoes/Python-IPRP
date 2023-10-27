import turtle
from turtle import Screen

Screen().bgcolor("lightgreen")
turtle.color("red")

escrever = ""

def relogio(angulo,escrever):
    turtle.setheading(angulo)
    turtle.penup()
    turtle.forward(200)
    turtle.pendown()
    turtle.forward(25)
    turtle.penup()
    turtle.forward(50)
    fonte2 = ("Comic Sans", 20, "normal") #para escrever coisas
    turtle.write(escrever, False, "left", fonte2)
    turtle.penup()
    turtle.setposition(0,0)
        
relogio(0,"3")
relogio(30,"2")
relogio(60,"1")
relogio(90,"12")
relogio(120,"11")
relogio(150,"10")
relogio(180,"9")
relogio(210,"8")
relogio(240,"7")
relogio(270,"6")
relogio(300,"5")
relogio(330,"4")

turtle.exitonclick()