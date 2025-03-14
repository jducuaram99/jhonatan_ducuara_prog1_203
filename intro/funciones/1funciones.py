def fibo(j):
    if j == 1:
        return (0)
    elif j == 2:
        return (0, 1)
    
    serie1 = [0, 1]
    for i in range(2, j):
        n1 = serie1[-1] + serie1[-2]
        serie1 = serie1 + [n1]
    
    return serie1

j = int(input("introduza la cantidad de numeros que desea"))
solucion = fibo(j)
print("la serie es", solucion)