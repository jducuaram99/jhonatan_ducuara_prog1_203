#f. Cuál de los dos tiene mayor cantidad de pares
import random
def nuevovector():
    j = random.randint(5, 15)
    return [random.randint(1, 100+1) for i in range(j)]
def contpar(vector):
    return len([num for num in vector if num % 2 == 0])
def ev():
    v1 = nuevovector()
    v2 = nuevovector()
    parv1 = contpar(v1)
    parv2 = contpar(v2)
    print(v1, "cantidad", parv1)
    print(v2, "cantidad", parv2)
    if parv1 > parv2:
        print("el primero tiene mas números pares")
    elif parv2 > parv1:
        print("el segundo tiene mas números pares")
ev()