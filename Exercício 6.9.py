import turtle as t
import random

n = int(input("Introduz o tamanho da sequência: "))
lista_comandos = ["A", "E", "R", "D"]
lista_comandos_chamados = []
movimento = ""

def gera_comandos(n, lista_comandos, lista_comandos_chamados):
    for i in range(n):
        movimento = random.choice(lista_comandos)
        lista_comandos_chamados = lista_comandos_chamados + [movimento]
    return lista_comandos_chamados

def navega(lista_comandos_chamados, tartaruga):
    t.shape("circle")
    t.color("lime")
    t.stamp()
    t.color("black")
    for i in lista_comandos_chamados:
        if i == "A":
            t.forward(50)
        elif i == "E":
            t.left(90)
        elif i == "D":
            t.right(90)
        elif i == "R":
            t.back(50)
    t.color("red")
    t.stamp()
    


def main_tarta(n):
    tartaruga = t.Turtle()
    comandos = gera_comandos(n, lista_comandos, lista_comandos_chamados)
    navega(comandos, tartaruga)
    t.exitonclick()
    
main_tarta(n)