import turtle

def hexagono():

    for i in range(6):
        for i in range(3):
            turtle.forward(100)
            turtle.left(120)
        
        turtle.right(60)

turtle.hideturtle()
print(hexagono())
turtle.exitonclick()