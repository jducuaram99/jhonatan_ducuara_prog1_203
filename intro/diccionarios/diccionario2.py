#inverso a hora del ingles al español
electrodomensticos={"nevera":"refrigerator","cama":"bed","estufa":"stove","lavadora":"washing machine","computador":"computer","televisor":"tv","microondas":"microwave","licuadora":"blender"}

palabra=input("ingrese palabra a traducir")
if palabra in electrodomensticos.keys():
    print(electrodomensticos[palabra])

for key,value in electrodomensticos.items():
    if palabra==value:
        print(key)
# para la otra clase toca ponerle funciones a los diccionarios