autor = {"php":"Rasmus Lerdorf","perl":"Larry Wall","tcl":"John Ousterhout",
"awk":"Brian Kernighan","java":"James Gosling","parrot":"Simon Cozens",
"python":"GuidovanRossum","xpto":"zxcv"}

teste = {"Teste":"Teste Isto é um teste"}
autor.update(teste)
print("Adicionar um elemento:", autor)

autor["python"] = "Guido van Rossum"
print("Novo autor do python: ", autor)

del autor["xpto"]
print("Eliminar xpto:", autor)

print("O dicionário tem ", len(autor), " elementos.")

print("Há uma entrada para C++?", autor.get("c++", "Não"))
