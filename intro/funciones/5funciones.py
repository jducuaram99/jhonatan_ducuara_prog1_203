def c(i):
    while i != 1:
        print(i)
        if i % 2 == 0:
            i //= 2
        else:
            i = 3 * i + 1
    print(1)
i = int(input("ingrese un numero "))
c(i)