import turtle
import math

tamanho_quadrado = int(input("Introduz o tamanho do lado do quadrado: "))

x = tamanho_quadrado/2
y = tamanho_quadrado/2

diagonal = math.sqrt(x**2 + y**2)

head = 0

def quadrado(tamanho_quadrado,x,y):
    turtle.penup()
    turtle.setposition(-x,y)
    turtle.pendown()
    for i in range(4):
        turtle.forward(tamanho_quadrado)
        turtle.right(90)
        
def triangulo(tamanho_quadrado,x,y,head, diagonal):
    turtle.penup()
    turtle.setposition(x,y)
    turtle.setheading(head)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    
    turtle.forward(tamanho_quadrado)
    turtle.right(135)
    turtle.forward(diagonal)
    turtle.right(90)
    turtle.forward(diagonal)
    turtle.end_fill()


quadrado(tamanho_quadrado,x,y)
triangulo(tamanho_quadrado, -x, y, 0, diagonal)
triangulo(tamanho_quadrado, x, -y, 180, diagonal)

turtle.exitonclick()