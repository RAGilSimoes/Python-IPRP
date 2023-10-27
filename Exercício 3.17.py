import math

print("Introduz o ADN da tartaruga usando 'f','t','d' e 'e': ")
ADN = str(input())

n_caracteres_ADN = len(ADN)

verificar_e = ADN.count('e')
verificar_f = ADN.count('f')
verificar_d = ADN.count('d')
verificar_t = ADN.count('t')

while ((verificar_d + verificar_e +  verificar_f + verificar_t) != n_caracteres_ADN):
    print("Foram usados caracteres proibidos")
    
    print("Introduz o ADN da tartaruga usando 'f','t','d' e 'e': ")
    
    ADN = str(input())    
    
    n_caracteres_ADN = len(ADN)
    
    verificar_e = ADN.count('e')
    verificar_f = ADN.count('f')
    verificar_d = ADN.count('d')
    verificar_t = ADN.count('t')    
                 
if (verificar_e > 0) or (verificar_d > 0):
    rotacao = float(input("Introduza o valor da rotação que a tartaruga vai fazer: "))
    
if (verificar_t > 0) or (verificar_f > 0):
    deslocacao = float(input("Introduza o valor da deslocação que a tartaruga vai fazer: "))
     
    
for letra in ADN:
    if (letra == "e"):
        print("A tartaruga vai rodar ", rotacao, " graus para a esquerda.")
    elif (letra == "f"):
        print("A tartaruga vai andar ", deslocacao, " para a frente.")
    elif (letra == "d"):
        print("A tartaruga vai rodar ", rotacao, " graus para a direita.")
    elif (letra == "t"):
        print("A tartaruga vai andar ", deslocacao, " para trás.")