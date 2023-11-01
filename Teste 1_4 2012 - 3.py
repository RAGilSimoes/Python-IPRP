n = int(input("Introduz um número inteiro: "))
n_novo = n
tamanho_ciclo = 1

print(n, end=" ")

while (n_novo != 1):
    if (n_novo % 2 == 0):
        n_novo = int(n_novo / 2)
    else:
        n_novo = int(n_novo * 3 + 1)
        
    tamanho_ciclo += 1
    print(n_novo, end=" ")
    
print()    
print("O tamanho do ciclo é: ", tamanho_ciclo)