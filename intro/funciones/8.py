#imprima los multiplos de 3 entre 0 y 100
#solicite al usuario un valor de inicio, terminación y de incremento o decremento e imprima el ciclo 
for i in range (0,101,3):
    print(i)
#solicite al usuario un valor de inicio, terminación y de incremento o decremento e imprima el ciclo, diga que numeros son multiplos de 7
inicio=int(input("donde inicia"))
tope=int(input("donde termina"))
step=int(input("incremento"))
for i in range (inicio,tope,step):
    if i%7==0:
        print (i)