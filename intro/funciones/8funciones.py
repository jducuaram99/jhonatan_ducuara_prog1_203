def primos(j):
    d1 = 2
    r1 = []
    while j > 1:
        if j % d1 == 0:
            r1 += [d1]
            j //= d1
        else:
            d1 += 1
    return r1
num1 = int(input("Introduce un número para descomponer en factores primos: "))
print("Factores primos:", primos(num1))