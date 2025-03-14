import random
def crear():
    return random.randint(1, 100)
def adivinar():
    num2= crear()
    for i in range(1, 101):
        num1= int(input("adivine un numero entre 1 y 100 "))
        if num1 < num2:
            print("muy bajo intente de nuevo")
        elif num1 > num2:
            print("muy alto intente de nuevo")
        else:
            print(f" adivino en {i} intentos.")
adivinar()