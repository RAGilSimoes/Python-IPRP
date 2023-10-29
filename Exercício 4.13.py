import math

milha = 1.609

print("%s    %4s" % ("Milhas", "Quilómetros"))
print("---------------------------")

for i in range(10,19):
    print("%.2f    %10.2f" % (i, milha*i))