import turtle as t
import random

def criar_e_gerar_pares_de_numeros():
    with open("ficheiro_novo","w") as novo:
        for i in range(50):
            numero1 = str(random.randint(1,6))
            numero2 = str(random.randint(1,6))
            par = numero1 + numero2
            
            novo.write(par)
            novo.write("\n")
            
def criar_imagem():
    ficheiro = open("ficheiro_novo","r")
    for i in range(25):
        linha1 = ficheiro.readline()
        linha2 = ficheiro.readline()
        x = int(linha1)
        y = int(linha2)
    
        t.goto(x,y)
    t.exitonclick()
    
            
criar_e_gerar_pares_de_numeros()
criar_imagem()