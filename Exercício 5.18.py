import turtle

turtle.speed(100)

dimensao = int(input("Introduza a dimensão da grelha: "))
celula = int(input("Introduza a dimensão de cada célula da grelha: "))
conta = dimensao/celula
conta_inteira = int(conta)
avanco = conta % 1

if (avanco != 0):
    print("Medidas inválidas. ")
    
else: 
    turtle.penup()
    turtle.setposition(-(dimensao/2), dimensao/2)
    turtle.pendown()

    for i in range(4):
        turtle.forward(dimensao)
        turtle.right(90)
    
    for i in range(conta_inteira):
        turtle.forward(celula)
        turtle.right(90)
        turtle.forward(dimensao)
        turtle.back(dimensao)
        turtle.left(90)

    turtle.right(90)

    for i in range(conta_inteira):
        turtle.forward(celula)
        turtle.right(90)
        turtle.forward(dimensao)
        turtle.back(dimensao)
        turtle.left(90)

turtle.exitonclick()