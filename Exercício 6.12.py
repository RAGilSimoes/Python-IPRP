frutas = ["Maçã", "Banana", "Laranja", "Melancia", "Melão"]
print("Frutas disponíveis: ", frutas)
fruta_escolhida = input("Introduz uma fruta das disponíveis: ")


if fruta_escolhida == "Maçã":
    comprada = int(input("Introduz a quantidade de maçã comprada: "))
    preco_comprada = float(input("Introduz o preço a que a maçã foi comprada por quilo: "))
    stock = int(input("Introduz a quantidade de maçã em stock: "))
    preco_venda = float(input("Introduz o preco a que a maçã foi vendida:"))
    Informacoes = {"Fruta": fruta_escolhida, "Comprada (Kg)": comprada, "Preço_C/Kg": preco_comprada, "Stock": stock, "Preço_V/Kg": preco_venda}
    
elif fruta_escolhida == "Banana":
    comprada = int(input("Introduz a quantidade de banana comprada: "))
    preco_comprada = float(input("Introduz o preço a que a banana foi comprada por quilo: "))
    stock = int(input("Introduz a quantidade de banana em stock: "))
    preco_venda = float(input("Introduz o preco a que a banana foi vendida:"))
    Informacoes = {"Fruta": fruta_escolhida, "Comprada (Kg)": comprada, "Preço_C/Kg": preco_comprada, "Stock": stock, "Preço_V/Kg": preco_venda}

elif fruta_escolhida == "Laranja":
    comprada = int(input("Introduz a quantidade de laranja comprada: "))
    preco_comprada = float(input("Introduz o preço a que a laranja foi comprada por quilo: "))
    stock = int(input("Introduz a quantidade de laranja em stock: "))
    preco_venda = float(input("Introduz o preco a que a laranja foi vendida:"))
    Informacoes = {"Fruta": fruta_escolhida, "Comprada (Kg)": comprada, "Preço_C/Kg": preco_comprada, "Stock": stock, "Preço_V/Kg": preco_venda}
    
elif fruta_escolhida == "Melancia":
    comprada = int(input("Introduz a quantidade de melancia comprada: "))
    preco_comprada = float(input("Introduz o preço a que a melancia foi comprada por quilo: "))
    stock = int(input("Introduz a quantidade de melancia em stock: "))
    preco_venda = float(input("Introduz o preco a que a melancia foi vendida:"))
    Informacoes = {"Fruta": fruta_escolhida, "Comprada (Kg)": comprada, "Preço_C/Kg": preco_comprada, "Stock": stock, "Preço_V/Kg": preco_venda}

elif fruta_escolhida == "Melão":
    comprada = int(input("Introduz a quantidade de melão comprado: "))
    preco_comprada = float(input("Introduz o preço a que o melão foi comprado por quilo: "))
    stock = int(input("Introduz a quantidade de melão em stock: "))
    preco_venda = float(input("Introduz o preco a que o melão foi vendido:"))
    Informacoes = {"Fruta": fruta_escolhida, "Comprada (Kg)": comprada, "Preço_C/Kg": preco_comprada, "Stock": stock, "Preço_V/Kg": preco_venda}
    
preço_compra = Informacoes.get("Comprada (Kg)") * Informacoes.get("Preço_C/Kg")
vendida = Informacoes.get("Comprada_C/Kg") - Informacoes.get("Stock")
preço_venda = vendida * Informacoes.get("Preço_V/Kg")
lucro = preço_venda - preço_compra

print("O lucro obtido é ", lucro) 

