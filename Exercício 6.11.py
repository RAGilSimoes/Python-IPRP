frutas = ["Maçã", "Banana", "Laranja", "Melancia", "Melão"]
quantidade = [5, 4, 7, 6, 9]

dicionario = {}

for i in range(len(frutas)):
    dicionario.setdefault(frutas[i], quantidade[i])
    
print(dicionario)