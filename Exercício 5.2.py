viagem = 120

estrada = input("Escolhe uma estrada entre a A1, A20 e A21: ")

if (estrada == "A1"):
    combustível = 0.15
    portagens = 6.52
    custo = combustível * viagem + portagens
    
elif (estrada == "A20"):
    combustível = 0.12
    portagens = 15.2
    custo = combustível * viagem + portagens
    
elif (estrada == "A21"):
    combustível = 0.10
    portagens = 5.75
    custo = combustível * viagem + portagens
    
print("Ao escolher a estrada ", estrada, " o custo total da viagem vai ser de %.2f €" % (custo))