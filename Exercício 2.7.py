import turtle

turtle.circle(100, None, None)


turtle.penup()
turtle.setposition(-50,125)
turtle.pendown()
turtle.fillcolor(0,0,0)
turtle.begin_fill()
turtle.circle(15, None, None)
turtle.end_fill()

turtle.penup()
turtle.setposition(50,125)
turtle.pendown()
turtle.fillcolor(0,0,0)
turtle.begin_fill()
turtle.circle(15, None, None)
turtle.end_fill()

turtle.penup()
turtle.setposition(-45, 50)
turtle.setheading(-25)
turtle.pendown()
turtle.circle(100,55)

turtle.hideturtle()

turtle.exitonclick()