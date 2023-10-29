import turtle
import random

turtle.speed(50)
turtle.bgcolor("black")

dimensao = int(input("Introduza a dimensão da grelha: "))
tamanhoCasa = dimensao // 8
tamanhoInvalido = dimensao % 8

def quadrado(dimensao, tamanhoCasa):
    turtle.color("white")
    turtle.penup()
    turtle.setposition(-(dimensao/2), dimensao/2)
    turtle.pendown()

    #Desenha Quadrado
    for i in range(4):
        turtle.forward(dimensao)
        turtle.right(90)

    #Desenha Colunas
    for i in range(8):
        turtle.forward(tamanhoCasa)
        turtle.right(90)
        turtle.forward(dimensao)
        turtle.back(dimensao)
        turtle.left(90)

    #Pivot
    turtle.right(90)

    #Desenha Linhas
    for i in range(8):
        turtle.forward(tamanhoCasa)
        turtle.right(90)
        turtle.forward(dimensao)
        turtle.back(dimensao)
        turtle.left(90)

def posicaoInicial():
    turtle.penup()
    turtle.setposition(0,0)
    turtle.pendown()
    turtle.width(1)
    turtle.color("red")
    turtle.shape("circle")
    turtle.stamp()
    turtle.shape("classic")

def andar(tamanhoCasa):
    numeroDeslocacoes = random.randint(50,100)
    maxX = maxY = dimensao // 2
    minX = minY = -maxX

    passos = 0
    while (passos < numeroDeslocacoes ):
        direcao = random.randint(0,3)
        turtle.setheading(direcao * 90)
        xFinal = 0
        yFinal = 0

        if (direcao == 0):
            xFinal = turtle.xcor() + tamanhoCasa
        elif (direcao == 2):
            xFinal = turtle.xcor() - tamanhoCasa
        elif (direcao == 1):
            yFinal = turtle.ycor() + tamanhoCasa
        elif (direcao == 3):
            yFinal = turtle.ycor() - tamanhoCasa

        if (xFinal <= maxX and xFinal >= minX and yFinal <= maxY and yFinal >= minY ):
            turtle.forward(tamanhoCasa)
            passos+= 1

        print(turtle.position())


if (tamanhoInvalido != 0):
    print("Não é possível efetuar a grelha. ")
else:
    quadrado(dimensao, tamanhoCasa)
    posicaoInicial()
    andar(tamanhoCasa)

turtle.exitonclick()