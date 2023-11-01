texto = input("Introduz um texto à tua escolha: ")
letra_introduzida = input("Introduz a letra que quiseres: ")

texto_novo = ""

for letra in texto:
    if letra != letra_introduzida:
        texto_novo = texto_novo + letra
    
print(texto_novo)