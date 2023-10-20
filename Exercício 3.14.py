print("Introduz uma cadeia de caracteres: ")
cadeia = str(input())

i = 0

n_caracteres = len(cadeia)

print("Introduz um número inteiro positivo menor que a quantidade de caracteres introduzida: ")
n_positivo = int(input())

if (n_positivo <= 0) or (n_caracteres < n_positivo):
    print("Número introduzido inválido.")
    
n_caracteres_maximo= n_caracteres -2    
    
while (i < n_caracteres_maximo):
    i_depois = i + n_positivo
    cadeia_nova = cadeia[i:i_depois]
    print(cadeia_nova)
    i = i + 1