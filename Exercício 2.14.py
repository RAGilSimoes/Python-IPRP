import turtle

turtle.penup()
turtle.setposition(-120, 120)

for i in range(5):
    turtle.pendown()
    turtle.setheading(-90)
    turtle.forward(200 - 40*i)
    turtle.left(90)
    turtle.forward(200 - 40*i)
    turtle.left(90)
    turtle.forward(200 - 40*i)
    turtle.left(90)
    turtle.forward(200 - 40*i)
    
    turtle.penup()
    turtle.setposition(-100 + 20*i, 100 - 20*i)

turtle.hideturtle()
turtle.exitonclick()