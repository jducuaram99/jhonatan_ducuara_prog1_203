#1. Llenar un arreglo de n elementos con números generados con la función random. N es
ingresado por el usuario. Diseñe un menú con las siguientes operaciones.
b.Suma
import random
def nuevovector(j):
    return [random.randint(1, 100) for i in range(j)]
def csum(vector):
    t1 = [num for num in vector] 
    r= 0
    for num in t1:
        r=r+num
    return r
j = int(input("Ingrese la cantidad de elementos: "))
vector = nuevovector(j)
sum1 = csum(vector)
print(vector)
print("suma", sum1)