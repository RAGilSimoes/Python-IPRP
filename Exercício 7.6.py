nome_ficheiro_original = input("Introduz o nome do ficheiro original: ")
nome_ficheiro_copia = input("Introduz o nome do ficheiro cópia: ")

def copiar_ficheiros(nome_ficheiro_original, nome_ficheiro_copia):
    with open(nome_ficheiro_copia, "w") as copia:
        original = open(nome_ficheiro_original,"r")
        for linha in original:
            copia.write(linha)
            
            
copiar_ficheiros(nome_ficheiro_original, nome_ficheiro_copia)