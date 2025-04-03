#2. d. Cuál es el promedio conjunto (uniendo los dos arreglos)
import random
def nuevovector():
    return [random.randint(1, 100) for i in range(random.randint(5,15))]
def rta(vtotal):
    suma = 0
    for num in vtotal:
        suma += num
    return suma
def cpro(suma, vtotal):
    return suma / len(vtotal)
j1 = nuevovector()
j2 = nuevovector()
vtotal = j1 + j2
suma = rta(vtotal)
prom = cpro(suma, vtotal)
print(j1)
print(j2)
print("suma de los dos vectores", vtotal)
print("promedio", prom)