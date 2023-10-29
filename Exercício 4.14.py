numero = int(input("Introduz um número inteiro até 10: "))

print("Tabuada do número ", numero)
print("--------------------")

for i in range(1, 11):
    print("%d %s %4d %s %4d" % (numero, "x", i, "=", numero*i))