print("Introduz uma cadeia de caracteres: ")
cadeia = str(input())

cadeia_numero = len(cadeia)
i = 0 
i_2 = cadeia_numero

while (i <= cadeia_numero):
    cadeia_nova = cadeia[i_2:cadeia_numero]
    print(cadeia_nova)
    i_2 = i_2 - 1
    i += 1    