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
def creartupla():
    tupla=()
    cantidad=random.randint(5,15)
    for i in range(cantidad):
        tupla+=(random.randint(1,100),)
    return tupla
tupla1=creartupla()
print(tupla1)
print(tupla1[0])
print(tupla[-1])
def sumatupla(raro):
    suma=0
    for x in tupla:
        suma+=x
    return suma        

def meantupla(ttt):
    return(sumatupla(tupla1))

tup=(1,2,3)
print(sumatupla(tupla1))
print(sumatupla(tup))

print(meantupla(tupla1))
print(meantupla(tup))

def mayortupla(tupla)
if tupla1<tup
    print("tupla1 es menor que tup")

elif tupla1>tup
    print("tupla1 es mayor que tup")
else:
    print("las tuplas son iguales")    


#escriba una funcion que permita llenar una tupla. elementos entre 1 y 100 y la cantidad varia entre 1 y 15