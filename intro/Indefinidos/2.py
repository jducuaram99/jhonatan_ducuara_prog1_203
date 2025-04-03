num = int(input("Ingrese un numero"))
sumadedivisores= 0
for i in range(1, num):
    if num % i == 0:
        sumadedivisores += i
if sumadedivisores == num:
    print(f"{num} es un número perfecto.")
else:
    print(f"{num} no es un número perfecto.")
