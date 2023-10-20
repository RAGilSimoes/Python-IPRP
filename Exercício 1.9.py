print("Introduza o peso em kilos:")
peso = float(input())

print("Introduza a altura em metros:")
altura = float(input())

calculo_imc = (peso / (altura ** 2))
valor_imc = round(calculo_imc, 2)

print("O valor do IMC é ", valor_imc)