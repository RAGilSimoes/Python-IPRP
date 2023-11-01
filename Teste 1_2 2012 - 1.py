texto = input("Introduz um texto: ")
p = int(input("Introduz uma percentagem: "))

quantidade = int(len(texto) * (p/100))

palavra = texto[:quantidade]

print(palavra)