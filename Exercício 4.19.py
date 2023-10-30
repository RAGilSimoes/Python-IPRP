linhas = int(input("Introduz o número de linhas da matriz: "))
colunas = int(input("Introduz o número de colunas da matriz: "))

matriz= []

for i in range(linhas):
    linha = []
    for i in range(colunas):
        elemento = int(input("Introduz o próximo elemento: "))
        linha = linha + [elemento]
    matriz = matriz + [linha]
    
for i in range(linhas):
    nova_matris = matriz[i]
    for j in range(colunas):
        print("(%d,%d): %d" % (i, j, nova_matris[j]) , end=" ")
    print()
        
