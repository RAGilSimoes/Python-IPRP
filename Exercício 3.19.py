import random

ADN_comprimento = int(input("Introduz o comprimento do ADN que pretendes: "))

cadeia_adn = ""

adn = ("e", "f", "t", "d")
verificar_e = 0
verificar_d = 0
verificar_t = 0
verificar_f = 0

for i in range(ADN_comprimento):
    letra = random.choice(adn)
    if letra == "e":
        verificar_e += 1
    elif letra == "f":
        verificar_f += 1
    elif letra == "d":
        verificar_d += 1
    elif letra == "t":
        verificar_t += 1
        
    cadeia_adn = cadeia_adn + letra
    
print(cadeia_adn)
                     
for letra in cadeia_adn:
    if (verificar_e > 0) or (verificar_d > 0):
        rotacao = random.randint(0,360)
    
    if (verificar_t > 0) or (verificar_f > 0):
        deslocacao = random.randint(10,50)
        
    if (letra == "e"):
        print("A tartaruga vai rodar ", rotacao, " graus para a esquerda.")
    elif (letra == "f"):
        print("A tartaruga vai andar ", deslocacao, " para a frente.")
    elif (letra == "d"):
        print("A tartaruga vai rodar ", rotacao, " graus para a direita.")
    elif (letra == "t"):
        print("A tartaruga vai andar ", deslocacao, " para trás.")