numero = 0
quadrado = 0

linhas = int(input("Introduz o número de linhas que pretendes que o quadro tenha: "))

print('%s     %s' % ('Número', 'Quadrado'))

for i in range(1, linhas + 1):
    numero += 1
    quadrado = numero ** 2
    print('%6d %12d' % (numero, quadrado))
    