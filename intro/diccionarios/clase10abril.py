# vendedor = {"nombre": "Jhonatan",
#     "area": "cosmeticos",
#     "lider": "Ducuara",
#     "productos": ["sombras", "esmalte", "crema facial", "serum", "toallitas desmaquillantes"],
#     "precio": [18000, 7000, 25000, 30000, 12000]}

# vendedor = {"nombre": "Jhonatan",
#     "area": "Perecederos",
#     "lider": "Ducuara",
#     "productos": ["lechuga", "tomate", "pera", "res", "cerdo"],
#     "precio": [3000, 3500, 2500, 27000, 21000]}

# vendedor = {"nombre": "Jhonatan",
#     "area": "cosmeticos",
#     "lider": "Ducuara",
#     "productos": ["brillo labial", "mascarilla facial", "tinte de cejas", "crema antiarrugas", "kit de maquillaje"],
#     "precio": [8500, 22000, 15000, 27000, 45000]}

# vendedor = {"nombre": "Jhonatan",
#     "area": "no perecederos",
#     "lider": "Ducuara",
#     "productos": ["arroz", "lentejas", "harina", "aceite", "azúcar"],
#     "precio": [5000, 4000, 3500, 12000, 4500]}

# vendedor = {"nombre": "Jhonatan",
#     "area": "congelados",
#     "lider": "Ducuara",
#     "productos": ["nuggets", "vegetales mixtos", "helado", "empanadas", "filete de merluza"],
#     "precio": [11000, 8000, 9500, 6000, 28000]}

# #slicing
# lista=[10,30,20,50,5,7,11,21,31,100]
# print(lista[0])
# print(lista[5])
# print(lista[-1])
# print(lista[1:4])
# print(lista[0:5])
# print(lista[:5])
# print(lista[-1:-6:-1])
# print(lista[::2])
# print(lista[-2::-2])
# print(lista[-6:-1])
# print(lista[5:11])
# print(lista[5:])

#llenar una lista (tamaño 10 a 20 elementos) con numeros aleatorios(entre 1 y 100)

import random
tamaño=random.randint(5,10)*2
lista=[random.randint(1,100) for i in range(tamaño)]

print("lista1",lista)
print("tamaño",len(lista))

primeramitad = lista[:len(lista)//2]
suma_primera = sum(primeramitad)
promedio_primera = suma_primera / len(primeramitad)

segunda_mitad = lista[len(lista)//2:]
suma_segunda = sum(segunda_mitad)
promedio_segunda = suma_segunda / len(segunda_mitad)

pares = lista[::2]
suma_pares = sum(pares)
promedio_pares = suma_pares / len(pares)

impares = lista[1::2]
suma_impares = sum(impares)
promedio_impares = suma_impares / len(impares)

print("\nPrimera mitad:", primeramitad)
print("Suma:", suma_primera, "| Promedio:", promedio_primera)

print("\nSegunda mitad:", segunda_mitad)
print("Suma:", suma_segunda, "| Promedio:", promedio_segunda)

print("\nPosiciones pares:", pares)
print("Suma:", suma_pares, "| Promedio:", promedio_pares)

print("\nPosiciones impares:", impares)
print("Suma:", suma_impares, "| Promedio:", promedio_impares)

#ahora como lo hizo el profe

tam=1
while tam%2!=0:
    tam=random.randint(10,20)
    print(tam)

lista=[random.randint(1,100) for i in range(tam)]
print(lista)
sum1=0
sum2=0
mitad=len(lista)//2
print(f"mitad={mitad}")
for x in lista[:mitad]:
    sum1+=x
for x in lista[mitad:]:
    sum2+=x

print(f"suma primera mitad es:{sum1}")
print(f"suma segunda mitad es:{sum2}")
print(f"media primera mitad es:{sum1/mitad}")
print(f"media segunda mitad es:{sum2/mitad}")

sum3,sum4=(0,0)
for x in lista[::2]:
    sum3+=x
for x in lista[1::2]:
    sum4+=x

print(f"suma 3={sum3}")
print(f"suma 4={sum4}")
print(f"media 3={sum3/mitad}")
print(f"media 4={sum4/mitad}")

#cambiar la palabra lista por tupla 