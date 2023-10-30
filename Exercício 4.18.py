v = float(input("Introduz a velocidade do vento em milhas por hora: "))
t = float(input("Introduz o valor da temperatura exterior em Fahrenheit (entre -58 e 41): "))

t_v = 35.4 + (0.6215 * t) - (35.75 * (v ** 0.16)) + (0.4275 * t * (v ** 0.16))

print("Velocidade do vento (milhas/hora): %d" % (v))
print("Temperatura (Fahrenheit [-58, 41]): %d" % (t))
print("Para a velocidade de vento %.2f e temperatura exterior %.2f a temperatura é sentida como: %.2f" % (v, t, t_v))