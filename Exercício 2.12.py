import turtle

turtle.fillcolor("lime")
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()

turtle.fillcolor("red")
turtle.begin_fill()
for i in range(3):
    turtle.forward(100)
    turtle.left(120)
turtle.end_fill()

turtle.forward(100)
turtle.left(120)
turtle.forward(60)
turtle.right(30)
turtle.fillcolor("black")
turtle.begin_fill()
turtle.forward(30)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(10)
turtle.left(30)
turtle.forward(10)
turtle.end_fill()

turtle.hideturtle()
turtle.exitonclick()