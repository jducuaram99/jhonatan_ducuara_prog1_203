#Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera, Si trabaja 40 horas o menos se le paga $2600 por hora
#Si trabaja más de 40 horas se le paga $2600 por cada una de las primeras 40 horas y $5000 por cada hora extra
horas= int(input("Cuántas horas trabajó esta semana"))
tarifa1 = 2600
tarifa2 = 5000

if horas<= 40:
    salario1 = horas * tarifa1
    print ("Su salario es de", salario1)

else:
    salario2= 40 * tarifa1
    horasl= horas-40
    salariomas= horasl * tarifa2
    salario2= salario2 + salariomas
    print ("Su salario es de",salario2)