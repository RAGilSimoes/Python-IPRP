print("Introduz uma cadeia de caracteres: ")
cadeia = str(input())

cadeia_numero = len(cadeia)
i = cadeia_numero - 1
i_2 = cadeia_numero

while (i <= cadeia_numero):
    cadeia_nova = cadeia[i:i_2]
    print(cadeia_nova)
    i = i - 1