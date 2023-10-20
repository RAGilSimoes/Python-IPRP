import turtle
import random

x = int(input("Introduza o número de passeios que quer fazer: "))
r = float(random.randint(0,255))
g = float(random.randint(0,255))
b = float(random.randint(0,255))
avanco = float(random.randint(0,100))
head = float(random.randint(0,360))

def passeios(x, r, g, b, avanco, head):
    for i in range(x):
        turtle.color(r, g, b)
        turtle.forward(avanco)
        turtle.setheading(head)

print(passeios(x, r, g, b, avanco, head))    
turtle.exitonclick()