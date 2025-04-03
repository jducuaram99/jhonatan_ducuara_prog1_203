#lista=[]
#print(type(lista))
#cantidad=int(input("que cantidad de numeros?"))
#for i in range(cantidad):
  #  num=int(input("ingrese número"))
  #  lista.append(num)

#print(lista)

import random
cantidad=random.randint(5,15)
vector=[]
for i in range (cantidad):
    num=random.randint(1,100)
    vector.append(num)

print(vector)
print(len(vector))

for i in range(len(vector)):
    if i%2==0:
        print(vector[i],end="")

print()
for i in range(0,len(vector),2):
    print(vector[i],end="")

for i in range(len(vector)):
    if i%2==1:
        print(vector[i],end="")

print()
for i in range(1,len(vector),2):
    print(vector[i],end="")


cad="universidad de cundinamarca"
print(cad[0])
print(cad[-1])
for letra in cad:
    print(letra)
lista=[1,9,2,8,3,7,4,6,5]
suma=0
for num in lista:
    print(num)
    suma+=num
print(f"suma={suma}")