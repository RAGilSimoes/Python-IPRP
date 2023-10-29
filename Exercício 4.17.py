
t_i = float(input("Introduz a temperatura inicial em Celsius: "))
t_f = float(input("Introduz a temperatura final em Celsius: "))
m = float(input("Introduz a massa de água que se quer aquecer: "))

E = m * (t_i - t_f) * 4184

print("Temperatura inicial (Celsius): %d " % (t_i))
print("Temperatura final (Celsius): %d " % (t_f))
print("Quantidade de água (Quilogramas): %d " % (m))
print("Para a massa de água %.2f, temperatura inicial %.2f e temperatura final %.2f a energia necessária é: %.2f Joules" % (m, t_i, t_f, -E))