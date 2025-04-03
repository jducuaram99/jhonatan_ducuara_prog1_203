#1. Llenar un arreglo de n elementos con números generados con la función random. N es ingresado por el usuario. c. Promedio
import random
def nuevovector(j):
    return [random.randint(1, 100) for _ in range(j)]
def cprom(vector):
    t1 = 0
    for num in vector:
        t1=t1+num
    return t1 / len(vector) 
j = int(input("Ingrese la cantidad de elementos: "))
vector = nuevovector(j)
promedio = cprom(vector)
print("vector", vector)
print("promedio", promedio)