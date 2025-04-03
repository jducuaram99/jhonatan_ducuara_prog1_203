import random
c1=set()
c2=set()
tam=random.randint(15,20)
for i in range(tam):
    num=random.randint(1,20)
    c1.add(num)
tam=random.randint(15,20)
for i in range(tam):
    num=random.randint(1,20)
    c2.add(num)    


print("conjunto1", c1)
print("conjunto2", c2)
union=c1|c2
print(f"union{union}")
inter=c1&c2
print(f"interseccion{inter}")
diferencia=c1-c2
print(f"diferencia{diferencia}")
difsimetrica=c1^c2
print(f" diferencia simetrica{c1^c2}")
