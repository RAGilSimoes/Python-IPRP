#ocorrencia por cada minuto
nascimentos = int(input("Introduza a frequência de nascimentos (minutos): "))
falecimentos = int(input("Introduza a frequência de falecimentos (minutos): "))
emigracao = int(input("Introduza a frequência de emigração por cada (minutos): "))
populacao_inicial = int(input("Introduz a quantidade de pessoas existentes no início: "))

minutos = 365*24*60

estimativa = populacao_inicial - ((minutos * (1/nascimentos)) + (minutos * (1/falecimentos)) + (minutos * (1/emigracao)))

print(estimativa)