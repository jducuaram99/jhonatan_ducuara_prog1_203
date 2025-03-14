def fibo2(tope):
    v1= 0
    v2=1
    solucion = []
    while v1 <= tope:
        solucion += [v1]  
        v1, v2 = v2, v1 + v2
    return solucion
tope = int(input("introduzca el numero de tope"))
serief = fibo2(tope)
print("la secuencia es", serief)