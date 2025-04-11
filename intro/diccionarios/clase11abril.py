# vendedores=[{'nombre':'Maria Lopez',
# 'area':'cosmeticos',
# 'líder':'Jose Perez',
# 'productos':['shampoo', 'jabón', 'bloqueador','crema dental','gel'],
# 'precio':[20000,10000,25000,12000,30000]
# },
# {"nombre":"Laura Castiblanco","area":"cosmeticos","lider":"Alejandra","productos":["Labial","rubor","polvos","base","iluminador"], "precio":[10000,15000,20000,25000,30000]},
# {"nombre":"Laura Castiblanco","area":"Perecederos","lider":"Alejandra","productos":["uvas","manzanas","bananos","carne","pollo"], "precio":[8000,1500,2000,25000,11000]},
# {"nombre":"Laura Castiblanco","area":"cosmeticos","lider":"Alejandra","productos":["pestañina","corrector","delineador","lapiz de labios","brochas"], "precio":[17000,15000,10000,2500,32000]},
# {"nombre":"Laura Castiblanco","area":"no perecederos","lider":"Alejandra","productos":["miel","atun","sopas","maiz enlatado","cafe"], "precio":[5000,9000,6000,2500,10000]},
# {"nombre":"Laura Castiblanco","area":"congelados","lider":"Alejandra","productos":["huevos","queso","hierbas","hongos","pescado"], "precio":[12000,12000,2000,2500,30000]},

# {
#     "nombre": "Jhonatan",
#     "area": "cosmeticos",
#     "lider": "Ducuara",
#     "productos": ["sombras", "esmalte", "crema facial", "serum", "toallitas desmaquillantes"],
#     "precio": [18000, 7000, 25000, 30000, 12000]
# },

# {
#     "nombre": "Jhonatan",
#     "area": "Perecederos",
#     "lider": "Ducuara",
#     "productos": ["lechuga", "tomate", "pera", "res", "cerdo"],
#     "precio": [3000, 3500, 2500, 27000, 21000]
# },

#  {
#     "nombre": "Jhonatan",
#     "area": "cosmeticos",
#     "lider": "Ducuara",
#     "productos": ["brillo labial", "mascarilla facial", "tinte de cejas", "crema antiarrugas", "kit de maquillaje"],
#     "precio": [8500, 22000, 15000, 27000, 45000]
# },

#  {
#     "nombre": "Jhonatan",
#     "area": "no perecederos",
#     "lider": "Ducuara",
#     "productos": ["arroz", "lentejas", "harina", "aceite", "azúcar"],
#     "precio": [5000, 4000, 3500, 12000, 4500]
# },
# {
#     "nombre": "Jhonatan",
#     "area": "congelados",
#     "lider": "Ducuara",
#     "productos": ["nuggets", "vegetales mixtos", "helado", "empanadas", "filete de merluza"],
#     "precio": [11000, 8000, 9500, 6000, 28000]
#     }
# ]

vendedores = [
    {'nombre': 'Maria Lopez', 'area': 'cosmeticos', 'líder': 'Jose Perez', 'productos': ['shampoo', 'jabón', 'bloqueador','crema dental','gel'], 'precio': [20000,10000,25000,12000,30000]},
    {"nombre":"Laura Castiblanco","area":"cosmeticos","lider":"Alejandra","productos":["Labial","rubor","polvos","base","iluminador"], "precio":[10000,15000,20000,25000,30000]},
    {"nombre":"Laura Castiblanco","area":"Perecederos","lider":"Alejandra","productos":["uvas","manzanas","bananos","carne","pollo"], "precio":[8000,1500,2000,25000,11000]},
    {"nombre":"Laura Castiblanco","area":"cosmeticos","lider":"Alejandra","productos":["pestañina","corrector","delineador","lapiz de labios","brochas"], "precio":[17000,15000,10000,2500,32000]},
    {"nombre":"Laura Castiblanco","area":"no perecederos","lider":"Alejandra","productos":["miel","atun","sopas","maiz enlatado","cafe"], "precio":[5000,9000,6000,2500,10000]},
    {"nombre":"Laura Castiblanco","area":"congelados","lider":"Alejandra","productos":["huevos","queso","hierbas","hongos","pescado"], "precio":[12000,12000,2000,2500,30000]},
    {"nombre": "Jhonatan", "area": "cosmeticos", "lider": "Ducuara", "productos": ["sombras", "esmalte", "crema facial", "serum", "toallitas desmaquillantes"], "precio": [18000, 7000, 25000, 30000, 12000]},
    {"nombre": "Jhonatan", "area": "Perecederos", "lider": "Ducuara", "productos": ["lechuga", "tomate", "pera", "res", "cerdo"], "precio": [3000, 3500, 2500, 27000, 21000]},
    {"nombre": "Jhonatan", "area": "cosmeticos", "lider": "Ducuara", "productos": ["brillo labial", "mascarilla facial", "tinte de cejas", "crema antiarrugas", "kit de maquillaje"], "precio": [8500, 22000, 15000, 27000, 45000]},
    {"nombre": "Jhonatan", "area": "no perecederos", "lider": "Ducuara", "productos": ["arroz", "lentejas", "harina", "aceite", "azúcar"], "precio": [5000, 4000, 3500, 12000, 4500]},
    {"nombre": "Jhonatan", "area": "congelados", "lider": "Ducuara", "productos": ["nuggets", "vegetales mixtos", "helado", "empanadas", "filete de merluza"], "precio": [11000, 8000, 9500, 6000, 28000]}
]

# 1. Promedio por vendedor
promedios = {}
for vendedor in vendedores:
    nombre = vendedor["nombre"]
    if nombre not in promedios:
        promedios[nombre] = {"suma": 0, "cantidad": 0}
    precios = vendedor["precio"]
    i = 0
    while i < len(precios):
        promedios[nombre]["suma"] = promedios[nombre]["suma"] + precios[i]
        promedios[nombre]["cantidad"] = promedios[nombre]["cantidad"] + 1
        i = i + 1

# print("Promedio de precios por vendedor:")
# for nombre in promedios:
#     suma = promedios[nombre]["suma"]
#     cantidad = promedios[nombre]["cantidad"]
#     promedio = suma / cantidad
#     print(nombre, ":", promedio)

# #vendedor que vende el producto mas costoso (de todos los productos) y decir cual es el producto y el vendedor
# mayor_precio = -1
# producto_mas_caro = ""
# vendedor_producto_caro = ""

# i = 0
# while i < len(vendedores):
#     vendedor = vendedores[i]
#     precios = vendedor["precio"]
#     productos = vendedor["productos"]
#     j = 0
#     while j < len(precios):
#         if precios[j] > mayor_precio:
#             mayor_precio = precios[j]
#             producto_mas_caro = productos[j]
#             vendedor_producto_caro = vendedor["nombre"]
#         j = j + 1
#     i = i + 1

# print("Producto más caro:", producto_mas_caro)
# print("Precio:", mayor_precio)
# print("Vendido por:", vendedor_producto_caro)

# #Mostrar el vendedor que vende el producto mas barato (de todos los productos) y decir cual es el producto y el vendedor
# menor_precio = 100000000  
# producto_mas_barato = ""
# vendedor_producto_barato = ""

# i = 0
# while i < len(vendedores):
#     vendedor = vendedores[i]
#     precios = vendedor["precio"]
#     productos = vendedor["productos"]
#     j = 0
#     while j < len(precios):
#         if precios[j] < menor_precio:
#             menor_precio = precios[j]
#             producto_mas_barato = productos[j]
#             vendedor_producto_barato = vendedor["nombre"]
#         j = j + 1
#     i = i + 1

# print("Producto más barato:", producto_mas_barato)
# print("Precio:", menor_precio)
# print("Vendido por:", vendedor_producto_barato)

# #Mostrar los lideres de los vendedores de productos perecederos. Mostrar el vendedor también
# i = 0
# while i < len(vendedores):
#     vendedor = vendedores[i]
#     if vendedor["area"] == "Perecederos":
#         print("Vendedor:", vendedor["nombre"])
#         print("Líder:", vendedor["lider"])
#         print("-----")
#     i = i + 11


