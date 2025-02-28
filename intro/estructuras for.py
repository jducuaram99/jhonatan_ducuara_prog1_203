num=int(input("ingrese numero"))
cont=0
for i in range(1,num+1):
    if num%i==0:
        cont+=1
        #print(f"{i} es divisor")
if cont==2:
    print(f"{num}es primo")
else:
    print("no es primo")    


   

   
