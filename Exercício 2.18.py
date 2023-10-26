import turtle

raio = 0
x = 0
y = 0
cor = ""
angulo = 0
head = 0

def circulo_grande():
    turtle.penup()
    turtle.setposition(-150,0)
    turtle.pendown()
    turtle.setheading(-90)
    turtle.circle(150)

    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(150,180)
    turtle.left(90)
    turtle.forward(300)
    turtle.end_fill()

def circulo_pequeno(x, y, raio, cor, angulo,head):
    turtle.penup()
    turtle.setposition(x,y)
    turtle.pendown()
    turtle.setheading(head)
    turtle.fillcolor(cor)
    turtle.begin_fill()
    turtle.circle(raio,angulo)
    turtle.end_fill()

circulo_grande()
circulo_pequeno(0,0,75,"black",180,90)
circulo_pequeno(0,0,75,"white",180,-90)
circulo_pequeno(-60,0,15,"white",360,90)
circulo_pequeno(60,0,15,"black",360,-90)

turtle.hideturtle()
turtle.exitonclick()