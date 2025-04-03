#Pida un numero al usuario que representa días del año. Diga a que mes del año corresponde así. Si el número es menor o igual a 31 indica que esta en enero,
#Pero si el número por ejemplo es 32 indica que es el 1 de febrero. No tenga en cuenta si el año es bisiesto, es decir siempre febrero tiene 28 días.
j1=int(input("ingrese el numero del dia del año, del cual desea saber el mes"))
if j1<=31:
    print("enero")
elif j1 <=59:
    print ("febrero")
elif j1 <=90:
    print ("marzo")
elif j1 <=120:
    print ("abril")
elif j1 <=151:
    print ("mayo")
elif j1 <=181:
    print ("junio")
elif j1 <=212:
    print ("julio")
elif j1 <=243:
    print ("agosto")
elif j1 <=273:
    print ("septiembre")
elif j1 <=304:
    print ("octubre")
elif j1 <=334:
    print ("noviembre") 
else:
    print ("diciembre")