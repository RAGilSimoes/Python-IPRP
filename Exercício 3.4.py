idade = int(input("Introduza a sua idade: "))

bpm = 163 + (1.16 * idade) - (0.018 * (idade ** 2))

print("O valor médio do batimento cardíaco máximo para uma pessoa de ", idade, " anos é ", bpm)