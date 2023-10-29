palavra = input("Introduz um nome por extenso: ")
tamanho = len(palavra)
acronimo = ""
i = 0

acronimo = palavra[0]

for letra in palavra:
    if letra == " ":
        proxima = palavra[i+1]
        acronimo = acronimo + proxima
    i += 1

print(acronimo)