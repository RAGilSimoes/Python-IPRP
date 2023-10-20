a = 10
b = a

id_a = id(a)
id_b = id(b)

tipo_a = type(a)
tipo_b = type(b)

print(id_a, tipo_a, a)
print(id_b, tipo_b, b)
print("São objetos iguais.")