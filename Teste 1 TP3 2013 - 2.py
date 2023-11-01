import turtle as t

t.speed(10)

lado_maior = int(input("Introduz o tamanho do maior lado do retângulo: "))
lado_menor = int(input("Introduz o tamanho do menor lado do retângulo: "))

def quadrados(lado_maior, lado_menor):

    for i in range(16):
        t.fillcolor("red")
        t.begin_fill()

        t.setheading(90 - 22.5*i)
        for i in range(2):
            t.forward(lado_maior)
            t.right(90)
            t.forward(lado_menor)
            t.right(90)
        t.end_fill()

quadrados(lado_maior, lado_menor)
t.hideturtle()
t.exitonclick()