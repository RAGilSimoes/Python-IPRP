import turtle
import random

tartaruga1 = turtle.Turtle()
tartaruga2 = turtle.Turtle()
tartaruga3 = turtle.Turtle()

formas = ["arrow", "turtle", "circle", "square", "triangle", "classic"]

tartaruga1.shape(random.choice(formas))
tartaruga2.shape(random.choice(formas))
tartaruga3.shape(random.choice(formas))

tartaruga1.forward(100)

tartaruga2.setheading(180)
tartaruga2.forward(100)

tartaruga3.setheading(90)
tartaruga3.forward(100)

turtle.exitonclick()