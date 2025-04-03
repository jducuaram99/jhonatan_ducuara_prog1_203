#Escribe un programa que pida tres números y que escriba si son los tres iguales o si hay dos iguales o si son los tres distinto
numero1 = int(input("ingresa el primer numero: "))
numero2 = int(input("ingresa el segundo numero: "))
numero3 = int(input("ingresa el tercer numero: "))
if numero1 == numero2 == numero3:  
    print("los tres son iguales")
elif numero1 == numero2 or numero1 == numero3 or numero2== numero3:  
    print("hay dos numeros iguales")
else:  print("los tres numeros son distintos.")