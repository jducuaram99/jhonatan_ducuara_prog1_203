danzas={"ana","luis","carlos","maria","pedro","ana","lucia","juan","sofia","andy","esteban","laura","camila","jhonatan","nicolas",}
deportes={"juana","luis","camilo","maria","pablo","alicia","lucia","boris","sofia","amdy","esteban","camila","jhonatan","camilo"}
print("danzas",danzas)
print("deportes", deportes)

union=danzas|deportes 
print(f"union{union}")
#bienestar busca que estudiantes se encuentran en comun en los dos grupos para correr la voz del evento
inter=danzas&deportes
print(f"interseccion{inter}")
#adicional a esto bienestar busca dar una danza recreativa unicamente con los que estan en danzas

diferencia=danzas-deportes
print(f"diferencia{diferencia}")
#bienestar busca saber  que estudiantes pertenecen a uno de los dos grupos para destinar ciertas tareas
difsimetrica=danzas^deportes
print(f" diferencia simetrica{danzas^deportes}")



