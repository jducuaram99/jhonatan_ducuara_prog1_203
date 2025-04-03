import random 

def llenarLista(cantidad):
    lista=[]
    for i in range(cantidad):
        num=random.randint(1,100)
        lista.append(num)
    return lista
vec1=llenarLista(5)
vec2=llenarLista(10)
vec3=llenarLista(20)

print(vec1)
print(vec2)
print(vec3)

def sumalista(lista):
    suma=0
    for num in lista:
        suma+=num
    return suma 

print(vec1)
print(vec2)
print(vec3)