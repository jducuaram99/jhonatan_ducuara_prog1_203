#Pedir 3 numeros e indicar cual de ellos es el valor del medio. Ej 11, 2 1000, el valor del medio es 11. No use operadores lógicos
a= int(input("ingrese el primer numero"))
b= int(input("ingrese el segundo numero"))
c= int(input("ingrese el tercer numero"))
if b<a<c or c<a<b:
     print("el valor del medio es",a)
elif a<b<c or c<b<a:
     print("el valor del medio es",b)
else:
     print("el valor del medio es",c) 

    