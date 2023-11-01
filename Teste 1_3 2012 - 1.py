texto = input("Introduz um texto: ")
palavra = input("Introduz uma palavra: ")

palavra_invertida = palavra[::-1]

def encontra(texto, palavra):
    if palavra in texto:
        print("True")
    elif palavra not in texto:
        if palavra_invertida in texto:
            print("True")
        else:
            print("False")
        
encontra(texto, palavra)