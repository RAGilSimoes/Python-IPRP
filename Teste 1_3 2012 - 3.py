import random

pontos_inicias = int(input("Introduz o número de pontos iniciais do jogador: "))

numero_de_jogadas = 1
pontos = pontos_inicias

while (pontos > 0):
    face = random.randint(1,6)
    
    if face == 6:
        pontos = pontos + 14
    else:
        pontos = pontos - face
            
    numero_de_jogadas += 1

print(pontos)
print("Foram precisas ", numero_de_jogadas, " jogadas para o jogador perder ", pontos_inicias, " pontos.")