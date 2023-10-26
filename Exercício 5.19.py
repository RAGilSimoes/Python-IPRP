import turtle
import random

turtle.speed(50)

dimensao = int(input("Introduza a dimensão da grelha: "))
numero = dimensao / 8
numero_inteiro = int(numero)
numero_valido = dimensao % 8
conta_inteira = int(numero)
avanco = numero % 1

def quadrado(dimensao, numero_inteiro):
    turtle.penup()
    turtle.setposition(-(dimensao/2), dimensao/2)
    turtle.pendown()

    for i in range(4):
        turtle.forward(dimensao)
        turtle.right(90)
    
    for i in range(8):
        turtle.forward(numero_inteiro)
        turtle.right(90)
        turtle.forward(dimensao)
        turtle.back(dimensao)
        turtle.left(90)

    turtle.right(90)

    for i in range(8):
        turtle.forward(numero_inteiro)
        turtle.right(90)
        turtle.forward(dimensao)
        turtle.back(dimensao)
        turtle.left(90)

if (avanco != 0):
        print("Medidas inválidas. ")
else:
    if (numero_valido != 0):
        print("Não é possível efetuar a grelha. ")
    else:
        quadrado(dimensao, numero_inteiro)

def posicao():        
    turtle.penup()
    turtle.setposition(0,0)
    turtle.pendown()
    turtle.width(1)
    turtle.color("red")
    turtle.shape("circle")
    turtle.stamp()
    turtle.shape("classic")

def andar(numero_inteiro):
    numero = random.randint(1,100)
    for i in range(numero):
        direcao = random.randint(1,4)

        if direcao == 1:
            turtle.setheading(0)
        elif direcao == 2:
            turtle.setheading(90)
        elif direcao == 3:
            turtle.setheading(180)
        elif direcao == 4:
            turtle.setheading(270)

        turtle.forward(numero_inteiro)
        
        print(turtle.position())
        #este
        if (turtle.position() > (-(dimensao/2), -dimensao/2)):
            print("olá")
        if (turtle.position() > (-(dimensao/2), dimensao/2)):
            print("adeus")
        if (turtle.position() > ((dimensao/2), -dimensao/2)):
            print("até")
        if (turtle.position() > (-(dimensao/2), dimensao/2)):
            print("logo")
        #verificar este bloco
        
posicao()    
andar(numero_inteiro)

turtle.exitonclick()
