palavra1 = str(input("Introduz a primeira palavra: "))
palavra2 = str(input("Introduz a segunda palavra: "))

caracteres1 = len(palavra1)
caracteres2 = len(palavra2)

dez_porcento1 = caracteres1 * 0.10
dez_porcento2 = caracteres2 * 0.10

print("a 10 de 1:", dez_porcento1)
print("a 10 de 2:", dez_porcento2)

if (caracteres1 != caracteres2):
    print("As palavras não são amigas.")
    
else:
        
    for char in range(caracteres1):
        print("olá")
        
        #verificar cada caracter, ver se são iguais, ver se diferem e se diferirem ver onde está o mesmo
        #se estiver a mais de 10% de distância (tamanho do caracter), dizer que não são amigas
        #se estiver a menos, são amigas 