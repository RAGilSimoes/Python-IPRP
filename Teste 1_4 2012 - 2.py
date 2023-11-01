x = int(input("Introduz um número: "))
y = int(input("Introduz um número: "))
z = int(input("Introduz um número: "))

if (x > y) and (y > z):
    print(x, y, z)
elif (x > z) and (z > y):
    print(x, z, y)
elif (y > x) and (x > z):
    print(y, x, z)
elif (y > z) and (z > x):
    print(y, z, x)
elif (z > x) and (x > y):
    print(z, x, y)
elif (z > y) and (y > x):
    print(z, y, x)