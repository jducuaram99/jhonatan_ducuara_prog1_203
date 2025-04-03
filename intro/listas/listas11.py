#Desviación estandar
import random
cantidad=random.randint(5, 15)
vector=[]
for i in range(cantidad):
    num=random.randint(1, 100)
    vector.append(num)
print(vector)
def promedio(vector):
    suma=0  
    for num in vector:  
        suma+=num
    promedio1=suma/len(vector)
    return promedio1 

def desviacion(vector):
    promedio1=promedio(vector)  
    sum2=0
    for num in vector:
        diferencia=num-promedio1
        sum2+=diferencia**2
    
    desviacion1=(sum2/(len(vector)-1))**0.5
    print(desviacion1)

desviacion(vector)