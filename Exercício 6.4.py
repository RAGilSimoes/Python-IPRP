numero = int(input("Introduz um número: "))
lista = list(input("Introduz uma lista numérica: "))
numeros_menores = 0

def conta_menores(numero, lista, numeros_menores):
    for i in range(len(lista)):
        if int(lista[i]) < numero:
            numeros_menores += 1
            
    return numeros_menores

print(conta_menores(numero, lista, numeros_menores))
