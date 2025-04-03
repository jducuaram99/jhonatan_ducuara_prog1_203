import random
def llenarLista(cantidad):
     lista=[]
     for i in range(cantidad):
         num=random.randint(1,100)
         lista.append(num)
     return lista
 
def mayorlista(lista):
    
    mayor1=0
    
    for m in lista:
        if m>mayor1:
            mayor1=m
         
    return mayor1   

def menorlista(lista):
    
    menor1=100
    
    for m in lista:
        if m<menor1:
           menor1=m
    return menor1 

lista1=llenarLista(random.randint(3,15))
print(lista1)

print(f"el mayor es {mayorlista(lista1)}")
print(f"el menor es {menorlista(lista1)}")