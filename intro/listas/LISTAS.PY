#lista=[]
#print(type(lista))
#cantidad=int(input("que cantidad de numeros?"))
#for i in range(cantidad):
  #  num=int(input("ingrese número"))
  #  lista.append(num)

#print(lista)
import random
cantidad=random.randint(1,15)
vector=[]
for i in range (cantidad):
    num=random.randint(1,100)
    vector.append(num)
for i in range(0,len(vector),2):
    print(vector[i],end=" ")    
print()
for i in range(len(vector)):
    if i%2!=0:
        print(vector[i],end=" ")
print()
for i in range (1,len(vector),2):
    print(vector[i],end=" ")
    
        