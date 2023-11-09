lista = [[1,0,1],[0,1,1],[0,1,0]]

def rodar(lista):
    linha1 = [lista[2][0], lista[1][0], lista[0][0]]
    linha2 = [lista[2][1], lista[1][1], lista[0][1]]
    linha3 = [lista[2][2], lista[1][2], lista[0][2]]
    
    print(linha1)
    print()
    print(linha2)
    print()
    print(linha3)
    print()

print(lista)
rodar(lista)