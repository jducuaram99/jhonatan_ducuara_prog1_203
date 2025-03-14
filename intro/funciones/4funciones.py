def jhonatan(digi):
    a1 = 0
    while digi > 0:
        a1 += digi % 10  
        digi //= 10  
    return a1
digi = int(input("introduzca un numero"))
rpta = jhonatan(digi)
print("la suma es:", rpta)