#promedio
import random
cantidad=random.randint(5,15)
vector=[]
for i in range(cantidad):
    num=random.randint(1,100)
    vector.append(num)
print(vector)

def promedio(vector):
    suma = 0  
    for num in vector:  
        suma += num
    promedio1 = suma / len(vector)
    print("Promedio:", promedio1)

promedio(vector)