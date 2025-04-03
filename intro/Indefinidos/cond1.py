#Escribe un programa que pida tres números y que escriba si son los tres iguales
#si hay dos iguales o si son los tres distintos

num1 = float(input("ingresa el primer numero: "))
num2 = float(input("ingresa el segundo numero: "))
num3 = float(input("ingresa el tercer numero: "))
if num1 == num2 == num3:
  print("los tres son iguales")
elif num1 == num2 or num1 == num3 or num2== num3:
  print("hay dos numeros iguales")
else:
  print("los tres numeros son distintos.")

#Pedir una nota de 0 a 10 y mostrarla de la forma: Insuficiente, Suficiente, Bien,
#etc. Use la escala que prefiera, pero cerciórese que tiene 5 valores




