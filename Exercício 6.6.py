lista = list(input("Introduz uma lista: "))
soma = 0
lista_nova = [lista[0]]

def somas(lista, lista_nova, soma):
    for i in range(len(lista)-1):
        soma = soma + int(lista[i+1])
        lista_nova = lista_nova + [soma]
        
    return lista_nova

print(somas(lista, lista_nova, soma))
        