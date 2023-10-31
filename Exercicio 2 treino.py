cadeia = input("Introduz uma cadeia de caracteres: ")

def separa_chars(cadeia):
    cadeia_vogais = ()
    cadeia_resto = ()
    
    vogais="aeiouAEIOU"
    
    for letra in cadeia:
        if letra in vogais:
            cadeia_vogais = cadeia_vogais + tuple(letra)
            
        else:
            cadeia_resto = cadeia_resto + tuple(letra)
            
    cadeia_vogais_nova = cadeia_vogais[::-1]
    cadeia_resto_nova = cadeia_resto[::-1]
    resultado = (cadeia_vogais_nova) , (cadeia_resto_nova)
    
    print("resultado: ", resultado)
        
separa_chars(cadeia)
    