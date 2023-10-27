print("Introduz uma cadeia de caracteres: ")
cadeia = str(input())

cadeia_numero = len(cadeia)
i = 0 
i_2 = 12

while (i <= cadeia_numero):
    cadeia_nova = cadeia[i_2:12]
    print(cadeia_nova)
    i_2 = i_2 - 1
    i += 1    