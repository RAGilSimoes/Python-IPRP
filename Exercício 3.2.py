import math 

print("Introduz os lados do triângulo: ")
a = float(input())
b = float(input())
c = float(input())

s = (a + b + c)/ 2

area = math.sqrt(s*(s-a)*(s-b)*(s-c))

print("A área do triângulo é: ", area)