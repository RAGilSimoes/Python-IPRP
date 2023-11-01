n = int(input("Introduz um número inteiro: "))

factorial_final = 1

def fact(n, factorial_final):
    for i in range(n):
        factorial = n-i
        factorial_final = factorial_final * factorial
    print(factorial_final)
        
fact(n, factorial_final)