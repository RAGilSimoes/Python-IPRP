import turtle

turtle.width(5)

def circulos(x,y,cor):
    turtle.color(cor)
    turtle.penup()
    turtle.setposition(x,y) 
    turtle.pendown()
    turtle.circle(120)

circulos(-250,0,"blue")
circulos(0,0,"black")
circulos(250,0,"red")
circulos(-125,-120,"yellow")
circulos(125,-120,"lime")

turtle.exitonclick()