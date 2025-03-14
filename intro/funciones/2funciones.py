def pa(j, dif, can):
    suma = 0
    for i in range(can):
        suma += j
        j += dif
    return suma
j = int(input("introduzca el termino de inicio"))
dif = int(input("introduzca la diferencia que desea"))
can = int(input("introduzca cuantos terminos desea"))

suma = pa(j, dif, can)
print("la suma es", suma)