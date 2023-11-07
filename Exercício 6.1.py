soma_idades = 0

idades = [12,45,32,65,76,23,12,45,32]

print("número de idades: ", len(idades))

print("Idades: ", idades)

print("Idades invertidas: ", idades[::-1])

print("Idades sem a primeira e a última: ", idades[1:len(idades)])

print("Idade maior: ",max(idades), ", Idade menor: ", min(idades))

for i in range(len(idades)):
    soma_idades = soma_idades + idades[i]
    
print("A soma de todos os valores é:", soma_idades)

referencia = int(input("Introduz a idade de referência: "))
ocurrencias = 0
for i in range(len(idades)-1):
    if (idades[i] < referencia):
         ocurrencias += 1
         
print(ocurrencias)

if (idades.count(17) == 0):
    print("Não há alunos com 17 anos.")
else:
    print("Há alunos com 17 anos.")


