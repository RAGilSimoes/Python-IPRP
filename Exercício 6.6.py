def somas():
    lista = [1,2,3]
    soma = 0
    lista_nova = []
    for i in range(len(lista)):
        soma += lista[i]
        lista_nova += [soma]
        
    return lista_nova

print(somas())
        