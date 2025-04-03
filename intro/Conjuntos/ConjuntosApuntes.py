import random


c1=set()
c1.add(10)
print(c1)
c1.add(11)
print(c1)
lista=[9,8,7]
tupla=(23,24,9,7,8)
c2={55,60}
c1.update(c2)
print(c1)
c1.update(lista)
print(c1)
c1.update(tupla)
print(c1)
#no indexable
#for i in range(len(c2))
#print(c2[0])
for elemento in c1:
    print(elemento)

print(155 in c2)

#llenar un conjunto con numeros aleatorios entre 1 y 20, el tamaño del conjunto es un nunmero aleatorio entyre 1 y 15. si el numero a ingresar ya existe en el conjunto se debe copiar en otro conjunto llamado duplicapo
import random
original=set()
duplicados=set()
tam=random.randint(5,15)
for i in range(tam):
    num=random.randint(1,20)
    if num not in original:
        original.add(num)
    else:
        duplicados.add(num)
print(original)
print(duplicados)

c3={1,2,3,4,5,6,7,8,9,0}
c3.pop(10)
print(c3)
print(c3.pop())
print(c3)

#operaciones entre conjuntos
#| pipe
#& ampersant
#- diferencia
#^ circunflejo

A={1,2,3,4,5,7,9}
B={1,3,6,7,8,9,0}
print(A)
print(B)
union= A|B
print(union)

interseccionn =A&B
print(interseccionn)

diferencia= A-B
print(diferencia)

difsimetrica= A^B
print(difsimetrica)

import random

conjunto1=set()
conjunto2=()

xnumeros=random.randint(5,15)
for i in range (range.randint(1,20))


print("subset1=",diferencia,issubset(a))
print("subset2=",diferencia.issubset(b))

print("superset1=", union.issuperset(a))
print("superset1",union.issuperset(b))

industrial:{algebra,}
