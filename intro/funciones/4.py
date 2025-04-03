#Pedir una nota de 0 a 10 y mostrarla de la forma: Insuficiente, Suficiente, Bien,etc. Use la escala que prefiera, pero cerciórese que tiene 5 valores

nota=int(input("ingrese una nota de 0 a 10: "))
if nota < 0 or nota > 10:
  print("la nota debe estar entre 0 y 10.")
else:
  if nota < 5:
    print("insuficiente")
  elif nota <6:
    print("suficiente")
  elif nota <8:
    print("bien")
  elif nota <9:
    print("notable")
  else:
    print("sobresaliente")