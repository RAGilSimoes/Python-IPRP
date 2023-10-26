import turtle
import random

turtle.speed(1)

dimensao = int(input("Introduza a dimensão da grelha: "))
numero = dimensao / 8
numero_inteiro = int(numero)
numero_valido = dimensao % 8
conta_inteira = int(numero)
avanco = numero % 1

def quadrado(dimensao, numero_inteiro,conta_inteira):
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
        quadrado(dimensao, numero_inteiro, conta_inteira)

turtle.exitonclick()
