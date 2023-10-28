import random

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

        
for letra in ADN:           
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