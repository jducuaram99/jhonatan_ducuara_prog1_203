lista=[100]
x=90
escalar=(100)
tupla=(100,)
print(type(lista))
print(type(tupla))
lista.append(12)
t=(1,2)
print(type(t))
print(t)
t=t+(10,)
print(t)
#Para que sea tupla (agregarle una coma)

#Escriba una funcion que permita llenar una tupla con elementos entre 1 y 100 y lacantidad varia entre 5 y 15.
import random
def crearTupla():
   tupla=()
   cantidad=random.randint(5,15)
   for i in range(cantidad):
      tupla+=(random.randint(1,100),)
   return tupla
tupla1=crearTupla()
print(tupla1)
print(tupla1[0])
print(tupla1[-1])
suma=0
for x in tupla1:
   suma+=x
print(suma)


def sumarTupla(tt):
   suma=0
   for x in tt:
    suma+=x
    return suma
   
def meanTupla(ttt):
   return sumarTupla(ttt)/len(ttt)
tup=(1,2,3)
print(sumarTupla(tupla1))
print(sumarTupla(tup))
   
print(meanTupla(tupla1))
print(meanTupla(tup))

#Mayor y menor
def mayortupla(tupla1):
   mayor1=0
   for m in tupla1:
      if m>mayor1:
         mayor1=m
   return mayor1

def menortupla(tupla1):
   menor1=100
   for m in tupla1:
      if m<menor1:
         menor1=m
   return menor1

print(menortupla(tupla1))
print(mayortupla(tupla1))