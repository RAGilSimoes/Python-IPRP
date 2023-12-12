def metabolismo_basal(dicionario):
    dicionario_novo = {}
    for i in dicionario:
        pessoa = dicionario[i]

        sexo = pessoa[0]
        idade = pessoa[1]
        altura_cm = pessoa[2]
        peso_kg = pessoa[3]

        if (sexo == "homem"):
            racio_metabolismo_basal = (66 + (6.3 * peso_kg) + (12.9 * altura_cm) - (6.8 * idade))
        elif (sexo == "mulher"):
            racio_metabolismo_basal = (65.5 + (4.3 * peso_kg) + (4.7 * altura_cm) - (4.7 * idade))
           
        dicionario_novo.update({i : racio_metabolismo_basal})
    return dicionario, dicionario_novo
    
print(metabolismo_basal({"30551434":("homem", 18, 178, 80), "30551431":("mulher", 23, 154, 50)}))