import random as r

n = int(input("Introduz o número de vezes que o dado vai ser rodado: "))

pares = 0
impares = 0

for i in range(n):
    face = r.randint(1,6)
    
    if (face % 2 == 0):
        pares += 1
    else:
        impares += 1
        
percentagem = (pares / n) * 100

print("saiu par: ", pares)
print("saiu impar: ", impares)
print("A percentagem de vezes em que saiu número par é: ", percentagem, "%")