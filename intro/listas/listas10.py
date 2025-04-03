#varianza
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
def varianza(vector):
    promedio1=promedio(vector)  
    sum2=0
    for num in vector:
        resta=num-promedio1
        sum2+=resta**2
    varianza=(sum2/(len(vector)-1))
    print(varianza)
varianza(vector)