def piramide(num):
    for i in range(1, num+1 ):
        print(i * (10**i // 9))
num = int(input("introduzca la cantidad de filas  "))
piramide(num)