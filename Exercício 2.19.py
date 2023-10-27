import turtle

turtle.speed(25)

x = 0
y = 0
cor = ""

def grelha():
    turtle.width(5)

    turtle.penup()
    turtle.back(200)
    turtle.goto(-225,75)
    turtle.pendown()
    turtle.forward(450)

    turtle.penup()
    turtle.back(200)
    turtle.goto(-225,-75)
    turtle.pendown()
    turtle.forward(450)

    turtle.penup()
    turtle.goto(-75,-225)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(450)

    turtle.penup()
    turtle.goto(75,-225)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(450)

def circulo(x, y,cor):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(cor)
    turtle.fillcolor(cor)
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()

grelha()
circulo(-100,150,"black")
circulo(50,150,"black")
circulo(200,150,"black")
circulo(-100,0,"black")
circulo(50,0,"black")
circulo(200,0,"black")
circulo(-100,-150,"black")
circulo(50,-150,"black")
circulo(200,-150,"black")

def jogada():
    for i in range(9):
        jogador = int(input("Qual vai ser o primeiro jogador? "))
        if (jogador < 1) and (jogador > 2):
            print("Jogador inválido. ")
        else:    
            escolha = int(input("Introduz a posição da jogada (de 1 a 9): "))
            if (escolha < 1) and (escolha > 9):
                print("Valores inválidos.")
            else:
                if (jogador == 1):
                    cor = "red"
                    if (escolha == 1):
                        circulo(-100,150,cor)
                    if (escolha == 2):
                        circulo(50,150,cor)
                    if (escolha == 3):
                        circulo(200,150,cor)
                    if (escolha == 4):
                        circulo(-100,0,cor)
                    if (escolha == 5):
                        circulo(50,0,cor)
                    if (escolha == 6):
                        circulo(200,0,cor)
                    if (escolha == 7):
                        circulo(-100,-150,cor)
                    if (escolha == 8):
                        circulo(50,-150,cor)
                    if (escolha == 9):
                        circulo(200,-150,cor)
                        
                if (jogador == 2):
                    cor = "green"
                    if (escolha == 1):
                        circulo(-100,150,cor)
                    if (escolha == 2):
                        circulo(50,150,cor)
                    if (escolha == 3):
                        circulo(200,150,cor)
                    if (escolha == 4):
                        circulo(-100,0,cor)
                    if (escolha == 5):
                        circulo(50,0,cor)
                    if (escolha == 6):
                        circulo(200,0,cor)
                    if (escolha == 7):
                        circulo(-100,-150,cor)
                    if (escolha == 8):
                        circulo(50,-150,cor)
                    if (escolha == 9):
                        circulo(200,-150,cor)
            
jogada()

turtle.exitonclick()