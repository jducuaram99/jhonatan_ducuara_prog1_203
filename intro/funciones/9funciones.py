def maximo(v1, v2):
    while v2:
        v1, v2 = v2, v1 % v2
    return v1
def minimo(v1, v2):
    return (v1 * v2) // maximo(v1, v2)
v1 = int(input("ingrese primer numero"))
v2 = int(input("ingrese segundo numero"))
print(f"el mcm es {minimo(v1, v2)}")