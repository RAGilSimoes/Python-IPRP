print("Introduz a nota dos testes: ")
teste1 = int(input())
teste2 = int(input())
teste3 = int(input())
teste4 = int(input())

print("Introduz a nota do exame: ")
exame = int(input())

nota = 0.75 * (teste1 + teste2 + teste3 + teste4) + 0.7*exame

if nota < 7:
    print("Reprovado")
elif nota >= 14:
    print("Aprovado")
elif nota >= 7 and nota < 14:
    print("Oral")