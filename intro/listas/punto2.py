# Cuál de los dos tiene mayor cantidad de impares
import random
def nuevovector():
    j = random.randint(5, 15)
    return [random.randint(1, 100) for i in range(j)]
def contimpar(vector):
    return len([num for num in vector if num % 2 != 0])
def ev():
    v1 = nuevovector()
    v2 = nuevovector()
    imparv1 = contimpar(v1)
    imparv2 = contimpar(v2)
    print(v1, "cantidad", imparv1)
    print(v2, "cantidad", imparv2)
    if imparv1 > imparv2:
        print("el primero tiene mas numeros impares")
    elif imparv2 > imparv1:
        print("el segundo tiene mas numeros impares")
ev()