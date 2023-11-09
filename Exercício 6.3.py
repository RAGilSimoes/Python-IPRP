l1 = [1,2,3]
l2 = ['a','b','c']
lista_nova = []

def alterna(lista_nova, l1, l2):
    for i in range(len(l1)):
        lista_nova.append(l1[i])
        lista_nova.append(l2[i])
        
    return lista_nova
        
print(alterna(lista_nova, l1, l2))