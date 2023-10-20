import math

print("Introduz o ADN da tartaruga usando 'f','t','d' e 'e': ")
ADN = str(input())

#as cadeias de caracteres são imutaveis, não podem ser alteradas

i = 0 
i_d = 0
i_e = 0
i_f = 0
i_t = 0

n_caracteres_ADN = len(ADN)

print(n_caracteres_ADN)

verificar_e = ADN.count('e')
verificar_f = ADN.count('f')
verificar_d = ADN.count('d')
verificar_t = ADN.count('t')

while ((verificar_d + verificar_e +  verificar_f + verificar_t) != n_caracteres_ADN):
    print("Foram usados caracteres proibidos")
    
    print("Introduz o ADN da tartaruga usando 'f','t','d' e 'e': ")
    
    ADN = str(input())    
    
    print(ADN)
    
    n_caracteres_ADN = len(ADN)
    
    verificar_e = ADN.count('e')
    verificar_f = ADN.count('f')
    verificar_d = ADN.count('d')
    verificar_t = ADN.count('t')    
    
for i in range(n_caracteres_ADN):
    print(i)
    i = i + 1
        
#por cada valor de i verificar qual a letra que aparece e depois usar o if verificar letra e fazer a instrução            
    
    
    
if (verificar_e > 0) or (verificar_d > 0):
    rotacao = float(input("Introduza o valor da rotação que a tartaruga vai fazer: "))
    
if (verificar_t > 0) or (verificar_f > 0):
    deslocacao = float(input("Introduza o valor da deslocação que a tartaruga vai fazer: "))
    
for i_d in range(verificar_d):
    print("A tartaruga vai rodar ", rotacao, " graus.")
    i_d = i_d + 1
    
for i_e in range(verificar_e):
    print("A tartaruga vai rodar ", rotacao, " graus.")
    i_e = i_e + 1 
    
for i_f in range(verificar_f):
    print("A tartaruga vai rodar ", rotacao, " graus.")
    i_f = i_f + 1 
    
for i_t in range(verificar_t):
    print("A tartaruga vai rodar ", rotacao, " graus.")
    i_t = i_t + 1 