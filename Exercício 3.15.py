print("Introduz uma cadeia de caracteres: ")
cadeia = str(input())

cadeia_numero = len(cadeia)
i = 0
i_2 = 1

while (i_2 <= cadeia_numero):
    cadeia_nova = cadeia[i:i_2]
    print(cadeia_nova)
    i_2 = i_2 + 1