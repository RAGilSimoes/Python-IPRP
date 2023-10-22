import turtle
import random
from turtle import Screen

Screen = Screen()

Screen.colormode(255)

x = int(input("Introduza o número de passeios que quer fazer: "))
r = 0
g = 0
b = 0
avanco = 0
head = 0

def passeios(x, r, g, b, avanco, head):
    for i in range(x):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        avanco = float(random.randint(0,200))
        head = float(random.randint(0,360))
        turtle.color(r, g, b)
        turtle.forward(avanco)
        turtle.setheading(head)

passeios(x, r, g, b, avanco, head)   
turtle.exitonclick()